# Context Validation System

Validates the quality and completeness of context provided to Gemini CLI.

## Validation Checks:

### 1. Context Completeness
- [ ] GEMINI.md exists and is comprehensive
- [ ] Examples folder has relevant patterns
- [ ] Documentation links are valid
- [ ] PRP templates are complete

### 2. Example Quality
- [ ] Examples follow established patterns
- [ ] Code examples are runnable
- [ ] Examples cover common scenarios
- [ ] Test examples demonstrate best practices

### 3. Documentation Quality
- [ ] README is comprehensive and up-to-date
- [ ] API documentation is complete
- [ ] Setup instructions are clear
- [ ] Troubleshooting guide exists

### 4. Project Structure
- [ ] Folder structure follows conventions
- [ ] File naming is consistent
- [ ] Dependencies are properly managed
- [ ] Configuration files are complete

## Usage:
```bash
/validate-context
```

## Scoring System:
- **90-100**: Excellent context, optimal for AI assistance
- **80-89**: Good context, minor improvements needed
- **70-79**: Adequate context, some gaps present
- **60-69**: Poor context, significant improvements required
- **<60**: Inadequate context, major overhaul needed

## Improvement Suggestions:
The validator provides specific, actionable recommendations for improving context quality.
