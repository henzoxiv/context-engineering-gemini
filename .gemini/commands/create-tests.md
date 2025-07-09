# Create Tests Command

Generate comprehensive test suites for specified code components.

## Process:
1. **Code Analysis**: Understand the component structure and dependencies
2. **Test Strategy**: Determine appropriate testing approaches (unit, integration, e2e)
3. **Mock Setup**: Create necessary mocks and test data
4. **Edge Cases**: Identify and test edge cases and error conditions
5. **Coverage**: Ensure comprehensive test coverage

## Test Types Generated:
- Unit tests for individual functions/methods
- Integration tests for component interactions
- Contract tests for API endpoints
- Property-based tests for complex logic
- Performance tests for critical paths

## Usage:
```bash
/create-tests path/to/component.js
/create-tests --type=integration src/api/
/create-tests --coverage=90 src/utils/
```

## Output:
- Complete test files with proper structure
- Test data fixtures and mocks
- Test configuration and setup
- Coverage reports and metrics
