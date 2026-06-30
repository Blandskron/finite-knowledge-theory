# 🌌 Finite Knowledge Theory (FKT) - Scientific Laboratory

> **Canonical Scientific Research Laboratory for the Finite Knowledge Theory**
> 
> *A scalable research repository designed to support years of independent, parallel investigation by human scientists and autonomous AI agents.*

---

## 🧭 Vision

The long-term objective of this laboratory is to discover whether it is possible to represent every natural language, programming language, and structured document using a **finite hierarchy of foundational primitives**. 

This repository serves as the permanent memory and environment where FKT research is produced, challenged, documented, approved, and preserved.

---

## 📜 Laboratory Philosophy

We maintain five immutable research principles:

1.  **Research before implementation:** Never write production code before understanding the problem. Research always comes first.
2.  **Every decision must be documented:** Every architectural or theoretical decision becomes permanent documentation. No undocumented decisions are allowed.
3.  **Everything must be challenged:** Do not assume existing AI architectures, Transformers, or tokenizers are optimal. Question every assumption.
4.  **First Principles:** Always reason from mathematics and information theory before software engineering. The implementation must emerge from the theory.
5.  **The repository itself is part of the research:** Documentation, architecture, experiments, results, failures, and ideas all belong to the repository.

---

## 🔬 Multi-Agent Collaborative Research

To support parallel, independent investigations:
*   **Isolated Workspace:** AI models and researchers operate inside dedicated slots (e.g., `research/gpt/`, `research/claude/`, `research/gemini/`, `research/deepseek/`).
*   **Scientific Consensus:** Validated conclusions are promoted to the shared database (`research/shared/`) via formal promotion processes linked to Architectural Decision Records (ADRs).
*   **Trazabilidad Histórica:** Failed hypothesis and rejected ideas are preserved under status `🔴 Rejected` to serve as valuable learning resources.

---

## 📁 Repository Layout

```txt
finite-knowledge-theory/
├── README.md               # Human-facing introduction and principles
├── AGENTS.md               # Agent entry point and operational constraints
├── GEMINI.md               # Instructions for Gemini agents
├── LICENSE                 # License file
├── prompts/                # Canonical prompts of the repository
├── docs/                   # Guides, changelogs, and agent meta-docs
│   └── RESEARCH_LAB_ARCHITECTURE.md # Master layout and workflows standard
├── research/               # Investigation workspaces (isolated & shared)
├── adr/                    # Architectural Decision Records (ADRs)
├── specification/          # Language-agnostic specifications
├── reference-implementation/ # Canon and optimized implementation source code
├── validation/             # Compliance and validation test vectors
├── benchmarks/             # Portability, throughput, and memory benchmarks
├── experiments/            # Reproducible simulations and math checks
├── examples/               # Practical integration examples
└── scripts/                # Repository maintenance scripts
```

For a comprehensive guide on directory responsibilities, workflows, and promotion rules, see:
👉 [FKT Research Laboratory Architecture Standard (docs/RESEARCH_LAB_ARCHITECTURE.md)](docs/RESEARCH_LAB_ARCHITECTURE.md)

---

## 🤖 For AI Agents

If you are an AI assistant or coding agent working in this repository, you **must** read and follow the instructions in:
👉 [AGENTS.md](AGENTS.md)

---

## ⚖️ License

Licensed under the MIT License. See [LICENSE](LICENSE) for details.
