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

### <span style="color:#03A9F4">Common Debugging Methods</span>

Several approaches can help you diagnose and fix problems in your code:

1. **Print Statements - Simple yet effective**
   - Adding temporary `print()` statements to show variable values
   - Tracking program flow by printing markers at different points

2. **Interactive Debugging with Breakpoints - Like a surgical knife for coding**
   - Setting points where execution pauses for inspection
   - Examining variables of your program at runtime and how they change
   - Stepping through code execution line by line

3. **Using the Debug Console - For quick tests while in debug mode**
   - Evaluating expressions in the current execution context
   - Testing potential fixes without modifying your code
   - Inspecting complex data structures interactively

4. **Log-Based Debugging - Traceable and informative but requires setup**
   - Using logging modules instead of print statements
   - Creating persistent debug records for complex applications
   - Configuring different levels of detail (debug, info, warning, error)

5. **Exception Handling - Pre-emptive method**
   - Using try/except blocks to catch and diagnose errors
   - Understanding error messages and stack traces
   - Implementing graceful error recovery

interactive debugging with breakpoints, although print statement debugging remains valuable for quick troubleshooting. Both approaches complement each other and form the foundation of effective debugging practices.

### <span style="color:#03A9F4">Print Statement Debugging</span>

Print statement debugging is the most accessible approach - simply adding strategic print statements to see what's happening in your code. This technique is demonstrated in `part2-debugging-example-1.py`:

```python
# Example from part2-debugging-example-1.py
def calculate_average_with_prints(numbers):
    """Calculate the average with debug prints."""
    print(f"Input: {numbers}")
    print(f"Input length: {len(numbers)}")
    
    total = 0
    for num in numbers:
        total += num
        print(f"Added {num}, total is now {total}")
    
    print(f"Final total: {total}, dividing by length: {len(numbers)}")
    return total/len(numbers)
```

When executed with input `[10, 20, 30]`, this produces output that helps trace the execution:
```
Input: [10, 20, 30]
Input length: 3
Added 10, total is now 10
Added 20, total is now 30
Added 30, total is now 60
Final total: 60, dividing by length: 3
20.0
```

This approach helps you:
- Verify input data is what you expect
- Track how values change during execution 
- Identify exactly where issues occur (like division by zero with empty lists)
- Understand the flow of execution through your code

Print debugging is often sufficient for simple bugs and doesn't require any special tools or setup - making it the quickest way to start diagnosing problems.

### <span style="color:#03A9F4">Basic Debugging with Breakpoints</span>

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

### <span style="color:#03A9F4">Debugging Complex Data Structures</span>

When working with nested data (lists of lists, dictionaries of dictionaries, etc.), breakpoints are particularly valuable:

```python
def find_value_in_nested_list(nested_list, target_value):
    """Find the first occurrence of target_value in a nested list structure."""
    def search_nested(current_list, current_path):
        # Place a breakpoint here to examine the current state
        
        if isinstance(current_list, list):
            for i, item in enumerate(current_list):
                path = current_path + [i]
                if item == target_value:
                    # Place a breakpoint here to see when we find a match
                    return path
                elif isinstance(item, list):
                    # Place a breakpoint here to observe recursive calls
                    result = search_nested(item, path)
                    if result:
                        return result
        return None
    
    return search_nested(nested_list, [])
```

With breakpoints at strategic locations, you can:
- Watch the recursion unfold
- See how the path is constructed
- Understand exactly how your algorithm traverses complex structures

### <span style="color:#03A9F4">Using the Debug Console</span>

During debugging, you can interact with your code using the Debug Console:
1. While at a breakpoint, find the Debug Console tab at the bottom of VS Code
2. Type expressions to evaluate them in the current context
3. This allows you to test hypotheses about your code's behavior

For example, if you're stopped at a breakpoint inside a function, you can check variable values or test calculations without modifying your actual code.

### <span style="color:#03A9F4">Debugging Practice Example</span>

Open the example file `resources/example_code/part2-debugging-example-1.py` to practice debugging. This file contains:

1. A simple function with a potential division-by-zero bug
2. Examples of print statement debugging
3. A complex nested list search function perfect for interactive debugging

Try these debugging exercises:
1. Run the code and identify the bug in the `calculate_average` function
2. Add print statements to debug the issue
3. Fix the bug by adding proper error handling
4. Use breakpoints to trace through the nested list search function
5. Observe how the search algorithm works by stepping through the code

Common bugs to look for:
- Division by zero (empty lists)
- Off-by-one errors in loops
- Type errors when processing mixed data
- Incorrect handling of edge cases

### <span style="color:#03A9F4">Debugging with Exception Handling</span>

Adding proper exception handling helps create more robust code:

```python
def calculate_average_safe(numbers):
    """Calculate the average with proper error handling."""
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    
    total = sum(numbers)
    return total / len(numbers)

# Using with try/except
try:
    result = calculate_average_safe([])
except ValueError as e:
    print(f"Handled error: {e}")
    result = 0  # Default value or appropriate fallback
```

Proper exception handling makes debugging easier by:
- Providing clear error messages
- Failing early and explicitly
- Making error conditions obvious

## <span style="color:#689F38">Advanced Debugging with launch.json</span>

### <span style="color:#03A9F4">Creating a launch.json File</span>

For more control over debugging, you can create a `launch.json` file:

1. Click the "Run and Debug" icon in the Activity Bar
2. Click "create a launch.json file" or the gear icon
3. Select "Python" from the environment options

VS Code will create a `.vscode` folder in your project with a `launch.json` file containing basic Python debugging configuration.

### <span style="color:#03A9F4">Customizing Your Debug Configuration</span>

Here's an example of a
