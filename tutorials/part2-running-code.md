# <span style="color:#9575CD">Part 2: Running Python Code in VS Code</span>

## Table of Contents
- [Running Python Scripts](#running-python-scripts)
- [Working with the Interactive Window](#working-with-the-interactive-window)
- [Debugging Basics](#debugging-basics)
- [Advanced Debugging with launch.json](#advanced-debugging-with-launchjson)
- [Best Practices](#best-practices)
- [Next Steps](#next-steps)

## <span style="color:#689F38">Running Python Scripts</span>

### <span style="color:#03A9F4">Method 1: Simple Script Execution</span>

The most straightforward way to run Python code in VS Code is using the run button:

1. Open your Python file in the editor
2. Look for the ▶️ (play) button in the top-right corner of the editor window
3. Click the play button to execute your script

![Running a Python Script](/resources/images/run-python-script.png)

When you click the run button, VS Code will:
- Start a new terminal if one doesn't exist
- Execute your Python file using the selected Python interpreter
- Show the output directly in the terminal

This method is ideal for:
- Quick testing of script functionality
- Running simple scripts without debugging needs
- Getting immediate output from your code

### <span style="color:#03A9F4">Method 2: Running in a Dedicated Terminal</span>

You can also run Python files directly in the VS Code integrated terminal:

1. Open the terminal in VS Code (`View > Terminal` or `` Ctrl+` ``)
2. Navigate to your Python file's directory if needed
3. Run the file using the Python command:
    ```bash
    python your_file.py
    ```

Benefits of using a dedicated terminal:
- You maintain control over the execution environment
- You can pass command-line arguments to your script
- The terminal session persists, allowing you to review past outputs
- You can run multiple scripts sequentially without closing the terminal

Example with command-line arguments:
```bash
python data_analysis.py --input data.csv --output results.csv
```

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
