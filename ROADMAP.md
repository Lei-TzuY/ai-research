# AI Research Roadmap

## Phase 0 — Governance bootstrap

- [x] create the `ai-research` umbrella;
- [x] define the three core research layers without claiming interoperability;
- [x] establish research-validity and provenance invariants;
- [x] create a machine-checked migration ledger and read-only validator;
- [x] recheck live source heads/open PRs/CI before assigning Phase 0 status;
- [ ] resolve source-specific freeze blockers and move candidates to `ready-for-import` only with explicit evidence.

Current live preflight:

- `tiny-transformer-autograd@a011903671efb97db0f73b50e081f4d45f5eab11` — **HOLD** while multiple implementation/research PRs remain active, including the GQA/MQA, KV-cache, gradient-centralization, and deterministic beam-tie tracks;
- `Quality_Assurance@fb507f911de661dfc37c4c3136ca22e1c8ebb8c9` — **ATTRIBUTION REVIEW**; exact-main Tests run `34045251168` is green and there are zero open PRs, but reachable source history contains attribution metadata that must be reviewed/preserved explicitly before migration;
- `iqa-soa@802019b23f3e34396de10d2c1aeddf0456834640` — **PRE-FLIGHT**; zero open PRs, but no exact-head GitHub Actions run was observed, so source-equivalent verification still needs to be defined and executed.

## Phase 1 — Stable source freeze points

For each source:

1. re-read exact live `main`, open PRs, recent commits, workflow state, and repository hygiene;
2. reject a freeze while an implementation/research lane is actively changing the intended checkpoint;
3. scan the complete reachable history for configured attribution metadata and document the preservation decision rather than rewriting genuine history;
4. define the exact source-equivalent umbrella gate before migration;
5. record the selected source tree SHA and licensing/metadata state.

Planned order is evidence-driven, not name-driven. A clean `Quality_Assurance` or `iqa-soa` checkpoint may be imported before `tiny-transformer-autograd` if the latter remains active.

## Phase 2 — History-preserving migration

For each stable source:

- [ ] preserve source ancestry with a non-squashed import under `projects/<name>`;
- [ ] prove exact source tree ↔ imported subtree equality;
- [ ] run source-equivalent verification from the umbrella path;
- [ ] publish a migration PR only after temporary/bootstrap write machinery is removed;
- [ ] normal-merge only after the exact PR head is green;
- [ ] rerun the permanent gate on exact merged `main`.

A ZIP/current-tree copy or squash import does not satisfy this phase.

## Phase 3 — Bounded research integration

Do not infer a chain merely from co-location. The first verified edge should use one explicit evidence boundary. Candidate classes include:

- mechanism output from `tiny-transformer-autograd` consumed by a quality/evidence contract in `Quality_Assurance`;
- a `Quality_Assurance` machine-readable quality condition/evidence envelope executed through `iqa-soa` runtime governance;
- a deterministic research artifact whose producer, checker, provenance, and acceptance rule are all frozen and replayable.

Before implementation, write the exact hypothesis, artifact schema, expected result, failure semantics, and claim boundary. A passing toy contract proves only that contract.

## Phase 4 — AI research flagship checkpoint

A flagship checkpoint requires all of the following:

- all selected source histories preserved and independently verified;
- at least one non-trivial cross-project research edge permanently executable;
- machine-readable evidence distinguishes hypothesis, deterministic verification, and empirical result status;
- README/ledger claims are no broader than the executed evidence;
- original repositories remain available for issues, releases, study records, and historical references.

## Non-goals

- merging active research branches merely to make umbrella progress appear faster;
- rewriting historical attribution or study outcomes;
- relabelling deterministic MWE results as production effectiveness;
- claiming statistical generalization without the required study design/data;
- forcing all three repositories into one framework or runtime;
- deleting source repositories as part of routine consolidation.
