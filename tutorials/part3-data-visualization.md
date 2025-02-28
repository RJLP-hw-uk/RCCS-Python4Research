# <span style="color:#9575CD">Part 3: Data Visualization</span>

## Table of Contents
- [Reference Materials](#reference-materials)
- [Basic Line Graphs](#basic-line-graphs)
- [Creating Effective Visualizations](#creating-effective-visualizations)
    - [Visualization Taxonomy](#visualization-taxonomy)
    - [Elements of Beautiful Graphs](#elements-of-beautiful-graphs)
    - [Good vs. Bad Visualization Examples](#good-vs-bad-visualization-examples)

## <span style="color:#689F38">Reference Materials</span>

Before we begin, it's worth noting that there are excellent cheat sheets available in the `plotting` directory. These resources provide quick references for common plotting tasks.

## <span style="color:#689F38">Basic Line Graphs</span>

Let's start with the simplest form of visualization - a line graph:

```python
import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(8, 4))

# Plot the line
ax.plot(x, y, 'b-', linewidth=2)

# Add labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Simple Sine Wave')

# Add grid
ax.grid(True, linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()
```

## <span style="color:#689F38">Creating Effective Visualizations</span>

### <span style="color:#03A9F4">Visualization Taxonomy</span>

When creating visualizations, it's important to choose the right type:

- **Line plots**: For trends over time or continuous variables
- **Scatter plots**: For relationships between two variables
- **Bar plots**: For comparing categories
- **Histograms**: For distribution of a single variable
- **Box plots**: For statistical summaries of distributions
- **Heatmaps**: For matrix data and correlations
- **3D plots**: For relationships between three variables

### <span style="color:#03A9F4">Elements of Beautiful Graphs</span>

Well-designed graphs share several key elements:

1. **Clear purpose**: The visualization answers a specific question
2. **Appropriate type**: The chart type matches the data relationship
3. **Minimalist design**: Remove unnecessary elements (chartjunk)
4. **Effective use of color**: Purposeful, accessible color schemes
5. **Proper labeling**: Clear axes labels, titles, and legends
6. **Consistent formatting**: Fonts, sizes, and styles remain uniform
7. **Appropriate scale**: Axis scaling that doesn't distort the data
8. **Data-ink ratio**: Maximize the ink used for actual data representation

### <span style="color:#03A9F4">Good vs. Bad Visualization Examples</span>

#### Poor Visualization Example:

```python
# Example of a poor visualization
fig, ax = plt.subplots(figsize=(10, 6))
x = np.arange(5)
y = [2, 5, 1, 7, 3]

ax.bar(x, y, color='red')
ax.set_title('DATA VISUALIZATION')
# No labels, inappropriate colors, missing grid
plt.show()
```

#### Improved Visualization:

```python
# Example of an improved visualization
fig, ax = plt.subplots(figsize=(8, 5))
categories = ['A', 'B', 'C', 'D', 'E']
values = [2, 5, 1, 7, 3]

bars = ax.bar(categories, values, color='#5975A4', alpha=0.8)
ax.set_title('Comparison Across Categories', fontsize=14)
ax.set_xlabel('Category', fontsize=12)
ax.set_ylabel('Value', fontsize=12)

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{height}', ha='center', va='bottom')

# Add subtle grid for reference
ax.grid(axis='y', linestyle='--', alpha=0.2)

