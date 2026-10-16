---
title: "Feature-Sliced Design Architectural Invariants"
tags: ["fsd", "architecture", "vue3", "invariants"]
---

# Feature-Sliced Design Architectural Invariants

All code modifications across this frontend repository must strictly comply with Feature-Sliced Design (FSD) structural invariants:

## Invariant 1: Shared Layer Purity (`src/shared/`)
* Components and utilities under `src/shared/` must NEVER import anything from `src/entities/`, `src/features/`, `src/pages/`, or `src/app/`.
* `src/shared/` components must be presentationally pure and driven strictly by props and events.

## Invariant 2: Slice Isolation (`src/features/`)
* Features must never directly cross-import from other sibling features.
* Shared business logic between features belongs in `src/entities/` or higher composition in `src/pages/`.

## Invariant 3: Runtime Schema Validation (`src/shared/api/`)
* All incoming HTTP API responses must be validated against a `zod` schema before consumption by stores or components.
* Never use raw untyped `any` or cast raw network payloads.

## Invariant 4: Store Isolation (`src/entities/`)
* Pinia stores in `src/entities/` must not invoke browser lifecycle hooks (`onMounted`, `onUnmounted`) directly.
* Stores are pure reactive state containers. Lifecycle triggers belong in component setup scripts.

## Invariant 5: Testing Contracts
* Every component in `src/features/` or `src/shared/ui/` must have a corresponding unit test file in `tests/unit/`.
* Architectural layer import rules are guarded by `tests/architecture/test_boundaries.spec.ts`.
