# Personal Financial Ledger (PFL)

A production-quality Personal Financial Ledger (PFL) built using modern AI-assisted software engineering practices.

The project is designed to be stable, maintainable, and extensible while remaining simple enough for daily personal use.

---

# Project Goals

* Record personal income and expenses
* Produce accurate financial reports
* Support Telegram as the primary user interface
* Store data in Google Sheets
* Automate workflows with Google Apps Script
* Maintain production-quality engineering standards

---

# Technology Stack

* Google Sheets
* Google Apps Script
* Telegram Bot API
* JavaScript
* GitHub
* AI Engineering OS (AI-EOS)

---

# Repository Structure

```text
.
├── .github/                 GitHub workflows and templates
├── archive/                 Historical planning artifacts
│   └── planning-artifacts/
├── assets/                  Images and static resources
├── docs/                    Project documentation
├── scripts/                 Development and utility scripts
├── src/                     Source code
├── test/                    Tests
├── LICENSE
├── README.md
├── START_HERE.md
└── package.json
```

---

# Documentation

| Document                    | Purpose                                                |
| --------------------------- | ------------------------------------------------------ |
| START_HERE.md               | Project entry point                                    |
| docs/                       | Functional and technical documentation                 |
| archive/planning-artifacts/ | Historical planning packages and engineering artifacts |

---

# Branch Strategy

* **main** — Stable production baseline
* **feature/*** — New functionality
* **fix/*** — Bug fixes
* **chore/*** — Repository maintenance and documentation

All development should begin from the latest `main` branch.

---

# Engineering Workflow

1. Create a feature or chore branch.
2. Implement one small production-ready task.
3. Validate the implementation.
4. Commit with a descriptive message.
5. Review before merging into `main`.

---

# Current Status

The repository has completed its initial engineering foundation.

Current focus:

* Repository cleanup and synchronization
* Expense transaction flow
* Google Sheets integration
* Telegram integration
* Production readiness

---

# Historical Artifacts

Earlier planning deliverables and engineering design packages have been preserved under:

```text
archive/planning-artifacts/
```

These files are retained for historical reference and are no longer considered the primary source of project documentation.

---

# License

This project is licensed under the MIT License.
