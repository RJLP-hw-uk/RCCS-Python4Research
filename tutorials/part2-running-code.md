# <span style="color:#9575CD">Part 2: Running Python Code in VS Code</span>

## Table of Contents
- [Running Python Scripts](#running-python-scripts)
- [Working with the Interactive Window](#working-with-the-interactive-window)
- [Debugging Basics](#debugging-basics)
- [Advanced Debugging with launch.json](#advanced-debugging-with-launchjson)
- [Best Practices](#best-practices)
- [Next Steps](#next-steps)

## <span style="color:#689F38">Running Python Scripts</span>

## <span style="color:#03A9F4">Overview of Code Execution Options</span>

VS Code offers multiple ways to run Python code, each suited for different scenarios:

![VS Code Run Options](/resources/images/run-options.png)

Table of common run options:

| Option | Description | Best For |
|--------|-------------|----------|
| Run Python File | Executes entire script in integrated terminal | Quick script execution |
| Run in Terminal | Executes script in dedicated terminal | Command-line arguments |
| Run in Interactive | Opens Interactive Window | Data analysis and exploration |
| Debug Python File | Starts basic debugger | Finding and fixing errors |
| Run with Config | Launches with custom debug settings | Complex debugging scenarios |



### Key Considerations (Beginner-Friendly)
For starting with Python in research:
1. Interactive Window for data exploration - great for learning and immediate feedback
2. Debug Mode for understanding code flow step by step
3. Terminal for simple script execution and basic command-line usage

### Limitations (Advanced Users)
When pushing the limits of VS Code's capabilities:
- Memory intensive: Interactive Windows and Notebooks can be resource-heavy
- Performance bottlenecks: Not optimal for complex numerical simulations
- Computational limits: May struggle with intensive research computations
- Debugging challenges: Complex class hierarchies and object relationships
- Visualization constraints: Limited tools for advanced data structure inspection

> **Note:** These limitations mainly affect advanced research computing scenarios. For typical data analysis and exploratory tasks, interactive development tools like Interactive Window and Jupyter Notebooks provide excellent functionality.

### Important Note on Debugging

Debugging is essential for both interactive and script-based development. We will cover this later.

## <span style="color:#689F38">Working with the Interactive Window</span>

### <span style="color:#03A9F4">The Jupyter Experience in VS Code</span>

VS Code provides a powerful interactive coding experience similar to Jupyter Notebooks:

1. Open your Python file
2. Select a code block or the entire file
3. Right-click and select "Run Current File in Interactive Window" or use the keyboard shortcut (Shift+Enter)

![Interactive Window](/resources/images/interactive_window.png)
![Interactive Window](/resources/images/interactive_window2.png)

The Interactive Window provides:
- Cell-by-cell execution
- Rich output display (plots, tables, etc.)
- Variable inspection
- IntelliSense and code completion

### <span style="color:#03A9F4">Using Cell Comments for Code Organization</span>

You can define code cells in regular Python files using special comments:

```python
# %% This is a cell heading
import numpy as np
import pandas as pd

# %% Data preparation
data = pd.read_csv('data.csv')
data.head()

# %% Data visualization
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
plt.plot(data['x'], data['y'])
plt.title('My Research Data')
plt.show()
```

Each `# %%` comment marks the start of a new cell. You can run individual cells by clicking the "Run Cell" button that appears above each cell or using Shift+Enter when your cursor is in a cell.

This approach combines the best of both worlds: regular Python files and Jupyter-like interactivity.

### <span style="color:#03A9F4">Working with Jupyter Notebooks (.ipynb)</span>

VS Code provides excellent support for Jupyter Notebooks:

1. **Create a new notebook**:
    - Use Command Palette (Ctrl+Shift+P)
    - Type "Create New Jupyter Notebook"
    - Or right-click in Explorer and select "New Jupyter Notebook"

2. **Basic notebook structure**:
```python
# Code cell
import pandas as pd
data = pd.read_csv('experiment.csv')

# Markdown cell for documentation
## Analysis Steps
1. Load data
2. Clean outliers
3. Plot results
```

### <span style="color:#03A9F4">Research Workflow with Notebooks</span>

Here's a practical example to get started:

```python
# %% 1. Introduction and Setup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %% 2. Generate Sample Research Data
# Simulating temperature readings over time
np.random.seed(42)
dates = pd.date_range('2023-01-01', '2023-01-31')
temps = np.random.normal(20, 5, len(dates))
data = pd.DataFrame({'date': dates, 'temperature': temps})

# %% 3. Basic Analysis
print("Summary Statistics:")
print(data.describe())

# %% 4. Visualization
plt.figure(figsize=(10, 6))
plt.plot(data['date'], data['temperature'])
plt.title('Temperature Variations')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

# %% 5. Save Results
data.to_csv('temperature_data.csv', index=False)
```

Try running each cell individually using Shift+Enter. Observe how the Interactive Window displays both code output and visualizations.

### <span style="color:#03A9F4">Converting Between .py and .ipynb</span>

VS Code allows you to:
- Export notebooks to Python scripts
- Convert Python scripts with cell markers to notebooks
- Share notebooks with colleagues via GitHub or email

## <span style="color:#689F38">Debugging Basics</span>

### <span style="color:#03A9F4">Why Debugging Matters</span>

Debugging is the process of finding and fixing errors in your code. VS Code provides powerful tools to help you:
- Understand what your code is doing step-by-step
- Examine variable values at different points in execution
- Identify where and why errors occur

### <span style="color:#03A9F4">Basic Debugging Steps</span>

1. **Set breakpoints** by clicking in the gutter (space to the left of your code line numbers)
2. Start debugging by:
    - Clicking the debug icon in the activity bar, then the play button
    - Or pressing F5
    - Or selecting "Start Debugging" from the Run menu

![Setting Breakpoints](/resources/images/setting-breakpoints.png)

3. **Control execution** with the debug toolbar that appears:
    - Continue (F5): Run until the next breakpoint
    - Step Over (F10): Execute the current line and stop at the next line
    - Step Into (F11): Enter a function call to debug its internal code
    - Step Out (Shift+F11): Complete the current function and return to the caller
    - Restart (Ctrl+Shift+F5): Restart the debugging session
    - Stop (Shift+F5): End debugging

4. **Inspect variables** in the variables pane that appears during debugging

![Debug Controls](/resources/images/debug-controls.png)

### <span style="color:#03A9F4">Using the Debug Console</span>

During debugging, you can interact with your code using the Debug Console:
1. While at a breakpoint, find the Debug Console tab at the bottom of VS Code
2. Type expressions to evaluate them in the current context
3. This allows you to test hypotheses about your code's behavior

For example, if you're stopped at a breakpoint inside a function, you can check variable values or test calculations without modifying your actual code.

## <span style="color:#689F38">Advanced Debugging with launch.json</span>

### <span style="color:#03A9F4">Creating a launch.json File</span>

For more control over debugging, you can create a `launch.json` file:

1. Click the "Run and Debug" icon in the Activity Bar
2. Click "create a launch.json file" or the gear icon
3. Select "Python" from the environment options

VS Code will create a `.vscode` folder in your project with a `launch.json` file containing basic Python debugging configuration.

### <span style="color:#03A9F4">Customizing Your Debug Configuration</span>

Here's an example of a
