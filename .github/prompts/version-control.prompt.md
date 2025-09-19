# Version Control Workflow Prompt

## Overview

Manage the complete git workflow from changes detection to push, ensuring best practices and developer collaboration at each step.

## Workflow Instructions

### 1. **Initial Assessment & Status Check**

- Always start by checking current git status using `get_changed_files` tool or `git status`
- Identify modified, staged, and untracked files
- Present a clear summary of current repository state to the developer
- Ask developer to confirm which changes should be included in this commit

### 2. **Change Analysis & Review**

- Use `get_changed_files` tool to examine file diffs for staged/unstaged changes
- Provide a concise summary of changes per file:
  - **Added**: New files or functionality
  - **Modified**: Changed existing code (highlight key changes)
  - **Deleted**: Removed files or code sections
- Flag any potential issues (missing tests, breaking changes, etc.)
- Ask developer to review and approve the change summary

### 3. **Staging Strategy**

- Based on change analysis, suggest logical groupings for staging:
  - Related feature changes together
  - Bug fixes separately from features
  - Documentation updates as separate commits when substantial
- Use `git add` commands strategically (specific files vs. `git add .`)
- Confirm staging decisions with developer before proceeding

### 4. **Commit Message Generation**

- Follow conventional commit format: `<type>(<scope>): <description>`
- **Types**: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`, `ci`
- **Rules**:
  - Keep first line under 50 characters
  - Use imperative mood ("Add feature" not "Added feature")
  - Capitalize first letter
  - No period at end of first line
  - Blank line before detailed description (if needed)
- **Process**:
  1. Analyze changes to determine appropriate type and scope
  2. Generate 2-3 commit message options
  3. Present options to developer for selection/modification
  4. Include commit body for complex changes explaining WHY (not what)

### 5. **Commit Creation & Verification**

- Execute `git commit` with approved message
- Verify commit was created successfully
- Show commit hash and summary to developer
- Check if any pre-commit hooks were triggered and handle any failures

### 6. **Pre-Push Validation**

- Check current branch and confirm push destination
- Verify no sensitive information is being committed (API keys, passwords, etc.)
- Suggest running tests if test files exist in the project
- Ask developer to confirm push destination (origin, branch name)

### 7. **Push Execution**

- Execute `git push` to appropriate remote and branch
- Handle any push rejections (conflicts, force-push scenarios)
- Confirm successful push with remote commit URL if available
- Provide next steps or suggestions (create PR, merge, etc.)

## Integration Guidelines

### **Using MCP Servers**

- **Git MCP Server**: Use for advanced git operations, branch management, and conflict resolution
- **GitHub MCP Server**: Use for creating PRs, checking CI status, and repository interactions
- **Context7 MCP**: Reference git best practices and conventional commit documentation when needed

### **Developer Interaction Protocol**

- **Always ask before**: Staging files, committing, pushing
- **Provide options for**: Commit messages, staging strategies, branch operations
- **Confirm critical actions**: Force pushes, branch switches, merge operations
- **Explain decisions**: Why certain commit types/scopes were chosen

### **Error Handling**

- **Merge conflicts**: Guide developer through resolution process
- **Push rejections**: Explain cause and provide resolution options
- **Hook failures**: Help debug and fix pre-commit/pre-push hook issues
- **Authentication**: Assist with credential and permission issues

## Best Practices Enforcement

### **Commit Quality**

- ✅ Single responsibility commits
- ✅ Descriptive but concise messages
- ✅ Proper conventional commit format
- ❌ "WIP", "temp", or "test" commits in main branches
- ❌ Commits mixing unrelated changes

### **Security Checks**

- Scan for common secrets patterns before committing
- Warn about large file additions (>10MB)
- Check for TODO/FIXME comments that should be addressed
- Verify .gitignore is properly excluding build artifacts

### **Workflow Optimization**

- Suggest rebasing for cleaner history when appropriate
- Recommend feature branches for substantial changes
- Advise on when to squash commits before merging
- Guide on proper tag usage for releases

## Response Format Requirements

- Structure responses with clear workflow step headings
- Use ✅ for confirmed actions and ❌ for issues requiring attention
- Provide command examples with explanations
- Include "Next Steps" section after each major operation
- Ask specific questions rather than generic "Is this OK?"

## Example Interaction Flow

```
🔍 **Status Check**: Found 3 modified files, 1 new file
📋 **Change Summary**:
  - ✅ src/auth.py: Added login validation (47 lines)
  - ✅ tests/test_auth.py: New test file (23 lines)
  - ❌ config.py: Contains potential secret on line 15

❓ **Developer Decision**: Should we stage auth changes separately from config changes?

💡 **Commit Message Options**:
  1. `feat(auth): add user login validation with tests`
  2. `feat: implement user authentication system`
  3. `add: login validation feature`

🚀 **Ready to Push**: Commit abc123d created successfully. Push to origin/main?
```
