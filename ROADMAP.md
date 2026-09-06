# AI Research Roadmap

## Phase 0 — Governance bootstrap

- [x] create the `ai-research` umbrella;
- [x] define the three core research layers without claiming interoperability;
- [x] establish research-validity and provenance invariants;
- [x] create a machine-checked migration ledger and read-only validator;
- [x] recheck live source heads/open PRs/CI before assigning source status;
- [x] resolve `Quality_Assurance` attribution review and promote its exact source checkpoint to READY FOR IMPORT;
- [ ] finish `iqa-soa` source verification PR #49 and require exact merged-main CI before READY;
- [ ] keep `tiny-transformer-autograd` on HOLD until its active research lanes settle.

Current live preflight:

- `tiny-transformer-autograd@a011903671efb97db0f73b50e081f4d45f5eab11` — **HOLD** while multiple research/integration PRs remain active, including GQA/MQA, KV-cache, gradient-centralization and deterministic beam-tie tracks;
- `Quality_Assurance@fb507f911de661dfc37c4c3136ca22e1c8ebb8c9` — **READY FOR IMPORT**; exact-main Tests `34045251168` is green across Python 3.10/3.14 behavioral/evidence checks, Python 3.12 Ruff/mypy, and wheel/sdist verification; one historical QuantPilot co-author trailer is explicitly preserved, all other configured attribution markers are zero;
- `iqa-soa@802019b23f3e34396de10d2c1aeddf0456834640` — **PRE-FLIGHT / VERIFICATION ACTIVE**; source PR #49 adds read-only exact-head CI with strict mypy plus full pytest on Python 3.11/3.13 without changing scientific status.

## Phase 1 — Stable source freeze points

For each source:

1. re-read exact live `main`, open PRs, recent commits, workflow state and repository hygiene;
2. reject a freeze while an implementation/research lane is actively changing the intended checkpoint;
3. scan complete reachable history and record an explicit preservation decision for every attribution hit;
4. define the exact source-equivalent umbrella gate before migration;
5. record selected source tree SHA and licensing/metadata state.

### `Quality_Assurance` freeze candidate

- [x] exact source `fb507f911de661dfc37c4c3136ca22e1c8ebb8c9`, tree `6aeca34f2690a11b47d60d840976ce37368bc2f6`;
- [x] zero open PRs at preflight;
- [x] exact-main Tests run `34045251168` success, all four jobs green;
- [x] canonical commit list exhausted at API page 1; page 2 empty;
- [x] exactly one `Co-authored-by` hit: QuantPilot Developer on `565193e...`; preserve it;
- [x] Generated-By / Assisted-By / Signed-off-by / Claude / Anthropic / OpenAI: zero;
- [x] preserve the frozen Year-3B study claim boundary and evidence semantics unchanged.

## Phase 2 — History-preserving migration

For each stable source:

- [ ] preserve source ancestry with a non-squashed import under `projects/<name>`;
- [ ] prove exact source tree ↔ imported subtree equality;
- [ ] run source-equivalent verification from the umbrella path;
- [ ] publish a migration PR only after temporary/bootstrap write machinery is removed;
- [ ] normal-merge only after exact PR-head verification;
- [ ] rerun the permanent gate on exact merged `main`.

A ZIP/current-tree copy or squash import does not satisfy this phase.

## Phase 3 — Bounded research integration

Do not infer a chain merely from co-location. Candidate edges include:

- mechanism output from `tiny-transformer-autograd` consumed by a quality/evidence contract in `Quality_Assurance`;
- a `Quality_Assurance` machine-readable quality/evidence envelope executed through `iqa-soa` runtime governance;
- a deterministic research artifact whose producer, checker, provenance and acceptance rule are frozen and replayable.

Before implementation, write the exact hypothesis, artifact schema, expected result, failure semantics and claim boundary. A passing bounded contract proves only that contract.

## Phase 4 — AI research flagship checkpoint

Requires:

- all selected source histories preserved and independently verified;
- at least one non-trivial cross-project research edge permanently executable;
- machine-readable evidence distinguishes hypothesis, deterministic verification and empirical-result status;
- README/ledger claims are no broader than the executed evidence;
- original repositories remain available for study records and historical references.

## Non-goals

- merging active research branches merely to make umbrella progress look faster;
- rewriting historical attribution or study outcomes;
- relabelling deterministic MWE results as production effectiveness;
- claiming statistical generalization without the required study design/data;
- forcing all projects into one framework or runtime;
- deleting source repositories as routine consolidation.
