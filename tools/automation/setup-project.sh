#!/bin/bash

# Auto-setup script for new Context Engineering projects

echo "🚀 Setting up Context Engineering project..."

# Install Gemini CLI if not present
if ! command -v gemini &> /dev/null; then
    echo "📦 Installing Gemini CLI..."
    npm install -g @google/gemini-cli
fi

# Authenticate with Google
echo "🔐 Setting up authentication..."
gemini auth login

# Create project structure
echo "📁 Creating project structure..."
mkdir -p .gemini/commands
mkdir -p examples/{patterns,architectures,integrations,testing}
mkdir -p workflows
mkdir -p docs

# Copy templates
echo "📋 Setting up templates..."
cp -r templates/* ./ 2>/dev/null || echo "No templates to copy"

# Initialize git if not already initialized
if [ ! -d ".git" ]; then
    echo "🔧 Initializing git repository..."
    git init
    git add .
    git commit -m "Initial commit: Context Engineering setup"
fi

# Run initial validation
echo "✅ Running initial validation..."
gemini /validate-context

echo "🎉 Setup complete! Your Context Engineering project is ready."
echo "Next steps:"
echo "1. Customize GEMINI.md with project-specific rules"
echo "2. Add relevant examples to examples/ folder"
echo "3. Create your first feature request in INITIAL.md"
echo "4. Run: gemini /generate-prp INITIAL.md"
