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

### <span style="color:#03A9F4">Using Cell Comments for Code Organization</span>

The Interactive Window allows you to organize your code into cells using special comments. Open the example file `resources/example_code/part2-interactive-window.py` and try running each cell by clicking the "Run Cell" button above the cell or using Shift+Enter.

Cells provide numerous benefits for research code:

1. **Code Separation**: Divide your analysis into logical sections using `# %%` comments
2. **Markdown Documentation**: Use `# %% [markdown]` for rich text notes, including:
   - Headers with different levels using `#`, `##`, `###`
   - Formatting with *italics* and **bold** text
   - Bulleted and numbered lists
3. **Mathematical Equations**: Include LaTeX formulas using `$equation$` or `$$equation$$`
4. **Incremental Development**: Run and track results from individual code sections
5. **Visual Comparison**: Modify a visualization cell and run it again to compare results
6. **Result Persistence**: Outputs remain visible in the Interactive Window between sessions

For example, in our sample file, you can:
1. Run the first few cells to see markdown formatting and mathematical equations
2. Execute the data loading cell to import the Titanic dataset
3. Run visualization cells to generate different plots of the same data
4. View tabular data in a readable format
5. Modify a visualization (like changing colors or labels) and run it again to see the changes

This workflow enables rapid iteration, documentation, and analysis tracking—ideal for reproducible research.

### <span style="color:#03A9F4">Working with Jupyter Notebooks (.ipynb)</span>

In addition to Python files with cell markers, VS Code provides excellent support for native Jupyter Notebooks (.ipynb files). These files combine code, output, visualizations, and formatted text in a single document. Open the example notebook file [`resources/example_code/part2-jupyter-notebook.ipynb`](resources/example_code/part2-jupyter-notebook.ipynb) to see the previous example but in an ipynb file. This file was made by saving the previous example in the interactive window. 

### Creating a New Jupyter Notebook

To create a new Jupyter Notebook in VS Code:

1. **Using the Command Palette**:
    - Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac)
    - Type "Jupyter: Create New Blank Notebook" and select it
    - The new notebook will open in the editor

2. **From the File Menu**:
    - Click File → New File
    - Select "Jupyter Notebook" from the options

Once your notebook is created, you can add new cells using the "+ Code" or "+ Markdown" buttons at the top of the notebook or by pressing `Alt+Enter` to create a new cell below the current one.

### <span style="color:#03A9F4">Interactive Window vs. Jupyter Notebooks</span>

While similar, these tools have important differences:

| Feature | Interactive Window | Jupyter Notebook |
|---------|-------------------|------------------|
| Cell execution | Runs cells from Python files | Self-contained cells |
| State persistence | Maintains session state | State saved in notebook file |
| Output handling | Displays in separate pane | Outputs embedded with cells |

**When to use which?**
- **Interactive Window**: For development-focused workflows where you want to maintain code in regular .py files but with interactive execution
- **Jupyter Notebooks**: For analysis-focused workflows, sharing results, and when the narrative and visualization are central to your work

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

### <span style="color:#03A9F4">Debugging Practice Example</span>

Open the example file `resources/example_code/part2-debugging-example.py` to practice debugging. This file contains a temperature analysis program with several deliberate bugs for you to find and fix:

1. Set a breakpoint at the beginning of the `main()` function
2. Start debugging by pressing F5
3. Use Step Into (F11) to move through the code execution
4. Watch how variable values change
5. Try to identify the bugs in the conversion functions, calculation logic, and error handling

Common bugs to look for:
- Mathematical errors in formulas
- Off-by-one errors in loops
- Incorrect dictionary keys
- Logical errors in calculations

Try to fix each bug you find, then run the program again to see if your solution works!

## <span style="color:#689F38">Advanced Debugging with launch.json</span>

### <span style="color:#03A9F4">Creating a launch.json File</span>

For more control over debugging, you can create a `launch.json` file:

1. Click the "Run and Debug" icon in the Activity Bar
2. Click "create a launch.json file" or the gear icon
3. Select "Python" from the environment options

VS Code will create a `.vscode` folder in your project with a `launch.json` file containing basic Python debugging configuration.

### <span style="color:#03A9F4">Customizing Your Debug Configuration</span>

Here's an example of a
