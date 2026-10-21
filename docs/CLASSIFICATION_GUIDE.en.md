# How to classify self-improving agents: modification targets, training boundaries, and recursion

[中文](CLASSIFICATION_GUIDE.md) | **English** | [Full taxonomy](../README.en.md)

This guide explains the classification method used by Awesome RSI Classified. **Identify what a system writes back, then check which components are trained, whether later execution uses the update, and what evidence supports effectiveness.** The nine modification targets describe implementations; they are not capability levels or a universal definition of RSI.

This guide synthesizes existing classification evidence. It adds no performance reproduction and does not advance source-inspection dates. Follow the linked entries for inspected versions and scope.

## Contents

- [Which questions determine a classification?](#decision)
- [How do prompts, memory, and skills differ?](#prompt-memory-skill)
- [How does agent modification differ from program evolution?](#agent-versus-program)
- [Do frozen weights mean that no learning occurs?](#training)
- [What evidence supports discussing recursive self-improvement?](#recursion)
- [How should a classification be recorded and cited?](#evidence)

<a id="decision"></a>
## Which questions determine a classification?

**Classify a method's particular implementation path, rather than an entire project name.** One framework can support prompt optimization, training, and code generation. Findings about one optimizer do not cover every optimizer in that framework.

1. **Compare the artifacts retained before and after an update.** Are they instructions, experience, callable skills, workflows, event hooks, agent code, task programs, weights, or research artifacts? Producing reflection text alone does not establish a persistent update.
2. **Locate write-back and loading.** Which file, variable, database, or checkpoint changes? Where does a later iteration read it? Saving an artifact does not establish that execution uses it.
3. **Keep a primary target and document secondary targets.** Classify by the main object in the inspected optimization path, without hiding coupled changes.
4. **Separate training from inference.** Which model or controller receives parameter updates? Calling a frozen model to generate code does not train that model.
5. **Assess recursion and effectiveness separately.** Recursive structure, transfer, old-task regression, and cost each require evidence beyond a category label.

See the [nine-category table](../README.en.md#taxonomy) and [method overview](../README.en.md#overview) for definitions and implementation evidence.

<a id="prompt-memory-skill"></a>
## How do prompts, memory, and skills differ?

**Classify by the updated artifact's role in later execution, not its file extension.** Markdown can contain instructions, experience, or skills. Code can implement a reusable skill, the agent itself, or one task answer.

| Question | Likely target | Example and scope |
| --- | --- | --- |
| Are module instructions or demonstrations replaced? | Prompts | [MIPROv2](../README.en.md#miprov2) searches and assigns instructions / demos; this covers the inspected optimizer |
| Is experience or reflection retained and later retrieved or injected? | Memory | The inspected [Reflexion](../README.en.md#reflexion) path updates reflections and places them in subsequent prompts |
| Are reusable, callable procedures accumulated? | Skills | [Voyager](../README.en.md#voyager) stores JavaScript skills and descriptions, and retrieves skill code |

Primary materials: [MIPROv2 paper](https://arxiv.org/abs/2406.11695), [Reflexion paper](https://arxiv.org/abs/2303.11366), and [Voyager paper](https://arxiv.org/abs/2305.16291). The linked index entries include source locations at pinned commits.

**An ambiguous case:** [GEPA](../README.en.md#gepa) candidates contain text components; adapters determine whether those components act as prompts, skills, or code. Text optimization does not make every GEPA application prompt-only, and a skill label does not establish an executable skill library. See the [GEPA paper](https://arxiv.org/abs/2507.19457) and the linked implementation entry.

<a id="agent-versus-program"></a>
## How does agent modification differ from program evolution?

**Agent modification changes the system that executes tasks or produces improvements; task-program evolution changes a solution submitted by that system.** Both can generate Python files, run evaluations, and retain versions. Trace who loads the candidate and what responsibility it takes on.

| Dimension | Agent source modification | Target-task program evolution |
| --- | --- | --- |
| Primary object | Agent, harness, or improver implementation | Function or program solving a target task |
| Subsequent role | Part of the execution or improvement system | Candidate solution evaluated or deployed |
| Indexed example | [SICA](../README.en.md#sica): the current coding agent's codebase | [OpenEvolve](../README.en.md#openevolve): the target program and candidate population |
| Unsupported inference | Every edit improves future improvement capability | A better solution means a better improver |

Primary sources: [SICA paper](https://arxiv.org/abs/2504.15228) and [OpenEvolve repository](https://github.com/algorithmicsuperintelligence/openevolve). Their index entries describe the source-inspection scope.

**Counterexample:** A fixed searcher repeatedly generating faster sorting functions can form a program-optimization loop. Repetition alone does not establish recursive improvement of the search mechanism if that mechanism never changes. This is a classification example, not an experimental result.

<a id="training"></a>
## Do frozen weights mean that no learning occurs?

**Frozen model weights only establish that the relevant parameters are not updated.** Prompts, memory, skills, and code can still change subsequent system behavior. Whether these changes generalize in a meaningful learning sense requires separate evaluation.

The reverse mistake also matters: no base-model fine-tuning does not mean that every component remains untrained. Workflow graph parameters, auxiliary models, or experts may be fitted separately. Record edited artifacts, trained components, and training/deployment stages rather than a single system-wide training flag. See [workflow methods](../README.en.md#workflow) and [weight or coupled updates](../README.en.md#weights).

<a id="recursion"></a>
## What evidence supports discussing recursive self-improvement?

**Under this index's stricter inspection lens, trace whether the improvement mechanism changes and whether the changed mechanism participates in later improvement.** This is an analysis condition, not a claim that the field has only one definition.

- **A better task answer:** evidence of improvement on that task, insufficient on its own to establish a persistent system update.
- **An updated artifact used later:** evidence of an update loop; still identify whether the artifact is a solution or part of the improvement system.
- **An updated improvement mechanism used in the next round:** grounds for examining recursive structure, while sustained gains, transfer, and safety still require experiments.

These evidence distinctions are not a universal capability leaderboard. See [recursive boundaries](../README.en.md#recursive-boundary) for the broader discussion and method links.

<a id="evidence"></a>
## How should a classification be recorded and cited?

Record **method and implementation version → primary target → secondary targets → write-back location → subsequent loading location → trained components → inspection scope → unresolved questions**. Mark missing evidence as unverified instead of substituting a project's promotional description.

For example: “The inspected Reflexion path updates and injects reflection text, supporting a memory classification; this does not constitute a performance reproduction.” This scoped statement fits the available evidence better than asserting that the project has established general RSI.

To cite this guide's classification reasoning, include the repository name, guide URL, section anchor, commit SHA, and access date. For a method's mechanism or performance claim, also cite its original paper and relevant implementation. Press `y` on a GitHub file page for a commit permalink. See [citation guidance](../README.en.md#citation) and [contribution rules](../CONTRIBUTING.md).
