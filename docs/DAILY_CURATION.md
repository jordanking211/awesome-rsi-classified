# 每日云端维护 / Daily cloud curation

GitHub Actions 每天北京时间 10:00（UTC 02:00）运行。GitHub 的定时触发可能延迟；电脑关机或 Codex 退出不影响云端运行。公开仓库长期没有活动时，GitHub 可能停用定时工作流，应在 Actions 页面检查状态。

The workflow runs daily at 10:00 Asia/Shanghai (02:00 UTC). GitHub may delay scheduled runs. It runs independently of your computer and Codex. GitHub can disable scheduled workflows in inactive public repositories; check the Actions page periodically.

## 模型配置 / Model configuration

在仓库 Settings → Secrets and variables → Actions 设置：

| Type | Name | Value |
| --- | --- | --- |
| Secret | `RSI_API_KEY` | Your model provider's API key; never commit it |
| Variable | `RSI_API_BASE` | HTTPS OpenAI-compatible API base, ending in `/v1` where required; the script appends `/chat/completions` |
| Variable | `RSI_MODEL` | An available model ID supporting chat completions with a sufficiently large context window |
| Variable | `RSI_ENABLED` | Set to `true` only after a successful full manual run; until then scheduled curation is skipped |

模型应支持至少约 40k tokens 上下文和 JSON 输出；正文可能包含最多五份源码片段。每天最多五次逻辑模型调用，每次输出上限 5,000 tokens；暂时错误最多重试两次。实际费用取决于提供商，请在提供商端设置预算。模型没有工具执行权，外部代码只作为文本读取。

Use a model with roughly 40k+ context capacity and reliable JSON output. Evidence can include up to five source excerpts. There are at most five logical model calls per run, each with a 5,000-token output limit; transient failures may be retried twice. Provider billing applies; set a provider-side budget. The model has no execution tools, and downloaded code is only read as text.

GitHub Models 已于 2026-07-30 退役，不能使用旧教程中的 `models: read` 免费推理方案。参见 [GitHub 官方说明](https://docs.github.com/en/github-models)。

GitHub Models was retired on 2026-07-30. The old `models: read` inference setup is unavailable; see [GitHub's notice](https://docs.github.com/en/github-models).

## 行为与验证 / Behavior and validation

- Search GitHub for recently active implementations and arXiv for recent relevant papers. The rolling windows are 30 days and 7 days respectively. Abstract-linked repositories can supplement keyword discovery. Search coverage is bounded and is not an exhaustive daily literature review.
- Deduplicate against the current READMEs. Select at most one candidate; read up to five implementation files at a fixed commit and recent commit metadata. README claims alone do not establish implementation or activity.
- Generate a structured bilingual entry, then conduct a separate model evidence review. Validate source quotes against actual numbered lines. Label the entry as static source inspection, with no experimental reproduction.
- Deterministic code inserts one overview row and one detail card per language, updates method counts, and checks language parity. A model cannot rewrite arbitrary repository files or workflows.
- `.github/rsi-state.json` records successful additions by Asia/Shanghai date. Scheduled and manual runs share a concurrency group and the same daily limit. With no qualified candidate, no tracked files change and no commit is made.
- Push without force. If another commit arrived during research, fail rather than overwrite or automatically merge it. Public evidence and draft reports are kept as Actions artifacts for 14 days, including on failure.
- Changes are machine-reviewed and may still contain errors. No automated review establishes generalization or guarantees absence of regressions.

在 Actions → Daily RSI discovery → Run workflow 中，勾选 `discovery_only` 可验证云端检索，无需模型密钥，不修改 README。取消勾选则执行完整流程。缺失模型配置时完整流程明确失败，不假装已完成维护。成功新增记录在提交历史与 workflow summary；失败可通过 GitHub Actions 通知查看。

Use Actions → Daily RSI discovery → Run workflow with `discovery_only` enabled to check discovery without model credentials, model calls, or README edits. Disable it to run full curation. Missing model configuration causes an explicit failure. Additions appear in commit history and workflow summaries; failures are available through GitHub Actions notifications.

Local validation: `python -m unittest discover -s tests -v`.

配置顺序：添加模型密钥与变量 → 手动完整试跑 → 设置 `RSI_ENABLED=true` → 停用原本地定时任务，避免双重维护。仅检索试跑成功不能证明模型调用或自动提交已验证。

Activation order: configure the model secret/variables, complete a full manual run, set `RSI_ENABLED=true`, then disable the old local scheduled task. A successful discovery-only run does not validate model calls or automatic publishing.
