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

The Interactive Window allows you to organize your code into cells using special comments. Open the example file [`resources/example_code/part2-interactive-window.py`](resources/example_code/part2-interactive-window.py) and try running each cell by clicking the "Run Cell" button above the cell or using Shift+Enter.

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

## <span style="color:#03A9F4">Working with Jupyter Notebooks (.ipynb)</span>

In addition to Python files with cell markers, VS Code provides excellent support for native Jupyter Notebooks (.ipynb files). These files combine code, output, visualizations, and formatted text in a single document. Open the example notebook file [`resources/example_code/part2-jupyter-notebook.ipynb`](resources/example_code/part2-interactive-window.ipynb) to see the previous example but in an ipynb file. This file was made by saving the previous example in the interactive window. 

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

## <span style="color:#03A9F4">Interactive Window vs. Jupyter Notebooks</span>

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

Print statement debugging is the most accessible approach - simply adding strategic print statements to see what's happening in your code. This technique is demonstrated in [`resources/example_code/part2-debugging-example-1.py`](resources/example_code/part2-debugging-example-1.py):

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

Let's practice breakpoint debugging using the `calculate_average_debug` function from [`resources/example_code/part2-debugging-example-1.py`](resources/example_code/part2-debugging-example-1.py). This function demonstrates how to strategically place breakpoints to understand code execution:

```python
def calculate_average_debug(numbers):
    """
    Calculate the average of a list of numbers.
    This function demonstrates debugging with breakpoints.
    """
    # BREAKPOINT 1: Add here to see the input
    print(f"Input received: {numbers}")
    
    if not numbers:  # BREAKPOINT 2: Add here to check empty list handling
        print("Empty list detected")
        return None
    
    total = 0  # BREAKPOINT 3: Add here to see initial total
    
    for num in numbers:  # BREAKPOINT 4: Add here to see each iteration
        total += num
        print(f"Added {num}, running total: {total}")
    
    average = total / len(numbers)  # BREAKPOINT 5: Add here to see calculation
    print(f"Final calculation: {total} / {len(numbers)} = {average}")
    
    return average  # BREAKPOINT 6: Add here to see the final result
```

**Step-by-step debugging instructions:**

1. **Set strategic breakpoints** by clicking in the gutter (left margin) next to these line numbers:
   - **Line with `print(f"Input received: {numbers}")`** - to examine what data enters the function
   - **Line with `if not numbers:`** - to see how empty list detection works
   - **Line with `for num in numbers:`** - to watch the loop iteration begin
   - **Line with `total += num`** - to observe how the total accumulates
   - **Line with `average = total / len(numbers)`** - to see the final calculation

2. **Start debugging** by:
   - Opening the file `part2-debugging-example-1.py`
   - Pressing F5, or clicking the debug icon in the activity bar, then the play button
   - Or right-clicking and selecting "Debug Python File"

3. **Control execution** with the debug toolbar:
   - **Continue (F5)**: Run until the next breakpoint
   - **Step Over (F10)**: Execute the current line and stop at the next line
   - **Step Into (F11)**: Enter a function call to debug its internal code
   - **Step Out (Shift+F11)**: Complete the current function and return to the caller

4. **Inspect variables** in the Variables pane:
   - Watch how `numbers`, `total`, and `num` change as you step through
   - Notice how `average` appears only after the calculation line executes

**Try these debugging scenarios:**

- **Normal case**: Run with `test_data = [10, 20, 30, 40, 50]` and step through to see normal execution
- **Empty list**: Run with `empty_list = []` to see how the function handles edge cases
- **Single value**: Run with `single_number = [42]` to verify the calculation works with one item
- **Error case**: Run with `mixed_types = [10, 20, "hello", 30]` to see how type errors are caught

When stopped at each breakpoint, use the Variables pane to inspect the current state and the Debug Console to test expressions like `len(numbers)` or `type(num)`.

### <span style="color:#03A9F4">Debugging Complex Data Structures</span>
When debugging research code, complex data structures are common - datasets with multiple dimensions, experimental results organized in nested dictionaries, or model outputs with hierarchical structures. Breakpoints excel at helping you understand these complex data flows:

```python
def analyze_experimental_results(experiment_data):
    """Analyze nested experimental data with multiple conditions and measurements."""
    results_summary = {}
    
    for experiment_id, conditions in experiment_data.items():
        # Place a breakpoint here to examine each experiment's structure
        condition_averages = {}
        
        for condition_name, measurements in conditions.items():
            # Place a breakpoint here to inspect measurement arrays
            if len(measurements) > 0:
                avg_value = sum(measurements) / len(measurements)
                std_dev = (sum((x - avg_value) ** 2 for x in measurements) / len(measurements)) ** 0.5
                
                condition_averages[condition_name] = {
                    'mean': avg_value,
                    'std': std_dev,
                    'n_samples': len(measurements)
                }
                # Place a breakpoint here to verify calculations
        
        results_summary[experiment_id] = condition_averages
    
    return results_summary
```

With breakpoints at strategic locations, you can:
- Inspect the structure of incoming experimental data
- Verify statistical calculations are working correctly
- Watch how summary statistics accumulate across conditions
- Debug data quality issues (missing values, unexpected formats)
- Understand complex data transformations step-by-step

This approach is invaluable when working with real research data that often has irregular structures, missing values, or unexpected formats that can break your analysis pipeline.

### <span style="color:#03A9F4">Using the Debug Console</span>

During debugging, you can interact with your code using the Debug Console:

1. While at a breakpoint, find the Debug Console tab at the bottom of VS Code
2. Type expressions to evaluate them in the current context
3. This allows you to test hypotheses about your code's behavior

For example, if you're stopped at a breakpoint inside a function, you can check variable values or test calculations without modifying your actual code.

> **Pro Tip:** I've added the shortcut Alt+E to send selections to the debug console. This allows you to quickly highlight code in your editor and send it to the debug console for evaluation while debugging.


