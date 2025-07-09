## FEATURE:
Create a CLI tool that analyzes Python codebases and generates a comprehensive report including:
- Lines of code statistics (total, comments, blank lines)
- Function complexity metrics using cyclomatic complexity
- Import dependency graph visualization
- Test coverage analysis integration
- Code quality scores using pylint and flake8
- Duplicate code detection

The tool should accept a directory path and output results in multiple formats (JSON, CSV, HTML report).
Include a progress bar for large codebases and support for excluding specific directories/files.

## EXAMPLES:
- `examples/cli.py` - Shows argument parsing patterns using Click and output formatting
- `examples/analysis/complexity.py` - Contains example complexity analysis implementation
- `examples/analysis/dependencies.py` - Shows how to parse and analyze imports
- `examples/tests/test_analyzer.py` - Shows testing patterns for analysis tools with mocking
- `examples/reports/` - Contains example report templates and formatting

## DOCUMENTATION:
- https://docs.python.org/3/library/ast.html - For AST parsing and code analysis
- https://pylint.pycqa.org/en/latest/ - For code quality analysis integration
- https://click.palletsprojects.com/ - For CLI framework and argument handling
- https://networkx.org/ - For dependency graph creation and analysis
- https://coverage.readthedocs.io/ - For test coverage integration

## OTHER CONSIDERATIONS:
- Handle large codebases efficiently (>10,000 files) with streaming analysis
- Gracefully handle syntax errors in analyzed files without stopping analysis
- Support both Python 2 and 3 syntax analysis (configurable)
- Include progress bars for long-running analysis operations
- Cache analysis results to avoid re-analyzing unchanged files
- Memory-efficient processing for very large codebases
- Support for custom exclude patterns (.gitignore style)
- Configurable complexity thresholds and quality gates
- Integration with CI/CD pipelines through exit codes
