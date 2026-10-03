# Workflow Observation
## Trigger
Use this workflow when there is a Pull Request (PR) or set of changes that will go to human review and it is necessary to check, before the review, if the change has sufficient traceability, implementation, testing and evidence. 

The workflow must be read-only with respect to the GitHub review process: it must not post comments, approve, request changes, merge, or modify the reviewed PR.

## Inputs
- Pull Request ID and repository.
- Base branch and branch/head of the change.
- PR description and metadata.
- REQUIREMENTS.md, if available.
- SPEC.md, if available.
- ARCHITECTURE.md or equivalent, if available.
- TASKS.md, if available.
- Traceability matrix, if available.
- Modified files and PR diff.
- Code related to the changes.
- Relevant tests.
- Available evidence of test execution/CI.

## Steps Performed
1. Select PR #1 and review its metadata: status, branches, commits, and description.
2. Get the list of modified files and review the diff.
3. Read REQUIREMENTS.md, SPEC.md, ARCHITECTURE.md, TASKS.md, and docs/traceability.md to establish the change context.
4. Review the modified files directly: REQUIREMENTS.md and tests/test_setup.py.
5. Inspect the related implementation in src/customer_search/ and the existing tests in tests/.
6. Check the traceability: Requirement → Acceptance Criteria → Task → Implementation → Test.
7. Look for evidence of test execution using the commit status and GitHub workflow runs.
8. Run the suite locally for evidence of the test run.
9. Classify the findings by severity and prepare a report for human review.

## Decisions
- Determine which documentation was relevant to the change and expand the review from the two modified files to include SPEC, architecture, tasks, traceability, implementation, and related tests.
- Determine if each new requirement was fully covered and distinguish between existing functional coverage and explicit document traceability.
- Identify that FR-07 conceptually overlaps with FR-02/FR-03 and that their combined behavior already appears in SR-03, but is not explicitly incorporated into the traceability of the new requirement.
- Identify that FR-08 has behavior related to the order of encounter and a test exists for it, but the new requirement is not explicitly traced to SPEC/AC/Task/Test.
- Identify that FR-09 introduces character/format validation that is neither implemented nor tested.
- Determine that changing tests/test_setup.py from version 0.1.0 to 0.2.0, while src/customer_search/__init__.py continues to declare 0.1.0, constitutes a verifiable fault and requires correction before considering the PR ready.

## Deterministic Work
- Retrieve PR metadata.
- List modified files.
- Get the diff.
- Automatically detect the presence of REQUIREMENTS.md, SPEC.md, ARCHITECTURE.md/ARQUITECTURE.md, TASKS.md, and docs/traceability.md.
- Locate tests related to the modified files or requirements.
- Run pytest -v or the project-defined command.
- Get CI/check statuses when available.
- Find references to IDs such as FR-01, AC-01, T-01, and test names.
- Compare the declared package version with the version expected by the tests.
- Generate a report structure with findings and evidence sections.

## Reference Knowledge
- REQUIREMENTS.md: Functional and non-functional requirements, open questions, and constraints.
- SPEC.md: Search rules, validation, error handling, acceptance criteria, and test scenarios.
- ARCHITECTURE.md: Responsibilities by layer and testing strategy.
- TASKS.md: Relationship between tasks, files, acceptance criteria, and verifications.
- docs/traceability.md: Existing matrix of Requirement → SPEC/AC → Task → Files → Test → Status.
- tests/test_setup.py, tests/test_cli.py, tests/test_service.py, and tests/test_storage.py: Existing evidence and automated coverage.
- The PR diff as the primary source to define what actually changed.

## Output
The artifact produced by this workflow is a structured report for human review that contains:
- Scope and context of the PR.
- Documentation consulted.
- Files and changes inspected.
- Relevant tests.
- Evidence of execution available or missing.
- Findings classified as MUST FIX, SHOULD FIX, or OPTIONAL.
- Limitations of the evidence.
- Pending human decision on the review of the PR.

## Stop Conditions
Stop the workflow and request human intervention when:
- It's not possible to determine which change is being reviewed or what the correct commit/header is.
- Necessary requirements/specs are missing to evaluate a claim that depends on them, and there is no other verifiable source.
- There is a discrepancy that could have multiple interpretations and affect the conclusion.
- Tests cannot be run, and there is no reliable CI evidence; the report should mark the evidence as incomplete instead of assuming success.
- A MUST FIX is detected that prevents the change from being considered ready for human review.
- The review requires modifying code, tests, or documentation to resolve a finding.
- It is necessary to comment on GitHub, approve, request changes, change the PR status, or merge.