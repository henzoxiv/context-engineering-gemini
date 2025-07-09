# Context Engineering with Gemini CLI

A comprehensive template for getting started with Context Engineering - the discipline of engineering context for AI coding assistants so they have the information necessary to get the job done end to end.

Context Engineering is 10x better than prompt engineering and 100x better than vibe coding.

## Quick Start

```bash
# 1. Clone this template
git clone https://github.com/your-username/context-engineering-gemini.git
cd context-engineering-gemini

# 2. Set up your project rules (optional - template provided)
# Edit GEMINI.md to add your project-specific guidelines

# 3. Add examples (highly recommended)  
# Place relevant code examples in the examples/ folder

# 4. Create your initial feature request
# Edit INITIAL.md with your feature requirements

# 5. Generate a comprehensive PRP (Product Requirements Prompt)
# In Gemini CLI, run:
/generate-prp INITIAL.md

# 6. Execute the PRP to implement your feature
# In Gemini CLI, run:
/execute-prp PRPs/your-feature-name.md
```

## What is Context Engineering?

Context Engineering represents a paradigm shift from traditional prompt engineering:

**Prompt Engineering:**
- Focuses on clever wording and specific phrasing
- Limited to how you phrase a task
- Like giving someone a sticky note

**Context Engineering:**
- A complete system for providing comprehensive context
- Includes documentation, examples, rules, patterns, and validation
- Like writing a full screenplay with all the details

**Why Context Engineering Works:**
- **Reduces AI Failures**: Most agent failures aren't model failures - they're context failures
- **Ensures Consistency**: AI follows your project patterns and conventions
- **Enables Complex Features**: AI can handle multi-step implementations with proper context
- **Self-Correcting**: Validation loops allow AI to fix its own mistakes

## Template Structure

```
context-engineering-gemini/
├── .gemini/
│   ├── commands/
│   │   ├── generate-prp.md      # Generates comprehensive PRPs
│   │   └── execute-prp.md       # Executes PRPs to implement features
│   └── settings.json            # Gemini CLI configuration
├── PRPs/
│   ├── templates/
│   │   └── prp_base.md         # Base template for PRPs
│   └── EXAMPLE_multi_agent_prp.md # Example of a complete PRP
├── examples/                    # Your code examples (critical!)
├── GEMINI.md                   # Global rules for AI assistant
├── INITIAL.md                  # Template for feature requests
├── INITIAL_EXAMPLE.md          # Example feature request
└── README.md                   # This file
```

## Getting Started

1. **Install Gemini CLI**: Follow the [official installation guide](https://github.com/google-gemini/gemini-cli)
2. **Authenticate**: Use your Google account for free tier (60 requests/minute, 1000/day)
3. **Customize GEMINI.md**: Add your project-specific rules
4. **Add Examples**: Place relevant code patterns in examples/
5. **Create Feature Requests**: Use INITIAL.md template
6. **Generate PRPs**: Use `/generate-prp` command
7. **Execute PRPs**: Use `/execute-prp` command

## Key Features

- **Hierarchical Memory**: Uses GEMINI.md for persistent context
- **Custom Commands**: Slash commands for PRP workflow
- **Examples-Driven**: Rich examples folder for pattern recognition
- **Validation Loops**: Ensures working code through iteration
- **MCP Integration**: Supports Model Context Protocol servers

## Best Practices

- **Context is Everything**: Provide comprehensive, structured context
- **Show, Don't Tell**: Include examples of what to do and what not to do
- **Document Thoroughly**: Include API docs, gotchas, and requirements
- **Validate Continuously**: Use test-driven development with AI

---

*Based on the original context-engineering-intro by coleam00, adapted for Gemini CLI*
