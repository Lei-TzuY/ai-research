# AI Research Migration Protocol & Ledger

This document is the durable preflight, migration, and research-integration ledger for `Lei-TzuY/ai-research`.

## Status vocabulary

- **PRE-FLIGHT** — candidate identified; exact source verification is incomplete.
- **HOLD** — active implementation/research work makes the source checkpoint intentionally unstable.
- **ATTRIBUTION REVIEW** — source may otherwise be stable, but reachable history contains attribution metadata requiring an explicit preservation decision before migration.
- **READY FOR IMPORT** — exact source head, no conflicting PR, source-appropriate verification, attribution review, hygiene, and umbrella verification contract are all defined and clean.
- **IMPORTED / VERIFIED** — source history is preserved in umbrella ancestry, source tree equals imported subtree at the selected SHA, and source-equivalent umbrella verification is green.
- **INTEGRATION VERIFIED** — an executable cross-project research contract is permanently tested in addition to import verification.

## Phase 0 live preflight — 2026-09-07

### `tiny-transformer-autograd`

Observed source main: `a011903671efb97db0f73b50e081f4d45f5eab11`.

Status: **HOLD**.

The source still has multiple active research/integration lanes. Current examples include PR #172 (GQA/MQA integration), #177 (persistent KV-cache/beam stack), #178 (gradient centralization), and #179 (deterministic beam tie-breaking), in addition to other research helpers. Historical green CI on the common main base is not a license to freeze around active work. Re-evaluate source topology after the canonical integration lanes close or are explicitly superseded.

No umbrella import is performed at this checkpoint.

### `Quality_Assurance`

Observed source main: `fb507f911de661dfc37c4c3136ca22e1c8ebb8c9`.

- zero open PRs observed at Phase 0 preflight;
- exact-main Tests run `34045251168`: **success**;
- recent source history includes empirical-study closure and subsequent static-analysis work;
- at least one reachable commit (`565193e82903b6892ae2aed483f330b40bda2278`) contains `Co-authored-by: QuantPilot Developer <quantpilot@example.com>`.

Status: **ATTRIBUTION REVIEW**.

This metadata is not silently deleted or rewritten. Before migration, run a complete reachable-history scan, classify every configured attribution hit, record the preservation policy, and only then choose a freeze point. Scientific results and frozen-study boundaries remain historical evidence and are not rewritten by consolidation.

### `iqa-soa`

Observed source main: `802019b23f3e34396de10d2c1aeddf0456834640`.

- zero open PRs observed at Phase 0 preflight;
- no GitHub Actions run exists for the exact observed head;
- current source documentation explicitly records a Route-A manuscript/evidence hardening state while successor qualification/effectiveness work remains HOLD.

Status: **PRE-FLIGHT**.

Before this source can become READY, define a source-equivalent verification contract for the current repository. The umbrella must not convert manuscript/evidence HOLD wording into a confirmatory effectiveness claim.

## Attribution rule

Search results are first-pass evidence only. Every migration requires a complete reachable-history scan over the exact fetched source history. Configured markers include at least:

```text
Co-Authored-By
Generated-By
Assisted-By
Signed-off-by
Claude
Anthropic
OpenAI
other AI/bot attribution markers identified during review
```

Matches are classified and preserved or explicitly rejected according to provenance policy. Genuine source history is not falsified to produce a cleaner portfolio graph. New umbrella commits do not add these attribution trailers.

## History-preserving migration procedure

For each READY source:

1. recheck exact source `main`, open PRs, recent commits and required CI immediately before migration;
2. freeze source SHA and source tree SHA;
3. perform a non-squashed history-preserving import under `projects/<name>`;
4. prove the frozen source SHA remains reachable from umbrella history;
5. prove source root tree equals the imported subtree tree at that freeze point;
6. run the source-equivalent verification contract from the umbrella path;
7. remove temporary write-capable bootstrap machinery before publishing the migration PR;
8. normal-merge only after exact candidate verification;
9. rerun permanent verification on exact merged `main`.

A ZIP copy, archive copy, current-tree-only commit, or squash migration does not satisfy this protocol.

## Research integration evidence rule

Import verification and research integration are separate claims. A verified research edge must define:

- the named participants and exact imported source SHAs;
- a concrete artifact/workload/evidence schema shared across participants;
- a pre-specified hypothesis or acceptance rule;
- deterministic setup where applicable;
- executable failure semantics;
- explicit limitations and scientific claim boundary;
- exact PR-head and merged-main evidence.

A deterministic MWE may establish implementation consistency or evidence plumbing. It does not establish production effectiveness, generalization, statistical superiority, or a real-world effect unless a separately designed empirical study supports that claim.

## Original repository policy

Original repositories remain available after import while their issues, releases, study records, links, and historical context remain useful. Routine consolidation does not delete source repositories.
