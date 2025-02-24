# Development Environment Setup Guide

Step-by-step guide to set up your Python development environment on Windows.

## Quick Start Installation Steps

### 1. Install Miniconda
1. Download [Miniconda for Windows](https://docs.conda.io/en/latest/miniconda.html)
2. Double-click the `.exe` file
3. Follow installer prompts (Important: Check "Add Miniconda to PATH")
4. Verify in Command Prompt:
   ```bash
   conda --version
   ```

### 2. Install Visual Studio Code
1. Open Microsoft Store
2. Search for "Visual Studio Code"
3. Click "Get" or "Install"
4. Launch VS Code after installation

### 3. Install VS Code Extensions
1. Open VS Code
2. Press `Ctrl + Shift + X` for Extensions panel
3. Search and install:
   - Python
   - Python Indent
   - Jupyter

### 4. Setup GitHub Copilot
1. Go to [GitHub Student Developer Pack](https://education.github.com/pack)
2. Sign up with your academic email
3. In VS Code:
   - Press `Ctrl + Shift + X`
   - Search "GitHub Copilot"
   - Install the extension
   - Sign in when prompted

### Basic Conda Commands to Get Started
```bash
# Create a new project environment
conda create --name myproject python=3.9

# Activate your environment
conda activate myproject

# Install common packages
conda install pandas numpy matplotlib
```

## Understanding the Tools

### What is Miniconda?
Miniconda is like a toolbox manager for Python. Imagine you're working on different art projects:
- One needs watercolors
- Another needs oil paints
- They shouldn't mix

Miniconda helps you:
- Create separate "toolboxes" (environments) for different projects
- Install only the tools (packages) you need
- Switch between different Python versions easily
- Keep your computer clean and organized

### What is an IDE (VS Code)?
An IDE (Integrated Development Environment) is like a super-powered notepad for coding. VS Code is Microsoft's free IDE that:
- Highlights code to make it readable
- Catches errors as you type
- Suggests completions
- Helps debug your code

Why VS Code?
- Free and fast
- Works with many programming languages
- Huge library of extensions
- Regular updates
- Large community support

### What are VS Code Extensions?
Extensions are add-ons that give VS Code new abilities, like:
- Python extension: Adds Python support
- Jupyter: Lets you work with Jupyter notebooks
- GitHub Copilot: AI-powered coding assistant
- Python Indent: Better code formatting

Think of them like apps on your phone - they add new features to make your work easier.

## Troubleshooting Common Issues

### Miniconda Issues
- If `conda` command not found: Restart Command Prompt
- If environments don't show up: Check PATH in System Environment Variables

### VS Code Issues
- If Python extension doesn't work: Check Python installation path
- If Copilot doesn't activate: Verify GitHub student status

## Need Help?
- Miniconda docs: [Link](https://docs.conda.io/)
- VS Code docs: [Link](https://code.visualstudio.com/docs)
- GitHub Student Pack: [Link](https://education.github.com/pack)
```
