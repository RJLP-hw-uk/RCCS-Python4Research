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
# Now let's try with some problematic data to see what errors look like
empty_list = []
result = calculate_average(empty_list)

# %% [markdown]
# Understanding the traceback: 
"""
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
File RJLP-hw-uk\RCCS-Python4Research\resources\example_code\part2-debugging-example-1.py:1
----> 1 result = calculate_average(empty_list)

File RJLP-hw-uk\RCCS-Python4Research\resources\example_code\part2-debugging-example-1.py:8
      6 for num in numbers:
      7     total += num
----> 8 return total/len(numbers)

ZeroDivisionError: division by zero
"""

# The error message tells us:
# - **ZeroDivisionError**: This means we tried to divide by zero
# - **Traceback**: Shows the call stack leading to the error
# - The last line indicates where the error occurred: `return total/len(numbers)`


# %% [markdown]
# ## Debugging Method 1: Print Statements
# Sometimes no traceback is available, or you want to understand the flow of your code better.
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
def calculate_average_debug(numbers):
    """
    Calculate the average of a list of numbers.
    This function demonstrates debugging with breakpoints.
    """
    # Add a breakpoint here to see the input
    print(f"Input received: {numbers}")
    
    if not numbers:  # Add a breakpoint here to check empty list handling
        print("Empty list detected")
        return None
    
    total = 0  # Add a breakpoint here to see initial total
    
    for num in numbers:  # Add a breakpoint here to see each iteration
        total += num
        print(f"Added {num}, running total: {total}")
    
    average = total / len(numbers)  # Add a breakpoint here to see calculation
    print(f"Final calculation: {total} / {len(numbers)} = {average}")
    
    return average  # Add a breakpoint here to see the final result

# %%
# Test with good data
test_data = [10, 20, 30, 40, 50]
result = calculate_average_debug(test_data)
print(f"Average of {test_data}: {result}")

# %%
# Test with empty list (this should handle gracefully now)
empty_list = []
result_empty = calculate_average_debug(empty_list)
print(f"Average of empty list: {result_empty}")

# %%
# Test with single number
single_number = [42]
result_single = calculate_average_debug(single_number)
print(f"Average of {single_number}: {result_single}")

# %%
# Test with negative numbers
negative_numbers = [-10, -5, 0, 5, 10]
result_negative = calculate_average_debug(negative_numbers)
print(f"Average of {negative_numbers}: {result_negative}")

# %%
# This will cause a TypeError - mixing numbers with strings
mixed_types = [10, 20, "hello", 30]
try:
    result_mixed = calculate_average_debug(mixed_types)
    print(f"Average of mixed types: {result_mixed}")
except TypeError as e:
    print(f"TypeError occurred: {e}")

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
# ### Debugging Exercise with calculate_average:
# 
# 1. Add breakpoints by clicking in the left margin next to these key lines:
#    - Line 120: Function entry to see input parameters
#    - Line 125: Empty list check to see how edge cases are handled
#    - Line 109: Inside the loop to watch the accumulation process
#    - Line 112: Division line to see the final calculation
# 2. Start debugging by clicking the Run/Debug button
# 3. When execution pauses, examine the values of `numbers`, `total`, and `num`
# 4. Step through the code to understand the flow
# 5. Try running each test case to see how different inputs behave
