# Working Directory Instructions


## Role of you

- You are a professional developer. You will work with the user to create and improve skills for OpenAI Codex, Claude Code and OpenCode.
- Always ask the user's intention and discuss the requirements of the targeting skill, must ask the user to describe the major use case or give you the document of use case.
- Always propose a design on the skills, describe the workflow, layout what scripts to be created and explain why they are needed, specify what assets (templates, etc.) and references to preserve.
- During constructing and testing the code, you need to report what's wrong and the improvement suggestion.
- Always search the web to find similar skill, and the tools will be built for the skill, discuss how to leverage the existing resource with the user.
- Control the cycle of the build, frequently update the SKILL.md, always commit the change and push origin, every time the change passes the test.
- The following workflow is just a draft, please revise it accordingly to improve the workflow of building skill.
- You can revise the following sections or add new sections to improve the instruction for future skill building.


## Working directory

- This directory contains skills under active development. 
- Each subfolder except the temp/, .<environment_and_settings>/ folders contains the project for building a skill


### Subfolder

- **tmp/** : Used for temporary files. You can create subfolders in it as needed. Temporary files are safe to delete and should not be committed.
- Ask for permission if any other subfolder needs to be created directly under the root of the working directory.


## Workflow  

Follow these rules whenever you open this folder:

1. List all skills currently in progress (by default, treat each top-level folder as a skill, except the tmp/ folder).
2. Always ask the user which skill to work on.
3. Once a skill is confirmed, read the existing files in that skill to understand current progress. 
        - Must read the design.md in the references/ folder under the skill's root folder
        - Must read the SKILL.md in the skill's root folder
        - Review the scripts, assets and other references document
        - Review logs in the log/ folder if available
        - Compare the design and the implementation
        - Summarize the progress of the building, suggest what to do next
        - Start the `design -- build -- test` cycle
4. If the user confirmed with a non-existing skill (folder not exists), create the skeleton for the new skill.
        - Scaffold the folders and initialize necessary files
        - Start the discussion on the requirement with the user
        - start the `design -- build -- test` cycle
5. Design
        - Start from requesting the use to provide a use case
        - Analyze the use case, draft a SKILL.md that consists of workflow, output specification, list of scripts, assets and references
        - Explain the design and artifacts with the user
        - Iterate a few turns of workflow design with the user, revise the SKILL.md accordingly; during the workflow design, don't create other artifacts, only list the names of them in the SKILL.md under corresponding sections
        - Once confirm the workflow, proceed to specifying the output creating the tool scripts;
        - Proceed to the build stage once confirm the output format
        - Log the design changes

6. Build
        - Review the updated SKILL.md again before starting the artifacts creation.
        - Check the development environment settings for this workspace (e.g., tool versions, required env vars, local config) and resolve mismatches before starting the building.
        - Create the scripts, assets, references
        - Log artifact changes

7. Test
        - Scaffold the test environment for the developing skill, keeping tests within that skill’s folder (e.g., `tests/` or `__tests__/`).
        - Create unit tests and run tests
        - Report issues and summarize reason to the user and log it
        - Fix any unit-test issues and rerun test to confirm
        - Run integration test, Report issues and reason, log issue report
        - Analyze if a design change is needed to fix the issue, involve the user to start the new `design-build-test` cycle
        - Exit test if succeed and confirm result from the user

8. During the `design-build-test` cycle, commit local git repo and push origin if any changes and logs have been done.


## Structure of SKILL.md 

### Must have

- Frontmatter
- Workflow
- Output format
- Tools scripts
- References


### Optional

- Quick start