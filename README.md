# template-vue-spa

A standardized [Copier](https://copier.readthedocs.io/) template generator for production-ready Vue 3 Single Page Applications (SPAs) built with Vite, TypeScript, and Pinia, strictly enforcing [Feature-Sliced Design (FSD)](https://feature-sliced.design/) architectural boundaries.

## Architecture & Governance

This generator adheres to the Homelab Systems Lifecycle (HSL) and Unified Process (UP) disciplines. Internal engineering documentation resides under [`architecture/`](architecture/):

* [`architecture/adr/0001_initial_template_architecture.md`](architecture/adr/0001_initial_template_architecture.md): Generator pattern selection and architectural decoupling.
* Invariant enforcement matrices spanning AST linting (`eslint-plugin-boundaries`), architectural test suites (`vitest`), pre-commit hooks, and CI gates.

## Downstream Stack & Tooling

Downstream SPAs scaffolded by this generator include:

* **Framework:** Vue 3 Composition API with `<script setup lang="ts">`.
* **Build Tool:** Vite with fast HMR and environment proxying.
* **State Management:** Pinia stores structured per domain entity.
* **Typing & Validation:** TypeScript (strict mode) and Zod schema contracts for all API interactions.
* **Testing:** Vitest for component unit tests and architectural boundary compliance.
* **Packaging:** Multi-stage `Dockerfile` (Node build -> Nginx Alpine with non-root security context).
* **AI Assistance Rules:** `.gemini/rules/frontend_fsd_invariants.md` codifying Feature-Sliced Design invariants.

## Usage

Scaffold a new frontend application:

```bash
copier copy gh:mnaatjes/template-vue-spa path/to/target-ui
```

Update an existing application with new template releases:

```bash
cd path/to/target-ui
copier update
```

## Template Development & Verification

Install development dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

Run template generation tests:

```bash
pytest -v
```
