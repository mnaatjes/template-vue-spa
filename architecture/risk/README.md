# Risk Register: template-vue-spa

Master risk register evaluating architectural, technical, and operational risks according to Boehm-UP risk exposure ($RE = P \times I$).

| Risk ID | Description | Probability ($P$) | Impact ($I$) | $RE$ | Mitigation Strategy |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `RSK-01` | Downstream apps break layer boundaries (e.g. shared imports entity). | 0.6 | 0.8 | **0.48** | Enforce via `eslint-plugin-boundaries` in CI and Vitest boundary test suite. |
| `RSK-02` | Copier updates overwrite downstream custom business logic. | 0.3 | 0.7 | **0.21** | Restrict copier payload to boilerplate plumbing, using clear exclusion and answer patterns. |
| `RSK-03` | API payload shape mismatches runtime TypeScript expectations. | 0.5 | 0.8 | **0.40** | Enforce Zod schema validation on all incoming API responses in `shared/api/`. |
| `RSK-04` | Node.js / pnpm toolchain version drift across developer environments. | 0.4 | 0.6 | **0.24** | Standardize containerized Docker builds and lockfile reproducibility. |
