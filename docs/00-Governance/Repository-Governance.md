# Repository Governance

Version: 0.1
Status: Active
Owner: Product Engineering

---

# Purpose

This document defines how the Personal Financial Ledger (PFL) GitHub repository is managed.

The objective is to maintain a clean, predictable, and AI-friendly engineering repository that supports long-term maintainability.

---

# Source of Truth

## Business Knowledge

Primary Source:

- Notion AKB (Authoritative Knowledge Base)

Contains:

- Product Vision
- PRD
- Business Rules
- Architecture Decisions
- Roadmap
- Functional Requirements
- Non-functional Requirements

GitHub MUST NOT duplicate this information.

---

## Engineering Execution

Primary Source:

GitHub Repository

Contains:

- Issues
- Pull Requests
- Source Code
- Engineering Documentation
- ADRs
- Technical Design
- Releases

GitHub represents executable engineering work.

---

# Repository Principles

The repository follows these principles:

- Simplicity over complexity
- Maintainability over cleverness
- Small incremental changes
- Reusable architecture
- AI-friendly structure
- Documentation close to implementation
- One source of truth for each type of information

---

# Issue Hierarchy

The backlog uses the following hierarchy.

Epic

↓

Feature

↓

Story

↓

Task

↓

Bug / Chore

Definitions

Epic
Large business objective.

Feature
Deliverable capability.

Story
User-focused implementation objective.

Task
Concrete engineering work.

Bug
Defect correction.

Chore
Maintenance or repository work.

---

# Issue Requirements

Every issue should contain:

- Objective
- Business Value
- Scope
- Dependencies
- Acceptance Criteria
- Priority
- Milestone
- Labels
- Estimated Size

No issue should be created without these fields.

---

# Naming Convention

Use concise titles.

Examples

feat(transaction): Record expense

feat(report): Monthly summary

task(sheet): Create transaction repository

bug(balance): Incorrect running balance

chore(github): Update issue templates

Avoid generic names such as:

- Update code
- Fix issue
- Improve system

---

# Labels

## Type

type/epic
type/feature
type/story
type/task
type/bug
type/chore

---

## Priority

priority/p0
priority/p1
priority/p2
priority/p3

---

## Status

status/backlog
status/ready
status/in-progress
status/review
status/testing
status/done
status/blocked
status/duplicate
status/obsolete

---

## Phase

phase/foundation
phase/mvp
phase/v1
phase/v2

---

## Component

component/apps-script
component/sheets
component/telegram
component/github
component/notion
component/n8n
component/gemini
component/testing

---

## Area

area/domain
area/backend
area/frontend
area/reporting
area/security
area/deployment
area/documentation

---

## Size

size/xs
size/s
size/m
size/l
size/xl

---

# Milestones

Repository milestones are:

- MVP Foundation
- MVP Core Ledger
- MVP Transaction Flow
- MVP Reporting
- MVP AI Assistant
- Production Hardening
- Version 1.0

---

# Definition of Ready

An issue is Ready when:

- Scope is understood
- Dependencies are identified
- Acceptance criteria are complete
- Priority assigned
- Milestone assigned
- Labels assigned

---

# Definition of Done

An issue is Done when:

- Acceptance criteria satisfied
- Code committed
- Reviewed
- Tested
- Documentation updated (if required)
- Ready for merge

---

# Pull Request Rules

Every Pull Request must:

- Reference an Issue
- Explain the change
- Describe testing performed
- Be reviewed before merge

---

# Repository Workflow

AKB

↓

Architecture Review

↓

GitHub Issue

↓

Implementation

↓

Pull Request

↓

Review

↓

Merge

↓

Release

---

# Change Management

Major architectural decisions must be recorded as ADRs.

Repository governance changes should be discussed before adoption.

---

# Future Improvements

Future repository improvements include:

- AI-EOS backlog validation
- Automatic issue quality checking
- Automatic dependency analysis
- Sprint generation
- Release automation

These enhancements must not compromise repository simplicity.
