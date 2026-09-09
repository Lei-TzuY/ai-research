# AI Research Migration Protocol & Ledger

This document is the durable preflight, migration, and research-integration ledger for `Lei-TzuY/ai-research`.

## Status vocabulary

- **PRE-FLIGHT** — candidate identified; exact source verification is incomplete.
- **HOLD** — active implementation/research work makes the intended source checkpoint unstable.
- **ATTRIBUTION REVIEW** — source may otherwise be stable, but reachable history contains provenance requiring an explicit preservation decision.
- **READY FOR IMPORT** — exact source head, zero conflicting implementation PRs, source-appropriate verification, attribution review, hygiene, and umbrella verification contract are clean.
- **IMPORTED / VERIFIED** — source history is preserved in umbrella ancestry, source tree equals imported subtree, and source-equivalent umbrella verification is green.
- **INTEGRATION VERIFIED** — an executable cross-project research contract is permanently tested in addition to import verification.

## Phase 0 live preflight — 2026-09-09

### `tiny-transformer-autograd` — HOLD

Observed source main: `a011903671efb97db0f73b50e081f4d45f5eab11`.

There are 81 open PRs. Representative active research/integration lanes include PR #172 (GQA/MQA), #177 (persistent KV-cache/beam), #178 (gradient centralization), and #179 (deterministic beam tie-breaking). Historical green CI does not authorize a freeze around active research history. No umbrella import is attempted.

### `Quality_Assurance` — READY FOR IMPORT

Selected source candidate: `273fe2b912e4a3e33874ae58f623878aec32978e`.
Source tree: `fab5550b2f694195cf1a0b6feb704003b94e63d7`.

#### Exact source verification

- zero open PRs at the live preflight;
- exact-main Tests run `34332582230`: **success**;
- Python 3.10 and 3.14 jobs install the package, byte-compile sources, execute the research artifact and Year-2 controlled evaluation, reproduce the documented deterministic summary/quality/traceability values, run the unit suite, and validate retained Year-2B evidence offline;
- Python 3.12 static job passes Ruff and mypy;
- Python 3.12 packaging job builds wheel + sdist, installs the wheel into a clean environment, and executes the installed research entrypoints.

#### Reachable-history attribution decision

The 95-entry canonical commit list reachable from the exact source head fits in the first 100-entry commits API page and page 2 is empty. Configured commit-message searches produced:

- `Co-authored-by`: exactly **one** hit, commit `565193e82903b6892ae2aed483f330b40bda2278`, trailer `Co-authored-by: QuantPilot Developer <quantpilot@example.com>`;
- `Generated-By`: 0;
- `Assisted-By`: 0;
- `Signed-off-by`: 0;
- `Claude`: 0;
- `Anthropic`: 0;
- `OpenAI`: 0.

Policy: preserve the QuantPilot Developer co-author trailer as genuine historical provenance. Do not rewrite or remove it during migration. A migration-time full Git-history audit must re-check the exact same conclusion before the source is admitted.

#### Scientific-record preservation

The attributed commit records the completed Year-3B retained study. Its own canonical message explicitly freezes the result boundary: 60/60 cells and 600/600 occasions matched their pre-specified four-way status pair, while the compromised-attestor signed-replay observation is a declared trust-model boundary. The record explicitly says these observations are not a detection rate, perfect-security claim, fresh-inference proof, or generalization beyond the frozen scenarios/targets.

Umbrella consolidation must preserve those frozen inputs, retained-evidence semantics, and claim boundaries unchanged. READY status does not authorize rerunning or relabelling the study. The later Year 2E closeout now present at the selected head is likewise preserved as a closed, bounded empirical record.

#### Migration transport blocker

The source repository is private. The currently available umbrella/connector credentials can edit both repositories but cannot transfer Git objects across repository object databases or authenticate an ancestry-preserving fetch from an umbrella workflow. Configure a narrowly scoped cross-repository credential with Contents: read access to `Quality_Assurance` before import. Do not substitute an archive/current-tree copy, which would fail the ancestry requirement.

### `iqa-soa` — PRE-FLIGHT / VERIFICATION ACTIVE

Observed source main before verification PR: `802019b23f3e34396de10d2c1aeddf0456834640`.

The source previously had no exact-head Actions run. Source PR #49 (`5f02fe94e445412749a425d8a0dfa4c53c614dfe`) adds a read-only verification workflow only:

- strict mypy on Python 3.11;
- full committed pytest suite on Python 3.11;
- full committed pytest suite on Python 3.13.

Workflow run `34065177947` is **red**: strict mypy succeeds, while Python 3.11 and 3.13 each finish with 186 failed, 3143 passed and 423 errors. Failures span conflicting lifecycle expectations and historical Git-worktree reconstruction; this is not an exact-head verification checkpoint. The PR changes no implementation, frozen evidence, or scientific status. Do not merge it or promote `iqa-soa` to READY until the committed suite has a defined current-state contract and both exact PR-head and exact merged source `main` pass it. Existing source documentation's successor-study/effectiveness HOLD boundaries remain authoritative.

`iqa-soa` is also private, so after source CI is repaired it will require the same scoped cross-repository Contents: read migration credential described above.

## Attribution rule

Search/API results are preflight evidence. Every actual migration still requires a complete reachable-history scan over the exact fetched source Git history. Configured markers include `Co-Authored-By`, `Generated-By`, `Assisted-By`, `Signed-off-by`, Claude, Anthropic, OpenAI, and any additional AI/bot attribution discovered during review.

Matches are classified and preserved according to provenance policy. Genuine source history is not falsified to produce a cleaner portfolio graph. New umbrella commits do not add attribution trailers.

## History-preserving migration procedure

For each READY source:

1. recheck exact source `main`, open PRs, recent commits and required CI immediately before migration;
2. freeze source SHA and tree SHA;
3. run the complete source-history provenance/hygiene audit;
4. perform a non-squashed import under `projects/<name>`;
5. prove the frozen source SHA remains umbrella ancestry;
6. prove source root tree equals imported subtree tree;
7. run source-equivalent verification from the umbrella path;
8. remove temporary write-capable bootstrap machinery before publishing the migration PR;
9. normal-merge only after exact candidate verification;
10. rerun permanent verification on exact merged `main`.

A ZIP/archive/current-tree copy or squash migration does not satisfy this protocol.

## Research integration evidence rule

Import verification and research integration are separate claims. A verified edge must define named participants and exact source SHAs, a concrete shared artifact/workload/evidence schema, a pre-specified hypothesis or acceptance rule, executable failure semantics, explicit limitations, and exact PR-head plus merged-main evidence.

A deterministic MWE may establish implementation consistency or evidence plumbing. It does not establish production effectiveness, generalization, statistical superiority, or a real-world effect unless a separately designed empirical study supports that claim.

## Original repository policy

Original repositories remain available after import while their issues, releases, study records, links, and historical context remain useful. Routine consolidation does not delete source repositories.
