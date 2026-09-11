# AI Research Roadmap

## Phase 0 — Governance bootstrap

- [x] create the `ai-research` umbrella;
- [x] define four core research layers without claiming interoperability;
- [x] establish research-validity and provenance invariants;
- [x] create a machine-checked migration ledger and read-only validator;
- [x] recheck live source heads/open PRs/CI before assigning source status;
- [x] retain the historical `Quality_Assurance@273fe2b...` preservation decision without pretending it still freezes the advanced source;
- [x] repair and merge `iqa-soa` source verification PR #49 after exact-head CI turned green;
- [x] admit `SE-and-AGI` as the fourth core candidate at the software-engineering lifecycle/traceability layer;
- [ ] re-freeze `Quality_Assurance@312cdc9...` after complete new-main attribution, hygiene, tree and exact-main CI review;
- [ ] complete `iqa-soa@07c92ed...` merged-main CI identity, provenance, hygiene and tree freeze before READY;
- [ ] complete `SE-and-AGI@b797b8d...` exact-main CI, provenance, hygiene, tree, license and source-equivalent contract preflight;
- [ ] keep `tiny-transformer-autograd` on HOLD until its active research lanes settle.

Current live preflight:

- `tiny-transformer-autograd@a011903671efb97db0f73b50e081f4d45f5eab11` — **HOLD** with 81 open PRs; representative active lanes include #172, #177, #178 and #179;
- `Quality_Assurance@312cdc907275848860fb86dfb0f3d6e314c0bb18` — **PRE-FLIGHT REFRESH**; PR #34 exact head `37e59c7...` passed Tests `34546487697` and ICST artifact `34546487654`, but the old 95-commit READY freeze is superseded;
- `iqa-soa@07c92ed5add3058b06be0b86263782923689b886` — **PRE-FLIGHT / PR CI GREEN**; repaired PR #49 head `0519177...` passed CI `34541093055` and merged; exact-main/provenance/tree freeze remains;
- `SE-and-AGI@b797b8d57ae65cfd2a33f3e1aee25f2285df7b07` — **PRE-FLIGHT**; PR #2 head `3c8ab77...` passed tests `33312614630`; exact-main/provenance/tree/license freeze remains.

## Phase 1 — Stable source freeze points

For each source:

1. re-read exact live `main`, open PRs, recent commits, workflow state and repository hygiene;
2. reject a freeze while an implementation/research lane is actively changing the intended checkpoint;
3. scan complete reachable history and record an explicit preservation decision for every attribution hit;
4. define the exact source-equivalent umbrella gate before migration;
5. record selected source tree SHA and licensing/metadata state.

### Historical `Quality_Assurance` freeze candidate — superseded

- [x] exact source `273fe2b912e4a3e33874ae58f623878aec32978e`, tree `fab5550b2f694195cf1a0b6feb704003b94e63d7`;
- [x] zero open PRs at preflight;
- [x] exact-main Tests run `34332582230` success, all four jobs green;
- [x] all 95 canonical commits exhausted at API page 1; page 2 empty;
- [x] exactly one `Co-authored-by` hit: QuantPilot Developer on `565193e...`; preserve it;
- [x] Generated-By / Assisted-By / Signed-off-by / Claude / Anthropic / OpenAI: zero;
- [x] preserve the frozen Year-3B study claim boundary and evidence semantics unchanged.

This preservation decision remains valid for the historical checkpoint, but source readiness is no longer current because Year 2F-1/2 advanced `main`. After the new source is frozen, history transfer will still be blocked until `ai-research` has a scoped cross-repository Contents: read credential for the private source. Do not replace ancestry-preserving import with a ZIP or current-tree copy.

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
- an `SE-and-AGI` lifecycle trace binding requirements, implementation/tests and immutable evidence references from another imported research project;
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
