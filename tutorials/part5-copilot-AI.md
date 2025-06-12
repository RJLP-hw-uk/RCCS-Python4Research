# <span style="color:#9575CD">Getting GitHub Copilot and Using it Properly</span>

## Table of Contents
- [Step 1: Understanding GitHub Copilot](#step-1-understanding-github-copilot)
- [Step 2: Getting Student Access](#step-2-getting-student-access)
- [Step 3: Setting Up Copilot in VS Code](#step-3-setting-up-copilot-in-vs-code)
- [Step 4: Basic Copilot Usage](#step-4-basic-copilot-usage)
- [Step 5: Advanced Prompting Techniques](#step-5-advanced-prompting-techniques)
- [Step 6: Best Practices](#step-6-best-practices)
- [Step 7: Hands-on Exercise](#step-7-hands-on-exercise)

## <span style="color:#689F38">Step 1: Understanding GitHub Copilot</span>

### <span style="color:#03A9F4">What is GitHub Copilot?</span>

GitHub Copilot is an AI pair programmer that helps you write code faster and with less work. It draws context from comments and code to suggest individual lines and whole functions instantly.

Key features:
- Suggests code as you type
- Generates entire functions from comments
- Helps with repetitive code patterns
- Learns from your coding style
- Supports multiple programming languages (Python, Latex, etc.)

### <span style="color:#03A9F4">Why Use Copilot for Research?</span>

For researchers, Copilot can:
- Speed up data analysis script creation
- Help implement statistical methods correctly
- Generate boilerplate code for visualization
- Assist with unfamiliar libraries or APIs
- Explain code functionality through comments

## <span style="color:#689F38">Step 2: Getting Student Access</span>

GitHub Copilot is available for free to verified academics through the GitHub Student/Teacher Developer Pack.

### <span style="color:#03A9F4">Accessing GitHub Student Developer Pack</span>

1. Visit [GitHub Education](https://education.github.com/pack)
2. Click "Get the Pack"
3. Sign in with your GitHub account (or create one)
4. Click "Get student benefits"
5. Verify your student status using your university email

![GitHub Student Developer Pack Page](/resources/images/github-student-pack.png)

### <span style="color:#03A9F4">Activating GitHub Copilot</span>

After your student status is verified:

1. Go to [GitHub Copilot](https://github.com/features/copilot)
2. Click "Start my free trial"
3. Follow the prompts to activate Copilot for your account
4. Verify that Copilot shows as active in your GitHub account settings

> **Note**: Verification may take up to 48 hours, but is usually much faster.

## <span style="color:#689F38">Step 3: Setting Up Copilot in VS Code</span>

### <span style="color:#03A9F4">Installing the Copilot Extension</span>

1. Open VS Code
2. Click the Extensions icon in the Activity Bar (or press `Ctrl+Shift+X`)
3. Search for "GitHub Copilot"
4. Click "Install" on the GitHub Copilot extension
5. After installation, click "Sign in to GitHub" when prompted

![GitHub Copilot Extension](/resources/images/copilot-extension.png)

### <span style="color:#03A9F4">Verifying Installation</span>

To verify Copilot is working:

1. Create a new Python file (e.g., `test_copilot.py`)
2. Type a comment describing a simple function, like:
   ```python
   # Function to calculate the mean of a list of numbers
   ```
3. Press Enter and wait a moment
4. Copilot should suggest code for this function

If Copilot suggestions appear as ghosted text, the installation was successful.

## <span style="color:#689F38">Step 4: Basic Copilot Usage</span>

### <span style="color:#03A9F4">Getting Code Suggestions</span>

Copilot provides suggestions in several ways:

**1. Inline Completions:**
As you type, Copilot offers completions. Press `Tab` to accept a suggestion or continue typing to ignore it.

**2. Generating from Comments:**
Write a descriptive comment about what you want to accomplish:

```python
# Create a scatter plot of x and y with a trend line
```

**3. Function Signatures:**
Start typing a function and Copilot will suggest the full signature:

```python
def calculate_correlation(x, y):
```

**4. Completing Patterns:**
If Copilot detects a pattern in your code, it will suggest similar code:

```python
# After writing code to process one column
df['column1'] = df['column1'].fillna(0)
# Copilot might suggest:
# df['column2'] = df['column2'].fillna(0)
```

### <span style="color:#03A9F4">Keyboard Shortcuts</span>

- `Tab`: Accept the current suggestion
- `Esc`: Dismiss the current suggestion
- `Alt+]` (Windows) / `Option+]` (Mac): See next suggestion
- `Alt+[` (Windows) / `Option+[` (Mac): See previous suggestion
- `Ctrl+Enter`: Open Copilot suggestions in a separate panel

## <span style="color:#689F38">Step 5: Advanced Prompting Techniques</span>

### <span style="color:#03A9F4">Writing Effective Prompts</span>

The key to getting useful suggestions from Copilot is writing clear, specific prompts:

**1. Be Specific:**
```python
# BAD: Plot the data
# GOOD: Create a scatter plot of temperature vs. humidity with blue points and a red trend line
```

**2. Include Expected Inputs/Outputs:**
```python
# Function that takes a DataFrame with columns 'temp' and 'humidity'
# and returns a new DataFrame with an additional 'heat_index' column
```

**3. Specify Libraries:**
```python
# Using pandas and matplotlib, load data.csv and create a histogram of the 'age' column
```

**4. Reference Existing Code:**
Make sure related functions or variables are visible in the same file to give Copilot context.

### <span style="color:#03A9F4">Using Copilot Chat</span>

If you have access to Copilot Chat (newer feature):

1. Open Copilot Chat with `Ctrl+Shift+I` (Windows) or `Cmd+Shift+I` (Mac)
2. Ask questions about your code or request code snippets
3. Use specific commands like `/explain` to understand code or `/tests` to generate tests

## <span style="color:#689F38">Step 6: Best Practices</span>

### <span style="color:#03A9F4">Verify and Understand Generated Code</span>

Always review Copilot's suggestions for:

1. **Correctness**: Does the code do what you intended?
2. **Efficiency**: Is this the most efficient solution?
3. **Security**: Are there any potential security issues?
4. **Understanding**: Make sure you understand how the suggested code works

> **Personal Experience**: Copilot is excellent for suggesting code, but it occasionally makes subtle errors or assumptions. Always run and test the generated code before relying on it.

### <span style="color:#03A9F4">Ethical Considerations</span>

When using Copilot, consider:

1. **Citation**: If Copilot helps implement an algorithm or method for research, cite both the original method and mention that Copilot assisted with implementation
2. **Learning**: Use Copilot as a learning tool, not just to copy solutions
3. **Verification**: Always verify that generated code is correct and appropriate for your needs
4. **Ownership**: Understand that you are responsible for all code in your project, even if AI-assisted


## <span style="color:#689F38">Dos and Don'ts for New Programmers</span>

### <span style="color:#03A9F4">Dos</span>

- **DO** learn basic programming concepts first - understand variables, loops, conditionals, and functions before heavily relying on Copilot
- **DO** use Copilot to explore different approaches to problems you already understand
- **DO** carefully review all generated code line-by-line to understand how it works
- **DO** try writing code yourself first before asking Copilot for help
- **DO** use Copilot to learn new libraries and APIs by examining its suggestions
- **DO** break down complex problems into smaller parts with specific prompts
- **DO** test all generated code thoroughly - never assume it works correctly

### <span style="color:#03A9F4">Don'ts</span>

- **DON'T** use Copilot as a substitute for learning core programming concepts
- **DON'T** blindly accept and use suggestions without understanding them
- **DON'T** rely on Copilot for critical or sensitive code without thorough review
- **DON'T** assume Copilot always generates the most efficient or correct solution
- **DON'T** use Copilot to complete programming assignments without permission
- **DON'T** forget that Copilot may generate outdated or incorrect code
- **DON'T** let Copilot handle complex error handling or security-critical code

### <span style="color:#03A9F4">Balancing Learning and Assistance</span>

For new programmers, the key challenge is using Copilot as a learning aid without becoming dependent on it:

1. **Start with basics manually**: Write simple code yourself to build fundamental skills
2. **Understand before using**: Always ensure you can explain how generated code works
3. **Learn from suggestions**: When Copilot suggests code you wouldn't have written, take time to study why it works
4. **Gradually increase usage**: Start with using Copilot for simple tasks, then gradually use it for more complex problems as your understanding grows

### <span style="color:#03A9F4">Common Pitfalls for Beginners</span>

1. **Overreliance**: Becoming dependent on Copilot and struggling to code without it
   - *Solution*: Set aside time to code without Copilot to build your skills

2. **Skipping fundamentals**: Using Copilot before understanding basic programming concepts
   - *Solution*: Take a structured approach to learning programming basics first

3. **Copy without comprehension**: Implementing code you don't understand
   - *Solution*: Challenge yourself to explain each line of generated code

4. **False confidence**: Assuming all generated code is correct and optimal
   - *Solution*: Always test and review generated code carefully

5. **Neglecting debugging skills**: Not learning how to troubleshoot when code doesn't work
   - *Solution*: Deliberately practice debugging Copilot-generated code

## <span style="color:#689F38">Step 7: Hands-on Exercise</span>

Let's practice using Copilot with a simple research-oriented task:

### <span style="color:#03A9F4">Exercise: Data Analysis Script</span>

1. Create a new Python file called `copilot_exercise.py`
2. Add this comment and let Copilot generate the code:
```python
# Import necessary libraries for data analysis and visualization

# Generate a synthetic dataset with 100 points representing:
# - independent variable 'x' (normally distributed)
# - dependent variable 'y' that follows y = 2x + 3 + random noise

# Calculate summary statistics for x and y

# Create a scatter plot with a regression line
# Add labels, title, and save the figure as 'regression_analysis.png'

# Perform a linear regression and print the coefficient and intercept
```

3. Review, edit, and run the generated code
4. Try modifying the comments to see how Copilot's suggestions change

### <span style="color:#03A9F4">Example Solution</span>

Here's an example of what Copilot might generate (your results may vary):

```python
# Import necessary libraries for data analysis and visualization
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Generate a synthetic dataset with 100 points representing:
# - independent variable 'x' (normally distributed)
# - dependent variable 'y' that follows y = 2x + 3 + random noise
np.random.seed(42)  # for reproducibility
x = np.random.normal(0, 1, 100)
y = 2 * x + 3 + np.random.normal(0, 1, 100)

# Convert to DataFrame for easier handling
data = pd.DataFrame({'x': x, 'y': y})

# Calculate summary statistics for x and y
summary_stats = data.describe()
print("Summary Statistics:")
print(summary_stats)

# Create a scatter plot with a regression line
plt.figure(figsize=(10, 6))
plt.scatter(x, y, alpha=0.7)

# Add regression line
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
line_x = np.linspace(min(x), max(x), 100)
line_y = slope * line_x + intercept
plt.plot(line_x, line_y, 'r-', linewidth=2)

# Add labels, title, and save the figure
plt.xlabel('X Variable')
plt.ylabel('Y Variable')
plt.title(f'Linear Regression (y = {slope:.2f}x + {intercept:.2f}, R² = {r_value**2:.2f})')
plt.grid(True, alpha=0.3)
plt.savefig('regression_analysis.png', dpi=300)
plt.show()

# Perform a linear regression and print the coefficient and intercept
print(f"Regression Results:")
print(f"Slope (coefficient): {slope:.4f}")
print(f"Intercept: {intercept:.4f}")
print(f"R-squared: {r_value**2:.4f}")
print(f"P-value: {p_value:.4g}")
print(f"Standard Error: {std_err:.4f}")
```

## <span style="color:#689F38">Next Steps</span>

Now that you understand how to use GitHub Copilot effectively:
- Try using it in your own research projects
- Experiment with more complex prompts
- Explore Copilot Chat for code explanations
- Continue to the next tutorial to learn more advanced Python techniques for research