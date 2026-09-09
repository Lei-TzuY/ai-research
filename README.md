# AI Research

`ai-research` is a research umbrella for AI/ML systems whose mechanism, implementation, behavioral quality, runtime governance, and empirical evidence can be checked independently.

```text
mechanism / numerical ground truth
        tiny-transformer-autograd
                 ↓
validation / trustworthiness
          Quality_Assurance
                 ↓
runtime governance / auditable execution
              iqa-soa
```

These arrows are **research architecture, not verified interoperability**. A cross-project edge is claimed only after a concrete artifact/workload/evidence contract is executed by both sides and permanently regression-tested.

## Core projects

| Project | Research role | Live status |
| --- | --- | --- |
| `tiny-transformer-autograd` | tensor/autograd/Transformer mechanism and numerical behavior | **HOLD** — 81 open research/integration PRs still own the intended checkpoint |
| `Quality_Assurance` | validation, quality constraints, deterministic/empirical evidence | **READY FOR IMPORT** — exact-main Tests `34332582230` green; complete 95-commit attribution review resolved with one preserved QuantPilot co-author trailer |
| `iqa-soa` | runtime governance, auditable/fail-closed evaluation | **PRE-FLIGHT / CI RED** — source PR #49 passes strict mypy but its full Python 3.11/3.13 pytest jobs fail |

No project is treated as imported merely because it appears here. `projects/manifest.json` is the machine-checked migration ledger.

### `Quality_Assurance` preservation decision

The exact candidate is `273fe2b912e4a3e33874ae58f623878aec32978e`, tree `fab5550b2f694195cf1a0b6feb704003b94e63d7`. Its 95-commit canonical history fits in one 100-entry API page and page 2 is empty. Configured attribution searches find exactly one `Co-authored-by` hit: `QuantPilot Developer <quantpilot@example.com>` on commit `565193e82903b6892ae2aed483f330b40bda2278`; Generated-By, Assisted-By, Signed-off-by, Claude, Anthropic and OpenAI are zero.

That trailer is preserved, not rewritten. The commit records the completed Year-3B retained study and explicitly bounds its 600/600 exact status-pair observation: it is **not** a detection-rate, perfect-security, or generalization claim. Consolidation does not alter that frozen scientific record.

## Research-validity invariants

1. Hypotheses remain hypotheses until supported by pre-specified executable or empirical evidence.
2. Deterministic MWE evidence does not become an industrial-effectiveness/generalization claim.
3. Frozen study inputs/results are not silently changed after outcomes are known.
4. Source history and genuine provenance are preserved rather than cosmetically rewritten.
5. Import verification and cross-project research integration remain separate claims.
6. New umbrella commits add no AI/bot attribution trailers.

## Migration model

A source may be imported only after live-state preflight establishes a stable freeze point: exact source `main`, no conflicting implementation PR, source-appropriate CI, reachable-history attribution review, hygiene review, and an explicit source-equivalent umbrella gate.

Imports must preserve source ancestry with non-squashed history and prove source-tree ↔ imported-subtree equivalence. Original repositories remain available; migration is consolidation, not deletion.

`Quality_Assurance` and `iqa-soa` are private. Their source readiness is separate from migration transport: the umbrella currently has no credential that can read Git objects from those repositories. A scoped cross-repository Contents: read credential must be configured before their exact history can be imported; a current-tree copy is not an acceptable substitute.

See [ROADMAP.md](ROADMAP.md), [docs/MIGRATION.md](docs/MIGRATION.md), and [docs/RESEARCH_VALIDITY.md](docs/RESEARCH_VALIDITY.md).
