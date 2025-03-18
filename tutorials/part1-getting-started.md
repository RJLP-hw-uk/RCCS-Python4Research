# <span style="color:#9575CD">Part 1: Getting Started with Python on VS Code</span>

## Table of Contents
- [Step 1: Setting Up Anaconda](#step-1-setting-up-anaconda)
- [Step 2: Creating Your First Environment](#step-2-creating-your-first-environment)
- [Step 3: Installing Essential Python Packages](#step-3-installing-essential-python-packages)
- [Step 4: Setting Up VS Code](#step-4-setting-up-vs-code)
- [Step 5: Navigating VS Code](#step-5-navigating-vs-code)
- [Step 6: Installing Extensions](#step-6-installing-extensions)
- [Step 7: Connecting VS Code to Your Conda Environment](#step-7-connecting-vs-code-to-your-conda-environment)

## <span style="color:#689F38">Step 1: Setting Up Anaconda</span>

### <span style="color:#03A9F4">Heriot-Watt University Computers (Windows)</span>

1. Open the Software Centre from the Start menu
2. Search for "Anaconda 3"
3. Click "Install" and wait for the installation to complete
4. Launch Anaconda Navigator from the Start menu after installation

![Heriot-Watt Software Centre](resources/images/software-centre-anaconda.png)

After installation, you'll be able to access Anaconda from the Start menu. This provides you with the same functionality as a personal installation of Anaconda.

### <span style="color:#03A9F4">Option 1: Anaconda with Navigator (Recommended for Beginners)</span>

For personal computers not managed by Heriot-Watt University:

1. Download Anaconda from the [official website](https://www.anaconda.com/download)
2. Run the installer and follow the prompts
3. Launch Anaconda Navigator from your start menu or applications folder

![Anaconda Download Page](resources/images/anaconda-download.png)

Anaconda comes with a user-friendly graphical interface called Navigator that makes it easy to create environments and install packages without using command-line instructions.

![Anaconda Navigator Home](resources/images/anaconda-navigator-home.png)

### <span style="color:#03A9F4">Option 2: Miniconda (Advanced/Faster Option)</span>

If you prefer a more lightweight installation or are comfortable with command-line interfaces (CLI):

1. Download Miniconda from the [official website](https://docs.conda.io/en/latest/miniconda.html)
2. Run the installer and follow the prompts
3. Open the Anaconda Prompt (or terminal on Mac/Linux)

Miniconda provides the same core functionality as Anaconda but with a smaller footprint and is primarily operated through command-line instructions.

## <span style="color:#689F38">What is Anaconda/Miniconda and Why Use Environment Managers?</span>

### <span style="color:#03A9F4">Understanding Package Management</span>

Anaconda is a free distribution of Python that includes conda, a powerful package, dependency, and environment manager. Think of it as a way to create isolated workspaces for your Python projects.

### <span style="color:#03A9F4">Understanding Conda Environments</span>

Think of conda environments like separate folders in Windows Explorer. Just as you might have different folders for different projects, conda environments let you have separate "folders" for different Python setups.

In Windows Explorer, if you keep all your files in one folder, things get messy and hard to find. Similarly, if you install all Python packages in one environment, they can conflict with each other.

### <span style="color:#03A9F4">Why Environment Management Matters</span>

Environment management helps you:
- Maintain reproducible research
- Share your exact setup with colleagues
- Avoid "it works on my machine" problems
- Manage projects with conflicting dependencies

> **Personal Experience**: 

## <span style="color:#689F38">Step 2: Creating Your First Environment</span>

### <span style="color:#03A9F4">Using Anaconda Navigator (Beginner-Friendly)</span>

1. Open Anaconda Navigator
2. Click on the "Environments" tab in the left sidebar
3. Click the "Create" button at the bottom of the environments list
4. Name your environment "research-env" and select Python 3.11 from the dropdown
5. Click "Create" to finalize your environment

![Creating Environment in Navigator](resources/images/create-environment-navigator.png)

To activate this environment in Navigator, simply click on its name in the environments list. You can then return to the "Home" tab to install applications that will use this environment.

### <span style="color:#03A9F4">Using Command Line (Advanced)</span>

Open Anaconda Prompt (or terminal on Mac/Linux) and run:
```bash
conda create --name research-env python=3.11
```

To activate this environment:
```bash
conda activate research-env
```
Your prompt should change to show the active environment.

## <span style="color:#689F38">Step 3: Installing Essential Python Packages</span>

### <span style="color:#03A9F4">Using Anaconda Navigator (Beginner-Friendly)</span>

1. Open Anaconda Navigator
2. Make sure your "research-env" is active (click on it in the Environments tab)
3. Return to the "Home" tab
4. Select your environment from the dropdown menu (it may say "Applications on" followed by your environment name)
5. Click on "Install" under the packages you want to add (numpy, pandas, scipy, matplotlib)
6. Wait for the installation to complete

![Installing Packages in Navigator](resources/images/installing-packages-navigator.png)

### <span style="color:#03A9F4">Using Command Line (Advanced)</span>

Once your environment is active (you should see "(research-env)" at the beginning of your command prompt), install packages by running:
```bash
conda install numpy pandas scipy matplotlib
```

You can install multiple packages in a single command as shown above. To confirm successful installation:
```bash
conda list
```

**What These Packages Do:**

- **NumPy**: Provides support for large, multi-dimensional arrays and matrices, along with mathematical functions to operate on these elements. It's the foundation for scientific computing in Python.
- **Pandas**: Offers data structures and operations for manipulating numerical tables and time series. Think of it as "Excel for Python" but much more powerful.
- **SciPy**: Builds on NumPy with additional functionality for optimization, signal processing, statistics, and more.
- **Matplotlib**: The standard plotting library for creating static, animated, and interactive visualizations.

### <span style="color:#03A9F4">Alternatives Worth Knowing:</span>

**For Graphs/Plotting:**
- **Seaborn**: Provides a higher-level interface for drawing attractive and informative statistical graphics.
- **Plotly**: Offers interactive plots that can be embedded in web applications.
- **Bokeh**: Great for creating interactive and web-based visualizations.

**For Data Extraction/Reading Files:**
- **Polars**: A faster alternative for handling large datasets.
- **Dask**: Extends pandas for parallel computing and larger-than-memory datasets.

**For Data Analysis:**
- **scikit-learn**: For machine learning tasks.
- **statsmodels**: For statistical models and hypothesis tests.

## <span style="color:#689F38">Step 4: Setting Up VS Code</span>

### <span style="color:#03A9F4">Installing VS Code on Heriot-Watt University Computers</span>
VS Code can be installed through the Software Centre on Heriot-Watt University computers:
1. Open the Software Centre from the Start menu
2. Search for "VS Code" 
3. Click "Install" and wait for the installation to complete
4. Launch VS Code from the Start menu after installation

![VS Code in Software Centre](resources/images/software-centre-vscode.png)

### <span style="color:#03A9F4">Installing VS Code on Personal Computers</span>
For personal computers not managed by Heriot-Watt University:
1. Visit the [Visual Studio Code website](https://code.visualstudio.com/)
2. Download the appropriate installer for your operating system (Windows, macOS, or Linux)
3. Run the installer and follow the prompts
4. Launch VS Code after installation completes

### <span style="color:#03A9F4">What is an IDE?</span>
An Integrated Development Environment (IDE) combines a code editor, debugger, and other tools in one application. While you can write Python code in any text editor, IDEs provide features that make development easier and more efficient.

### <span style="color:#03A9F4">Why VS Code?</span>

- **GitHub Copilot Access**: VS Code allows seamless integration with GitHub Copilot, which is free for academic use. This AI assistant can dramatically speed up your coding by suggesting code completions.
- **Extensibility**: VS Code has a massive marketplace of extensions.
- **Lightweight but Powerful**: Unlike some IDEs, VS Code starts up quickly and runs smoothly while still offering powerful features.

While you could use other environments like PyCharm, Spyder, or Jupyter, VS Code offers the best combination of features for our research needs. That said, the skills you learn will transfer to other environments if you prefer them.

## <span style="color:#689F38">Step 5: Navigating VS Code</span>

When you first open VS Code, you'll see a welcome screen. Here are the key areas to be familiar with:

### <span style="color:#03A9F4">Activity Bar Functions</span>

The Activity Bar provides quick access to VS Code's main views:

- **Explorer**: Browse your project files and folders
- **Search**: Find text across your project
- **Source Control**: Manage Git repositories
- **Run and Debug**: Execute and troubleshoot your code
- **Extensions**: Install and manage VS Code add-ons

![Visual Studio Code Activity Bar](resources/images/activity-bar-vscode.png)

### <span style="color:#03A9F4">VS Code Interface</span>

- **Activity Bar**: The leftmost column with icons for different views
- **Side Bar**: Opens when you click an Activity Bar icon, showing files, extensions, etc.
- **Editor**: The main area where you'll write code
- **Status Bar**: At the bottom, showing information about your project

![VS Code Interface Overview](resources/images/vscode-interface-labelled.png)

## <span style="color:#689F38">Step 6: Installing Extensions</span>

### <span style="color:#03A9F4">Installing the Python Extensions Package</span>

To enhance your Python development experience in VS Code, you'll need to install the **Python extensions package**. Follow these steps:

1. Click the Extensions icon in the Activity Bar on the side of the window (or press `Ctrl+Shift+X`).
2. In the search box, type "Python" and look for the extension published by Microsoft.
3. Click the "Install" button to add the extension to your VS Code setup.

### <span style="color:#03A9F4">Recommended Extensions for Research</span>

Here are the essential extensions I recommend installing:

- **Python Language Support**: Provides syntax highlighting, code snippets, and other language-specific features.
- **Debugging**: Allows you to set breakpoints, inspect variables, and step through your code.
- **Linting**: Helps you maintain code quality by checking for errors and enforcing coding standards.
- **IntelliSense**: Offers intelligent code completions based on variable types, function definitions, and imported modules.
- **Jupyter Notebook Support**: Enables you to create and edit Jupyter Notebooks directly within VS Code.

After installing the Python extension, you may also want to install additional extensions to further enhance your workflow:

### <span style="color:#03A9F4">Additional Useful Extensions:</span>

**For Data Handling:**
- **"Rainbow CSV"**: Improves the readability of CSV files by highlighting columns in different colors.
- **"Excel Viewer"**: Allows you to view Excel files directly in VS Code.
- **"Data Wrangler"**: Simplifies data cleaning and transformation tasks.

**For Jupyter Notebooks:**
- **"Jupyter"**: Provides full support for Jupyter Notebooks within VS Code.
- **"Jupyter Keymap"**: Adds Jupyter-specific keybindings to VS Code.
- **"Jupyter Cell Tags"**: Enables tagging of Jupyter cells for better organization.

**For Python Development:**
- **"GitHub Copilot"**: Provides AI-assisted coding suggestions to speed up your development process.
- **"Python Indent"**: Automatically adjusts indentation levels for Python code, ensuring consistent formatting.

Once these extensions are installed, you can connect VS Code to your conda environment to ensure it uses the correct Python interpreter for your projects.

## <span style="color:#689F38">Step 7: Connecting VS Code to Your Conda Environment</span>

To connect VS Code to your conda environment, you need to select the appropriate Python interpreter:

### <span style="color:#03A9F4">Selecting Your Python Interpreter</span>

#### Option 1: Using the Command Palette
1. Open VS Code
2. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS) to open the Command Palette
3. Type "Python: Select Interpreter" and select it
4. Choose your "research-env" environment from the list

#### Option 2: Using the Status Bar
1. Look at the status bar at the bottom of the VS Code window
2. Find where it shows the Python version or "Select Python Interpreter"
3. Click on this area to select your "research-env" environment

#### Option 3: Using the Python Icon in Activity Bar
1. Click on the Python icon in the Activity Bar (left side of VS Code)
2. In the "INTERPRETER" section, click on the current interpreter or "Select Python Interpreter"
3. Choose your "research-env" environment from the dropdown list

You should now see the environment name in the status bar (bottom right corner). 
VS Code will use this environment when running Python code.

To verify everything is working:

Create a new file (Ctrl+N)
Save it as "test.py" (Ctrl+S)

Add this code:
```python
# Import Python Packages
import numpy as np                  # NumPy is used for numerical operations and arrays
import pandas as pd                 # Pandas is used for data manipulation and analysis
import matplotlib.pyplot as plt     # Matplotlib is used for creating visualizations

# Print version information to confirm successful installation
print("NumPy version:", np.__version__)
print("Pandas version:", pd.__version__)
print("Everything is working!")

# If you see the version numbers printed without errors,
# your Python environment is correctly set up!
```
Run the file by clicking the play button in the top right or right-clicking and selecting "Run Python File in Terminal"

If you see version information and "Everything is working!" without errors, congratulations! Your Python environment is set up correctly.

## <span style="color:#689F38">Next Steps</span>
Now that you have your environment set up, proceed to Part 2.
