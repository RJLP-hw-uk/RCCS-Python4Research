## <span style="color:#9575CD">Part 2: Data Extraction and Processing</span>

## Table of Contents
- [Common Steps to Handling Data](#common-steps-to-handling-data)
    - [Step 1: Knowing Your Data Format](#knowing-your-data-format)
    - [Step 2: Pulling Your Data into Python](#pulling-your-data-into-python)
    - [Step 3: Filtering and Cleaning Your Data](#filtering-and-cleaning-your-data)
    - [Step 4: Saving Your Clean Data](#saving-your-clean-data)
- [Example 1: Reading CSV Files](#example-1-reading-csv-files)
- [Example 2: Reading Excel Files](#example-2-reading-excel-files)
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

# Saving to CSV
data.to_csv("data/cleaned_data.csv", index=False)

# Saving to Excel
data.to_excel("data/cleaned_data.xlsx", index=False)

# Setting index=False removes the auto-generated pandas indices from the output.
# This is typically preferred for cleaned data files to avoid confusion.

```

## <span style="color:#689F38">Example 1: Advanced Pandas Usage</span>

Pandas offers powerful functionality for data handling beyond basic reading:

```python
import pandas as pd
import numpy as np

# Reading with advanced options
df = pd.read_csv("data/sample.csv", 
                skiprows=2,              # Skip first 2 rows
                na_values=["NA", "N/A"], # Custom NA values
                usecols=["col1", "col2"],# Read only specific columns
                nrows=1000)              # Limit number of rows

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

# Reshaping data
# Wide to long format
long_df = pd.melt(df, 
                 id_vars=["id_column"],
                 value_vars=["var1", "var2"],
                 var_name="variable",
                 value_name="value")

# Pivot tables
pivot_df = df.pivot_table(values="value_col", 
                         index="row_categories",
                         columns="col_categories",
                         aggfunc=np.mean)

# SQL-like joins
merged_df = pd.merge(df1, df2, 
                    on="key_column",     # For single key
                    # left_on="df1_key", # For different column names
                    # right_on="df2_key",
                    how="inner")         # inner, outer, left, right
```

## <span style="color:#689F38">Example 2: Other Data Handling Libraries</span>

While pandas is versatile, specialized libraries can enhance your data workflow:

```python
# NumPy for numerical operations
import numpy as np
array = np.array([[1, 2, 3], [4, 5, 6]])
np_mean = np.mean(array, axis=0)     # Column means
np_filtered = array[array > 2]       # Boolean indexing

# Dask for larger-than-memory datasets
import dask.dataframe as dd
dask_df = dd.read_csv("data/huge_data_*.csv")  # Can handle multiple files
result = dask_df.groupby('column').mean().compute()  # Lazy evaluation until compute()

# Polars for fast DataFrame operations
import polars as pl
pl_df = pl.read_csv("data/sample.csv")
filtered = pl_df.filter(pl.col("value") > 100).groupby("category").agg(pl.sum("amount"))

# PyArrow for efficient data processing
import pyarrow as pa
import pyarrow.csv as csv
table = csv.read_csv("data/sample.csv")
filtered_table = table.filter(pa.compute.greater(table["value"], 100))

# SQLAlchemy for database interactions
from sqlalchemy import create_engine
engine = create_engine('sqlite:///data.db')
sql_df = pd.read_sql("SELECT * FROM table", engine)
sql_df.to_sql("new_table", engine, if_exists="replace")
```

### <span style="color:#03A9F4">Pulling Data from Specific Cells, Ranges, and Sheets</span>

```python
import pandas as pd

# Reading an Excel file
excel_data = pd.read_excel("data/sample.xlsx")

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
import pandas as pd

# Load a sample dataset
data = pd.read_csv("data/sample.csv")

# Filtering by a condition
filtered_data = data[data['column'] > value]

# Using functions for more complex filtering
filtered_data = data[data['column'].apply(lambda x: x.startswith('prefix'))]

# String extraction
filtered_data = data[data['column'].str.contains('substring')]
```

## <span style="color:#689F38">Next Steps</span>

Now that you have learned how to extract data from various sources, proceed to Part 3: Data Cleaning and Transformation to learn how to prepare your data for analysis.
