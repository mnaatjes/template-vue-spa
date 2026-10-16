---
title: "Adopt Copier Template Architecture for Vue 3 SPAs"
status: "accepted"
date: "2026-10-16"
tags: ["template", "vue3", "typescript", "copier", "fsd"]
---

# 1. Context and Problem Statement

Downstream frontend applications across the homelab and client ecosystems need rapid, deterministic, and repeatable scaffolding. Without architectural governance, frontends suffer from leaky boundaries (business logic mixed with UI views), brittle state management, unvalidated backend API payloads, and untyped configurations.

# 2. Decision Drivers

* **Deterministic Decoupling:** Enforce strict boundaries between presentation, business rules, and entities using Feature-Sliced Design (FSD).
* **Upstream Synchronization:** Leverage Copier to propagate template updates, bug fixes, and security patches without manual downstream diffing.
* **Non-Bypassable Verification:** Guarantee layer boundary rules via compile-time AST linting, architectural test suites, pre-commit quality gates, and downstream CI.
* **Autonomous AI Alignment:** Ensure AI agents follow strict invariants codified directly in `.gemini/rules/frontend_fsd_invariants.md`.

# 3. Considered Options

* Option 1: Ad-hoc scaffolding using `npm create vue@latest`.
* Option 2: Monolithic frontend/backend template.
* Option 3: Dedicated Copier template generator (`template-vue-spa`) adhering to Unified Process and Feature-Sliced Design.

# 4. Decision Outcome

Chosen Option: Option 3 (`template-vue-spa`).

## Positive Consequences

* Scaffolds production-ready Vue 3 + TypeScript + Vite + Pinia SPAs in seconds.
* Dual-plane repository design separates template lifecycle from downstream app payloads.
* Downstream apps inherit automated pre-commit gates, Vitest boundary tests, and GitHub Actions CI/release pipelines.
