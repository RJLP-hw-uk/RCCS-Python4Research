## <span style="color:#9575CD">Part 2: Data Extraction and Processing</span>

## Table of Contents
- [Python Code Organization](#python-code-organization)
    - [Python Files and Modules](#python-files-and-modules)
    - [Basic Structure of a Python Script](#basic-structure-of-a-python-script)
- [Common Steps to Handling Data](#common-steps-to-handling-data)
    - [Knowing Your Data Format](#knowing-your-data-format)
    - [Pulling Your Data into Python](#pulling-your-data-into-python)
    - [Filtering and Cleaning Your Data](#filtering-and-cleaning-your-data)
    - [Saving Your Clean Data](#saving-your-clean-data)
- [Example 1: Reading CSV Files](#example-1-reading-csv-files)
- [Example 2: Reading Excel Files](#example-2-reading-excel-files)
- [Next Steps](#next-steps)

## <span style="color:#689F38">Python Code Organization</span>

Before diving into data extraction, let's understand how Python code is typically organized.

### <span style="color:#03A9F4">Python Files and Modules</span>

- **Script (.py file)**: A standalone Python file that can be executed.
- **Module**: A Python file containing functions, classes, and variables that can be imported.
- **Package**: A directory containing multiple modules and a special `__init__.py` file.

### <span style="color:#03A9F4">Basic Structure of a Python Script</span>

```python
# 1. Import statements
import numpy as np
import pandas as pd
import os

# 2. Constants and configuration
DATA_DIR = "data/"
OUTPUT_FILE = "results.csv"

# 3. Function definitions
def process_data(filename):
    # Function implementation
    pass

# 4. Main execution (often in a main function or under if __name__ == "__main__":)
if __name__ == "__main__":
    # Script execution starts here
    data = process_data(DATA_DIR + "input.csv")
    # More code...
```

## <span style="color:#689F38">Common Steps to Handling Data</span>

### <span style="color:#03A9F4">Knowing Your Data Format</span>

Understanding the format of your data is crucial. Common formats include CSV, Excel, JSON, and SQL databases. Tools like Microsoft Excel, Google Sheets, and text editors can help you inspect the data.

### <span style="color:#03A9F4">Pulling Your Data into Python</span>

Use libraries like `pandas` to read data into Python. For example:
```python
import pandas as pd

# Reading a CSV file
csv_data = pd.read_csv("data/sample.csv")

# Reading an Excel file
excel_data = pd.read_excel("data/sample.xlsx", sheet_name="Sheet1")
```

### <span style="color:#03A9F4">Filtering and Cleaning Your Data</span>

Cleaning data involves handling missing values, removing duplicates, and filtering rows/columns. Methods include:
- Dropping missing values: `data.dropna()`
- Filling missing values: `data.fillna(value)`
- Filtering rows: `data[data['column'] > value]`

### <span style="color:#03A9F4">Saving Your Clean Data</span>

After cleaning, save your data back to a file:
```python
# Saving to CSV
data.to_csv("data/cleaned_data.csv", index=False)

# Saving to Excel
data.to_excel("data/cleaned_data.xlsx", index=False)
```

## <span style="color:#689F38">Example 1: Reading CSV Files</span>

Reading CSV files is a common task in data extraction. Here's how you can do it using pandas:

```python
import pandas as pd

def read_csv_file(file_path):
    data = pd.read_csv(file_path)
    print(data.head())  # Display the first few rows of the dataframe
    return data

if __name__ == "__main__":
    data = read_csv_file("data/sample.csv")
```

## <span style="color:#689F38">Example 2: Reading Excel Files</span>

You can also read Excel files using pandas:

```python
import pandas as pd

def read_excel_file(file_path, sheet_name="Sheet1"):
    data = pd.read_excel(file_path, sheet_name=sheet_name)
    print(data.head())  # Display the first few rows of the dataframe
    return data

if __name__ == "__main__":
    data = read_excel_file("data/sample.xlsx")
```

### <span style="color:#03A9F4">Pulling Data from Specific Cells, Ranges, and Sheets</span>

```python
# Reading a specific cell
cell_value = excel_data.at[0, 'ColumnName']

# Reading a range of cells
range_data = excel_data.loc[0:10, 'ColumnName']

# Reading multiple sheets
sheet1 = pd.read_excel("data/sample.xlsx", sheet_name="Sheet1")
sheet2 = pd.read_excel("data/sample.xlsx", sheet_name="Sheet2")
```

### <span style="color:#03A9F4">Filtering Data</span>

```python
# Filtering by row/heading
filtered_data = data[data['column'] > value]

# Using functions and loops
filtered_data = data[data['column'].apply(lambda x: x.startswith('prefix'))]

# String extraction
filtered_data = data[data['column'].str.contains('substring')]
```

## <span style="color:#689F38">Next Steps</span>

Now that you have learned how to extract data from various sources, proceed to Part 3: Data Cleaning and Transformation to learn how to prepare your data for analysis.
