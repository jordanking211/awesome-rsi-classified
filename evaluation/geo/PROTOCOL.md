# Search discovery and citation evaluation

This is an observation protocol, not a claim that GEO improvements have been demonstrated. The first recorded run was after the initial README changes. It cannot establish their causal effect.

## Fixed query set

Reuse queries N1–N6 in baseline-2026-10-08.json unchanged. These neutral questions are the primary discovery set. D1–D2 are branded/site diagnostics only and must not count toward neutral discovery success. Do not insert the repository name, URL, classification wording, or desired citation into later neutral prompts. New exploratory queries must be reported separately.

## Record each observation

Record time and timezone, live repository commit, tool/product, search mode, query, returned URL list, errors, and whether the exact target repository or its actual documentation site appears. Save only necessary metadata and URLs; do not republish third-party snippets or full answers without permission. Search-result order from web.run is not a native engine ranking. Results from another provider are a separate series.

The primary metric is queries returning the target divided by successful neutral queries. Failed calls are missing data, not misses. Report the denominator. Branded discovery, explicit URL retrieval, and AI answer citations are different metrics.

For independent answer-citation tests, use a fresh context without the target URL/name or prior repository knowledge, a fixed product/model/search mode, and the same neutral questions. Record actual linked source citations separately from name mentions. This chat's own answers cannot serve as independent citation evidence. If a surface is unavailable, label it not measured.

## Review cadence and stopping rule

Run the fixed set daily at 10:00 Asia/Shanghai. Inspect commit freshness when direct retrieval is possible, but never count direct retrieval as discovery. Avoid same-day repeated searches and keep results from different dates distinct. Review every seven days; after each substantive public-content change allow at least seven days for observation, extending that window if fresh content cannot be confirmed. Unchanged low visibility is not a reason to rewrite daily.

Operational discovery milestone: at least two of six neutral queries return the target on three measurement dates spanning at least seven days. This is a practical repeated-discovery threshold, not a statistical significance or causal claim.

Citation milestone: independently generated answers cite the target for at least two neutral prompts on three dates spanning at least seven days. Only claim this if those product surfaces were actually tested. Neither milestone proves the README edit caused the improvement; organic indexing and external changes remain confounders. Report discovery and citation separately and do not stop merely because branded search succeeds.

At 30 days review the evidence, remaining access limitations, and next hypothesis. Report inconclusive or negative evidence honestly; never change success criteria after seeing results or silently treat prolonged uncertainty as success. Continue low-frequency observation unless the user stops it, with meaningful updates only.

## Permitted improvements

Maintain the project's taxonomy and research-index scope. Make one evidence-motivated batch at a time, with source checks, bilingual parity, and a commit record. Preserve existing user changes and publish only reviewed in-scope corrections. Do not claim performance reproduction or change inspection dates without evidence. Avoid keyword stuffing, duplicate thin pages, fake mentions, unsolicited external messages, paid promotion, and misleading citations. Record each hypothesis and outcome, including failures.

## Initial finding — 2026-10-08

N1–N6: 0/6 returned the target. D1–D2: 0/2 returned the target. Repository metadata reports creation on 2026-10-07. The search tool returned off-target URLs even for the site query, so this result cannot establish that the repository is absent from every index. Independent AI citation rate is not measured. The immediate next step is repeat discovery measurement; further title rewrites have no demonstrated justification yet.
