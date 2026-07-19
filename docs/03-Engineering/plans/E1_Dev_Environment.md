# Implementation Plan: Engineering Sprint E1 — Local Development & Sandbox Environment

## Objective
Establish a production-quality local development and sandbox environment for Google Apps Script using `clasp`, `gas-fakes`, and `npm` to enable automated, repeatable workflows, while ensuring all artifacts are maintained within the repository.

## Refined Scope
- **Environment Separation:** Clearly define and document three environments:
  - Local Sandbox (Fast, pure JS, mock data)
  - Apps Script Development (Fast deployment, linked to Google)
  - Production (Controlled, stable)
- **Tooling:**
  - `clasp`: Management and deployment.
  - `gas-fakes`: Local sandbox execution.
  - `npm`: Script orchestration.
- **Standards:**
  - No artifacts outside the repo.
  - Standardized npm scripts (`doctor`, `test`, `lint`, `push`, `deploy`).
  - `ENGINEERING_ENVIRONMENT.md` (renamed from previous plan).

## Implementation Steps

### 1. Repository Reorganization (Artifacts)
- Move existing implementation plans from temporary directory to `docs/03-Engineering/plans/`.
- Ensure all future review packages are created in `review/artifacts/` and `review/snapshots/` as requested.

### 2. Dependency & Script Configuration
- Update `package.json`:
  - Add `devDependencies` (`@google/clasp`, `gas-fakes`, etc.).
  - Standardize `scripts`:
    - `doctor`: Validate local environment.
    - `test`: Run local sandbox tests (`gas-fakes`).
    - `lint`: Static analysis.
    - `push`: `clasp push`.
    - `deploy`: `clasp deploy`.

### 3. Clasp Setup
- Configure `.clasp.json` (user authentication required).
- Create `.claspignore` (exclude docs, temp, and review files).

### 4. Sandbox Framework
- Integrate `gas-fakes` to run existing `test/` suites locally without deploying to Google.

### 5. Documentation
- Create `docs/03-Engineering/ENGINEERING_ENVIRONMENT.md` defining environments and workflows.

## Verification
- Validate `npm run doctor` passes.
- Run `npm run test` (local sandbox).
- Dry-run `clasp push`.
