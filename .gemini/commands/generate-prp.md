# Generate PRP Command

Read the feature request from $ARGUMENTS and create a comprehensive Product Requirements Prompt (PRP).

## Process:
1. **Analyze Request**: Parse the INITIAL.md file content thoroughly
2. **Research Codebase**: Look for similar patterns and implementations in examples/
3. **Gather Context**: Collect relevant documentation, APIs, and external resources
4. **Create PRP**: Generate a detailed implementation blueprint

## Research Steps:
- Read the entire codebase to understand existing patterns
- Identify similar implementations or related functionality
- Note coding conventions, testing patterns, and architectural decisions
- Gather relevant documentation from the feature request
- Search for best practices and common pitfalls

## Output Format:
Create a new file in PRPs/ directory with:
- Executive summary of the feature
- Complete technical requirements
- Step-by-step implementation plan
- Validation criteria and test requirements
- Success metrics and acceptance criteria
- Risk assessment and mitigation strategies

Use the template in PRPs/templates/prp_base.md as a starting point.

## Quality Check:
- Ensure all context is included
- Verify requirements are specific and measurable
- Include error handling and edge cases
- Add performance considerations
- Score confidence level (1-10) for implementation success
