## <span style="color:#9575CD">Part 2: Data Extraction and Processing</span>

## Table of Contents
- [Python Code Organization](#python-code-organization)
    - [Python Files and Modules](#python-files-and-modules)
    - [Basic Structure of a Python Script](#basic-structure-of-a-python-script)
- [Example 1: Reading CSV Files](#example-1-reading-csv-files)
- [Example 2: Reading Excel Files](#example-2-reading-excel-files)
- [Example 3: Web Scraping](#example-3-web-scraping)
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

def read_excel_file(file_path):
    data = pd.read_excel(file_path)
    print(data.head())  # Display the first few rows of the dataframe
    return data

if __name__ == "__main__":
    data = read_excel_file("data/sample.xlsx")
```

## <span style="color:#689F38">Example 3: Web Scraping</span>

Web scraping allows you to extract data from websites. Here's a simple example using BeautifulSoup:

```python
import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    titles = soup.find_all('h2')
    for title in titles:
        print(title.get_text())

if __name__ == "__main__":
    scrape_website("https://example.com")
```

## <span style="color:#689F38">Next Steps</span>

Now that you have learned how to extract data from various sources, proceed to Part 3: Data Cleaning and Transformation to learn how to prepare your data for analysis.
