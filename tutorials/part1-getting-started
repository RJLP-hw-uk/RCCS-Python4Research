# Part 1: Getting Started with Python on VS Code

## What is Miniconda and Why Use Environment Managers?

### Understanding Package Management

Miniconda is a free minimal installer for conda, a powerful package, dependency, and environment manager. Think of it as a way to create isolated workspaces for your Python projects.

> **Personal Experience**: When I first started using Python, I installed packages directly on my system. Eventually, I ended up with conflicting dependencies between projects - one needed TensorFlow 1.x while another required 2.x. After wasting hours debugging these conflicts, I discovered conda environments. Now, each project has its own environment with precisely the packages it needs, at the exact versions required. This approach has saved me countless hours of troubleshooting.

### Why Environment Management Matters

Environment management helps you:
- Maintain reproducible research
- Share your exact setup with colleagues
- Avoid "it works on my machine" problems
- Manage projects with conflicting dependencies

## Setting Up Miniconda

1. Download Miniconda from the [official website](https://docs.conda.io/en/latest/miniconda.html)
2. Run the installer and follow the prompts
3. Open the Anaconda Prompt (or terminal on Mac/Linux)

## Understanding Conda Environments

Think of conda environments like separate folders in Windows Explorer. Just as you might have different folders for different projects, conda environments let you have separate "folders" for different Python setups.

In Windows Explorer, if you keep all your files in one folder, things get messy and hard to find. Similarly, if you install all Python packages in one environment, they can conflict with each other.

### Creating Your First Environment

Open Anaconda Prompt and run:
```bash
conda create --name research-env python=3.9
This creates a new environment called "research-env" with Python 3.9 installed.

To activate this environment:
```bash
conda activate research-env
Your prompt should change to show the active environment.

Installing Essential Packages
Now let's install the core packages for scientific computing:
```bash
conda install numpy pandas scipy matplotlib

What These Packages Do:
NumPy: Provides support for large, multi-dimensional arrays and matrices, along with mathematical functions to operate on these elements. It's the foundation for scientific computing in Python.
Pandas: Offers data structures and operations for manipulating numerical tables and time series. Think of it as "Excel for Python" but much more powerful.
SciPy: Builds on NumPy with additional functionality for optimization, signal processing, statistics, and more.
Matplotlib: The standard plotting library for creating static, animated, and interactive visualizations.

Alternatives Worth Knowing:

For NumPy: There aren't many direct alternatives, as it's the foundation most other packages build upon.
For Pandas: Polars is a faster alternative for large datasets, and Dask extends pandas for parallel computing.
For SciPy: scikit-learn for machine learning, statsmodels for statistical models.
For Matplotlib: Seaborn provides a higher-level interface, Plotly offers interactive plots, and Bokeh is great for web-based visualizations.

Setting Up VS Code
What is an IDE?
An Integrated Development Environment (IDE) combines a code editor, debugger, and other tools in one application. While you can write Python code in any text editor, IDEs provide features that make development easier and more efficient.
Installing VS Code
VS Code can be installed through the software center on our organization's computers. Simply search for "Visual Studio Code" and click install.
Why VS Code?
We're using VS Code for several reasons:

GitHub Copilot Access: VS Code allows seamless integration with GitHub Copilot, which is free for academic use. This AI assistant can dramatically speed up your coding by suggesting code completions.
Extensibility: VS Code has a massive marketplace of extensions.
Lightweight but Powerful: Unlike some IDEs, VS Code starts up quickly and runs smoothly while still offering powerful features.

While you could use other environments like PyCharm, Spyder, or Jupyter, VS Code offers the best combination of features for our research needs. That said, the skills you learn will transfer to other environments if you prefer them.
Navigating VS Code
When you first open VS Code, you'll see a welcome screen. Here are the key areas to be familiar with:

Activity Bar: The leftmost column with icons for different views
Side Bar: Opens when you click an Activity Bar icon, showing files, extensions, etc.
Editor: The main area where you'll write code
Status Bar: At the bottom, showing information about your project

Essential Extensions

Click the Extensions icon in the Activity Bar (or press Ctrl+Shift+X)
Search for and install the "Python" extension package from Microsoft

This package includes:

Python language support
Debugging
Linting (code quality checks)
IntelliSense (code completions)
Jupyter Notebook support

Other useful extensions:

"Rainbow CSV" for better CSV file viewing
"Excel Viewer" for viewing Excel files
"GitHub Copilot" for AI-assisted coding

Connecting VS Code to Your Conda Environment

Open VS Code
Open the Command Palette (Ctrl+Shift+P)
Type "Python: Select Interpreter" and select it
Choose your "research-env" environment from the list

You should now see the environment name in the status bar. VS Code will use this environment when running Python code.
To verify everything is working:

Create a new file (Ctrl+N)
Save it as "test.py" (Ctrl+S)
Add this code:
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("NumPy version:", np.__version__)
print("Pandas version:", pd.__version__)
print("Everything is working!")

Run the file by clicking the play button in the top right or right-clicking and selecting "Run Python File in Terminal"

If you see version information and "Everything is working!" without errors, congratulations! Your Python environment is set up correctly.
Next Steps
Now that you have your environment set up, proceed to Part 2: Data Extraction and Processing to learn how to work with data files.
