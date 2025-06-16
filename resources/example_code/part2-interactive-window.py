# %% [markdown]
# # Exercise 0: Notebook Cells and Notation
# 
# In Jupyter notebooks or VS Code Interactive Window:
# 
# - `# %%` or `#%%` starts a new code cell
# - `# %% [markdown]` starts a markdown cell
# - In markdown cells, use `#` for headers, `*text*` for italic, `**text**` for bold
# - Use `$formula$` for inline math or `$$formula$$` for display math
# - For code comments, use `#` as usual

# %% [markdown]
# ## Markdown Examples
# 
# This is regular text in a markdown cell.
# 
# ### Text Formatting
# - *Italic text* using single asterisks
# - **Bold text** using double asterisks
# - ***Bold and italic*** using triple asterisks
# 
# ### Math Formulas
# - Uses latex syntax for mathematical expressions
# - Inline formula: The Pythagorean theorem is $a^2 + b^2 = c^2$
# - Display formula:
# $$E = mc^2$$
# $$\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$$

# %%
# Exercise 1: Loading Data
import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset
data = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# Display the first few rows
print("First 5 rows of the dataset:")
print(data.head())

# %%
# Exercise 2: Basic Data Visualization
# Create a simple bar chart
plt.figure(figsize=(8, 6))
survived_counts = data['Survived'].value_counts()
plt.bar(['Did not survive (0)', 'Survived (1)'], survived_counts.values)
plt.title('Survival Count')
plt.ylabel('Number of Passengers')
plt.show()

# Create a simple histogram
plt.figure(figsize=(8, 6))
plt.hist(data['Age'].dropna(), bins=10)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Number of Passengers')
plt.show()

# %%
# Exercise 3: More Simple Visualizations
# Create a bar chart for passenger classes
plt.figure(figsize=(8, 6))
class_counts = data['Pclass'].value_counts().sort_index()
plt.bar(['1st Class', '2nd Class', '3rd Class'], class_counts.values)
plt.title('Passenger Class Count')
plt.ylabel('Number of Passengers')
plt.show()

# Create a bar chart for gender
plt.figure(figsize=(8, 6))
gender_counts = data['Sex'].value_counts()
plt.bar(gender_counts.index, gender_counts.values)
plt.title('Gender Count')
plt.ylabel('Number of Passengers')
plt.show()

# %%
# Exercise 4: Viewing Tabular Data
# Print basic information about the dataset
print("\nTotal number of passengers:", len(data))
print("Number of survivors:", data['Survived'].sum())
print("Survival rate:", round(data['Survived'].mean() * 100, 1), "%")

# Print average age and fare
print("\nAverage age:", round(data['Age'].mean(), 1), "years")
print("Average fare:", round(data['Fare'].mean(), 2), "$")

# Create a simple table of survival by class
print("\nSurvival count by passenger class:")
survival_table = pd.crosstab(data['Pclass'], data['Survived'])
survival_table.columns = ['Did not survive', 'Survived']
print(survival_table)

# Create a simple table of survival by gender
print("\nSurvival count by gender:")
gender_table = pd.crosstab(data['Sex'], data['Survived'])
gender_table.columns = ['Did not survive', 'Survived']
print(gender_table)
