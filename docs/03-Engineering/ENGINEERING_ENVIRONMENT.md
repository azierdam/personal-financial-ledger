# Engineering Environment

This document defines the development, sandbox, and production environments for the PFL project.

## 1. Local Sandbox Environment
- **Purpose**: Rapid development, local testing, and validation of logic without Google Cloud dependencies.
- **Tooling**: `gas-fakes`, `npm`.
- **Workflow**: 
  - `npm install`
  - `npm run test` (executes tests against local fakes)

## 2. Apps Script Development Environment
- **Purpose**: Integration testing, debugging, and iterative deployment.
- **Tooling**: `clasp`, Google Apps Script IDE.
- **Workflow**:
  - `npm run push` (pushes code to a development script project)
  - Verify in the Apps Script online IDE.

## 3. Production Environment
- **Purpose**: Stable, user-facing application.
- **Tooling**: `clasp` (production deployment).
- **Workflow**:
  - `npm run deploy` (deploys versioned code to production script project).

## Environment Validation
- Run `npm run doctor` to ensure all tools (`node`, `clasp`) are installed and configured correctly.
