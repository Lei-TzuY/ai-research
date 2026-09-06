# AI Research

`ai-research` is a research umbrella for building AI/ML systems that can be checked at multiple evidence layers: mathematical mechanism, implementation correctness, behavioral quality, runtime governance, and reproducible empirical evidence.

The objective is not to collect unrelated AI demos. The intended research stack is:

```text
mechanism / numerical ground truth
        tiny-transformer-autograd
                 ↓
validation / trustworthiness methods
          Quality_Assurance
                 ↓
runtime governance / auditable execution
              iqa-soa
```

The arrows above are **research architecture**, not verified cross-project interoperability. A cross-project edge is claimed only after the same concrete artifact, workload, result envelope, or evidence contract is executed by both sides and permanently regression-tested.

## Core projects

| Project | Research role | Live Phase 0 status |
| --- | --- | --- |
| `tiny-transformer-autograd` | Mechanism / foundation: tensor, autograd, Transformer math, numerical behavior, controlled ablations | **HOLD** — multiple active research/integration PRs own the source surface |
| `Quality_Assurance` | Validation / trustworthiness: machine-readable quality constraints, evidence models, deterministic and empirical QA studies | **ATTRIBUTION REVIEW** — exact main tests are green, but reachable history contains attribution metadata that must be preserved/reviewed explicitly before migration |
| `iqa-soa` | Runtime governance / service-oriented evaluation: requirement-to-check execution, auditability, fail-closed evaluation, evidence/provenance boundaries | **PRE-FLIGHT** — no open PR, but no exact-main Actions run was observed for the current head |

No project is treated as imported merely because it appears in this table. `projects/manifest.json` is the machine-checked migration ledger.

## Research-validity invariants

1. Research validity is a hard constraint, not a presentation preference.
2. Hypotheses remain hypotheses until supported by pre-specified executable or empirical evidence.
3. A deterministic small MWE does not become an industrial-effectiveness or generalization claim.
4. Frozen study inputs/results are not silently changed after outcomes are known.
5. Source history is preserved rather than rewritten to manufacture a cleaner provenance story.
6. Import verification and cross-project research integration are separate claims.
7. New umbrella commits do not add `Co-Authored-By`, `Generated-By`, `Assisted-By`, `Signed-off-by`, Claude/Anthropic/OpenAI, or other AI/bot attribution trailers.

## Migration model

A source may be imported only after live-state preflight establishes a stable freeze point: exact source `main`, no conflicting implementation PR, source-appropriate CI or an explicitly defined replacement gate, complete reachable-history attribution review, repository hygiene review, and a source-equivalent umbrella CI contract.

Imports must preserve source ancestry with non-squashed history and prove source-tree ↔ imported-subtree equivalence. Original repositories remain available; migration is consolidation, not deletion.

## Current checkpoint

This repository is at **Phase 0 governance bootstrap**. The next milestone is not “three directories copied in.” It is to resolve each source's freeze blocker honestly, import stable sources with history intact, and then define one bounded research edge whose evidence can be reproduced from the umbrella without broadening the scientific claim.

See [ROADMAP.md](ROADMAP.md) and [docs/MIGRATION.md](docs/MIGRATION.md).
