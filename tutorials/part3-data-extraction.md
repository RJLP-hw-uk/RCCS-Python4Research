## <span style="color:#9575CD">Part 3: Data Extraction and Processing</span>

## Table of Contents
- [Common Steps to Handling Data](#common-steps-to-handling-data)
    - [Step 1: Knowing Your Data Format](#step-1-knowing-your-data-format)
    - [Step 2: Pulling Your Data into Python](#step-2-pulling-your-data-into-python)
    - [Step 3: Filtering, Cleaning, and Manipulating Your Data](#step-3-filtering-cleaning-and-manipulating-your-data)
    - [Step 4: Saving Your Clean Data](#step-4-saving-your-clean-data)
- [Example 1: Reading CSV Files](#example-1-reading-csv-files)
- [Example 2: Reading Excel Files](#example-2-reading-excel-files)
    - [Using Pandas for Excel](#using-pandas-for-excel)
    - [Using xlwings for Excel](#using-xlwings-for-excel)
    - [Using openpyxl for Excel](#using-openpyxl-for-excel)
- [Next Steps](#next-steps)

## <span style="color:#689F38">Common Steps to Handling Data</span>

### <span style="color:#03A9F4">Step 1: Knowing Your Data Format</span>

Understanding the format of your data is crucial. Common formats include CSV, Excel, JSON, and SQL databases. Tools like Microsoft Excel, Google Sheets, and text editors can help you inspect the data.

### <span style="color:#03A9F4">Step 2: Pulling Your Data into Python</span>

Use libraries like `pandas` to read data into Python. For example:
```python
import pandas as pd

# Reading a CSV file
csv_data = pd.read_csv("data/sample.csv")

# Reading an Excel file - Here we added an additional argument to specify 'which' excel sheet to read from
excel_data = pd.read_excel("data/sample.xlsx", sheet_name="Sheet1")
```
### <span style="color:#03A9F4">Step 3: Filtering, Cleaning, and Manipulating Your Data</span>

Cleaning data involves handling missing values, removing duplicates, and filtering rows/columns. Methods include:
```python
# Handling missing values
data_cleaned = data.dropna()  # Remove rows with any missing values (NA)
data_filled = data.fillna(0)  # Fill missing values (NA) with 0

# Filtering rows based on conditions
filtered_data = data[data['y'] > 100]  # Keep only rows where 'y' > 100

# Removing duplicate rows
unique_data = data.drop_duplicates()  # Remove all duplicate rows
unique_subset = data.drop_duplicates(subset=['y1', 'y2'])  # Remove duplicates based on specific columns
```

Data manipulation extends beyond basic cleaning:

```python
# Using pandas for advanced transformations
# Applying mathematical operations
data['new_column'] = data['column_a'] + data['column_b']

# String manipulations
data['lowercase'] = data['text_column'].str.lower()
data['extracted'] = data['text_column'].str.extract(r'(\d+)')

# Grouping and aggregating
grouped_data = data.groupby('category').agg({'value': ['mean', 'sum', 'count']})

# Applying custom functions
data['custom'] = data['column'].apply(lambda x: x*2 if x > 0 else 0)
```

Other libraries for specialized manipulation:

```python
# NumPy for numerical operations - Manual normalization
import numpy as np
data['normalized'] = (data['value'] - np.mean(data['value'])) / np.std(data['value'])

# SciPy for scientific computing - Z-score standardization
from scipy import stats
data['z_score'] = stats.zscore(data['value'])

# Scikit-learn for preprocessing - Min-Max scaling
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
data['scaled'] = scaler.fit_transform(data[['value']])
```

### <span style="color:#03A9F4">Step 4: Saving Your Clean Data</span>

After cleaning, save your data back to a file:
```python
# Saving to CSV
data.to_csv("data/cleaned_data.csv", index=False)

# Saving to Excel
data.to_excel("data/cleaned_data.xlsx", index=False)

# Setting index=False removes the auto-generated pandas indices from the output.
# This is typically preferred for cleaned data files to avoid confusion.

```

## <span style="color:#689F38">Example 1: Reading CSV Files</span>

Pandas offers powerful functionality for data handling beyond basic reading:

```python
import pandas as pd
import numpy as np

# Basic CSV reading
data = pd.read_csv("data/sample.csv")

# Reading with advanced options
df = pd.read_csv("data/sample.csv", 
                skiprows=2,                 # Skip first 2 rows
                usecols=["col1", "col2"],   # Read only specific columns
                nrows=1000,                 # Limit number of rows
                na_values=["NA", "N/A"],    # Custom NA values
                )                 

# Memory efficient reading for large files
chunks = pd.read_csv("data/large_file.csv", chunksize=10000)
for chunk in chunks:
    # Process each chunk
    processed_chunk = chunk.some_operation()
    # Do something with processed_chunk

# Time series data with proper date parsing
ts_data = pd.read_csv("data/timeseries.csv",
                     parse_dates=["date_column"],
                     index_col="date_column")

# Filtering by a condition
filtered_data = data[data['column'] > value]

# Using functions for more complex filtering
filtered_data = data[data['column'].apply(lambda x: x.startswith('prefix'))]

# String extraction
filtered_data = data[data['column'].str.contains('substring')]
```

## <span style="color:#689F38">Example 2: Reading Excel Files</span>

### <span style="color:#03A9F4">Using Pandas for Excel</span>

```python
import pandas as pd

# Reading an Excel file
excel_data = pd.read_excel("data/sample.xlsx", sheet_name="Sheet1")

# Reading a specific cell
cell_value = excel_data.at[0, 'ColumnName']

# Reading a range of cells
range_data = excel_data.loc[0:10, 'ColumnName']

# Reading multiple sheets
sheet1 = pd.read_excel("data/sample.xlsx", sheet_name="Sheet1")
sheet2 = pd.read_excel("data/sample.xlsx", sheet_name="Sheet2")
```

### <span style="color:#03A9F4">Using xlwings for Excel</span>

While pandas is excellent for data analysis, specialized libraries offer more control for Excel interactions:

```python
# xlwings provides direct access to Excel files with more control
import xlwings as xw

# Open an Excel file
wb = xw.Book("data/sample.xlsx")  
sheet = wb.sheets["Sheet1"]

# Read specific ranges with native Excel references
data_range = sheet.range("A1:D10").value  # Returns a list of lists
cell_value = sheet.range("A1").value

# Read named ranges
named_range = sheet.range("NamedRange").value

# Dynamic interaction with Excel (works with Excel running)
sheet.range("E1").value = "New Value"  # Write data
sheet.range("A1:A10").color = (255, 0, 0)  # Format cells
wb.save()
```

Benefits of xlwings over pandas:
- Two-way communication (read/write while Excel is running)
- Automate Excel with Python without losing Excel's interface benefits
- Direct interaction with open Excel files
- Preserves Excel formatting and formulas
- Access to Excel's calculation engine

### <span style="color:#03A9F4">Using openpyxl for Excel</span>

openpyxl provides detailed control over Excel files at a lower level:

```python
# openpyxl for granular control over Excel files
import openpyxl

# Load the workbook and select the sheet
wb = openpyxl.load_workbook("data/sample.xlsx")
sheet = wb["Sheet1"]

# Read cell values
cell_value = sheet["A1"].value
cell_value_alt = sheet.cell(row=1, column=1).value

# Read a range into a list of tuples
data = []
for row in sheet["A1:C10"]:
    row_data = [cell.value for cell in row]
    data.append(row_data)
    
# Edit cell properties
sheet["A1"].value = "New Header"
sheet["A1"].font = openpyxl.styles.Font(bold=True, color="FF0000")
sheet["A1"].fill = openpyxl.styles.PatternFill(start_color="FFFF00", fill_type="solid")

# Save the modified workbook
wb.save("data/modified_sample.xlsx")
```

Benefits of openpyxl over pandas:
- Detailed control over Excel's formatting features
- Cell-by-cell manipulation of styles, formulas, and content
- Create Excel files with complex formatting from scratch
- Access to Excel features like charts, comments, and named ranges
- No dependency on Excel installation (unlike xlwings)
- Great for generating professional reports and templates

## <span style="color:#689F38">Next Steps</span>

Now that you have learned how to extract data from various sources, proceed to Part 3: Data Cleaning and Transformation to learn how to prepare your data for analysis.
