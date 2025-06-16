# %% [markdown]
# # Simple Debugging Example
# 
# This notebook demonstrates basic debugging techniques in Python using Jupyter Notebook cells.
# We'll create a simple function with a bug, then use different methods to find and fix it.

# %%
# First, let's import what we need
import numpy as np
import matplotlib.pyplot as plt

# %%
# Here's our function with a bug
def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    total = 0
    for num in numbers:
        total += num
    return total/len(numbers)  # What happens if numbers is empty?

# %%
# Let's test our function
test_data = [10, 20, 30, 40, 50]
print(f"Average of {test_data}: {calculate_average(test_data)}")

# %%
# Now let's try with some problematic data
empty_list = []
try:
    result = calculate_average(empty_list)
    print(f"Average of empty list: {result}")
except Exception as e:
    print(f"Error occurred: {type(e).__name__}: {e}")

# %% [markdown]
# ## Debugging Method 1: Print Statements
# Let's add print statements to see what's happening inside the function

# %%
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

# %%
# Try with good data
calculate_average_with_prints([10, 20, 30])

# %% [markdown]
# ## Debugging Method 2: Interactive Debugging with VS Code Breakpoints
# 
# Let's see how to use visual breakpoints in VS Code to debug a complex function.
# This example finds the first occurrence of a value in a nested list structure.
# 
# ### Adding Breakpoints in VS Code:
# 
# 1. To add a breakpoint, click in the left margin (gutter) next to the line number
# 2. A red dot will appear, indicating a breakpoint is set
# 3. Try adding breakpoints at these key lines:
#    - Line 143: Inside the `search_nested` function definition
#    - Line 147: Where we check if the item equals the target value
#    - Line 149: Where recursion happens for nested lists
# 
# When you run the code with the "Run" button or Debug menu, execution will pause at these breakpoints.

# %%
def find_value_in_nested_list(nested_list, target_value):
    """
    Find the first occurrence of target_value in a nested list structure.
    Returns the path to the value as a list of indices, or None if not found.
    """
    def search_nested(current_list, current_path):
        # Add a breakpoint by clicking in the left margin next to this line
        
        if isinstance(current_list, list):
            for i, item in enumerate(current_list):
                path = current_path + [i]
                if item == target_value:
                    # Add a breakpoint here to see when we find a match
                    return path
                elif isinstance(item, list):
                    # Add a breakpoint here to observe recursive calls
                    result = search_nested(item, path)
                    if result:
                        return result
        return None
    
    return search_nested(nested_list, [])

# %%
# Test data with a nested structure
nested_data = [1, 2, [3, 4, [5, 6]], 7, [8, 9]]

# Test the function
target = 6
path = find_value_in_nested_list(nested_data, target)
print(f"Path to value {target}: {path}")

# %%
# Let's try with a value that doesn't exist
missing_target = 10
path = find_value_in_nested_list(nested_data, missing_target)
print(f"Path to value {missing_target}: {path}")

# %% [markdown]
# ### Using VS Code Breakpoints for Debugging
# 
# When execution stops at a breakpoint:
# 
# 1. The VS Code Debug view will open automatically
# 2. You can inspect variables in the "Variables" panel
# 3. Use the Debug toolbar to control execution:
#    - Step Over (F10): Execute the current line and move to the next line
#    - Step Into (F11): Move into a function call
#    - Step Out (Shift+F11): Complete the current function and return to the caller
#    - Continue (F5): Resume execution until the next breakpoint
# 
# ### Debugging Exercise:
# 
# 1. Add breakpoints by clicking in the left margin next to lines 143, 147, and 149
# 2. Start debugging by clicking the Run/Debug button
# 3. When execution pauses, examine the values of `current_list` and `current_path`
# 4. Step through the code to see how the function traverses the nested list
# 5. Note how the path gets built up as you move deeper into the nested structure
