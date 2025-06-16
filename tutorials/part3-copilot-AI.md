# <span style="color:#9575CD">Getting GitHub Copilot and Using it Properly</span>

## Table of Contents
- [Step 1: Understanding GitHub Copilot](#step-1-understanding-github-copilot)
- [Step 2: Getting Access](#step-2-getting-access)
- [Step 3: Setting Up Copilot in VS Code](#step-3-setting-up-copilot-in-vs-code)
- [Step 4: Basic Copilot Usage](#step-4-basic-copilot-usage)
- [Step 5: Best Practices and Guidelines](#step-5-best-practices-and-guidelines)
- [Step 6: Hands-on Exercise](#step-6-hands-on-exercise)
- [Next Steps](#next-steps)

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

## <span style="color:#689F38">Step 2: Getting Access</span>

GitHub Copilot is available for free to verified academics through the GitHub Student/Teacher Developer Pack.

### <span style="color:#03A9F4">Setting Up Your GitHub Account</span>

1. Go to the GitHub website at [https://github.com](https://github.com)
2. Click "Sign up" in the top-right corner if you don't have an account, or "Sign in" if you already have one
3. Create a GitHub account using your university email, or link your university email to an existing GitHub account
   - If creating a new account: Fill out the registration form with your name, university email, and password
   - If using existing account: Go to your profile icon → Settings → Emails → Add email
4. Verify your university email address when prompted by checking your inbox and clicking the verification link
5. After signing in, click on your profile icon in the top-right corner and select "Settings"
6. To add billing information:
   - In the left sidebar, click on "Billing and plans"
   - Enter your university address/information when prompted
7. Enable two-factor authentication (required for GitHub benefits):
   - In the left sidebar, navigate to "Password and authentication"
   - Look for the "Two-factor authentication" section and click "Enable"
   - Follow the on-screen instructions to complete the setup

### <span style="color:#03A9F4">Applying for Education Benefits</span>

1. Go to your GitHub account settings
2. Under "Billing and plans," select "Education benefits"
3. Start a new application for GitHub Education benefits
4. IMPORTATNT: Complete the verification process with your student/staff ID card AND use the camera to do so
5. Wait 3 minutes for approval. Once approved you'll have full access to copilot the following day.

## <span style="color:#689F38">Step 3: Setting Up Copilot in VS Code</span>

### <span style="color:#03A9F4">Installing the Copilot Extension</span>

1. Open VS Code
2. Click the Extensions icon in the Activity Bar (or press `Ctrl+Shift+X`)
3. Search for "GitHub Copilot"
4. Click "Install" on the GitHub Copilot extension
5. After installation, sign in to VS Code with your GitHub account:
   - Click the account icon in the bottom-left corner
   - Select "Sign in to GitHub"
   - Your browser will open
   - Authorize VS Code in the browser
   - Return to VS Code
   - Wait for the "GitHub Copilot" extension to activate

![GitHub Copilot Extension](/resources/images/copilot-extension.png)

### <span style="color:#03A9F4">Verifying Installation</span>

To verify Copilot is working:

1. Create a new Python file (`Ctrl+N` for new file, then `Ctrl+S` to save as `test_copilot.py`)
2. Type a comment describing a simple function, like:
   ```python
   # Function to calculate the mean of a list of numbers
   ```
4. Press `Tab` to accept the ghosted text for the function that Copilot suggests.

If Copilot suggestions appear as ghosted text, the installation was successful.

## <span style="color:#689F38">Step 4: Basic Copilot Usage</span>

### <span style="color:#03A9F4">1. Inline Suggestions</span>

Copilot offers real-time code suggestions as you type:
- Press `Tab` to accept a suggestion
- Keep typing to ignore it
- Works best for completing lines or short blocks

Example:
```python
# Copilot suggests completions as you type
def calculate_mean(numbers):
   # It will suggest: return sum(numbers) / len(numbers)
```

### <span style="color:#03A9F4">2. Copilot Chat (Ctrl+Shift+I)</span>

Chat interface for complex interactions:
- Generate longer code snippets
- Ask questions about your codebase
- Reference multiple files or functions
- Copy generated code or apply directly to editor

Example chat prompts:
```
"Generate a function to process CSV files using pandas"
"How can I optimize this loop for better performance?"
"Write a test suite for the UserAuth class"
```

### <span style="color:#03A9F4">3. Inline Editor (Ctrl+I)</span>

Surgical code modifications:
1. Select code you want to modify
2. Press Ctrl+I
3. Describe the desired changes
4. Accept or reject suggestions

Example uses:
- Convert code to use different libraries
- Add error handling
- Optimize selected functions

## <span style="color:#689F38">Step 5: Best Practices and Guidelines</span>

### <span style="color:#03A9F4">Important Note</span>
Think of GitHub Copilot as an enthusiastic but junior intern - everything it suggests must be carefully reviewed and fully understood before use. While it can speed up development, you are ultimately responsible for the code's correctness, security, and performance.

### <span style="color:#03A9F4">Dos</span>
- Learn basic programming concepts first
- Review all generated code line-by-line
- Test code thoroughly before using
- Use as a learning tool for new libraries/APIs
- Break down complex problems into smaller parts
- Try writing code yourself first

### <span style="color:#03A9F4">Don'ts</span>
- Don't use as a substitute for learning
- Don't blindly accept suggestions
- Don't rely on it for critical/sensitive code
- Don't assume it's always correct/efficient
- Don't use for assignments without permission
- Don't let it handle security-critical code

### <span style="color:#03A9F4">Key Considerations</span>

1. **Verification**
   - Check correctness and efficiency
   - Review for security issues
   - Ensure you understand the code
   - Test thoroughly

2. **Ethics**
   - Cite both original methods and AI assistance in research
   - Use as a learning tool, not just for solutions
   - Take responsibility for all code in your project

3. **Common Pitfalls**
   - Overreliance on Copilot
   - Skipping fundamental learning
   - Implementing without understanding
   - Neglecting debugging skills


## <span style="color:#689F38">Step 6: Hands-on Exercise</span>

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