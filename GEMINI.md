# Project AI Assistant Rules

You are an AI assistant working on this project. Follow these rules:

## Project Awareness
- Always read project documentation before starting work
- Check for existing patterns in the examples/ folder
- Review any open issues or TODO items
- Understand the project's architecture and conventions

## Code Structure
- Keep files under 500 lines when possible
- Use clear, descriptive function and variable names
- Follow the established patterns in the examples/ folder
- Organize code into logical modules and packages
- Prefer composition over inheritance

## Code Quality
- Write unit tests for all new functions
- Use type hints in Python, TypeScript definitions in JS/TS
- Include docstrings for all public functions
- Handle errors gracefully with try/catch or try/except blocks
- Follow the DRY principle (Don't Repeat Yourself)

## Testing Requirements
- Run tests before submitting code
- Aim for >80% test coverage
- Use pytest for Python projects, Jest for JavaScript
- Mock external dependencies in tests
- Include both unit and integration tests
- Test error conditions and edge cases

## Documentation Standards
- Update README.md for new features
- Include usage examples in docstrings
- Document any environment variables needed
- Add comments for complex business logic only
- Keep comments up to date with code changes

## Style Conventions
- Use consistent formatting (prettier, black, etc.)
- Follow language-specific style guides (PEP 8, ESLint)
- Use meaningful commit messages
- Include type annotations where beneficial

## Communication
- Ask clarifying questions when requirements are unclear
- Explain your reasoning for architectural decisions
- Suggest improvements when you see opportunities
- Provide progress updates for long-running tasks

## Security Considerations
- Never commit sensitive data (API keys, passwords)
- Validate all user inputs
- Use secure defaults
- Follow security best practices for the technology stack

## Performance Guidelines
- Consider performance implications of design decisions
- Use appropriate data structures and algorithms
- Profile code when performance is critical
- Cache expensive operations when appropriate
