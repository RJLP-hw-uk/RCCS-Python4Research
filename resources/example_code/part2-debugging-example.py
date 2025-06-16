"""
Debug Example: Temperature Analysis
This file contains deliberate issues to practice debugging
"""

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    # BUG: Incorrect formula (missing parentheses)
    return fahrenheit - 32 * 5/9  # Should be: (fahrenheit - 32) * 5/9

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    # BUG: Doesn't check for negative Kelvin values (physically impossible)
    return kelvin - 273.15

def calculate_statistics(temperatures):
    """Calculate basic statistics for temperature data."""
    stats = {
        'mean': np.mean(temperatures),
        'median': np.median(temperatures),
        'std_dev': np.std(temperatures),
        'min': np.min(temperatures),
        'max': np.max(temperatures)
    }
    
    # BUG: Incorrect calculation of temperature range
    stats['range'] = stats['max'] + stats['min']  # Should be: max - min
    
    return stats

def analyze_temperature_data(dates, temperatures, location="Research Station"):
    """Analyze and visualize temperature trends."""
    # Find indices of min and max temperatures
    # BUG: Off-by-one error in loop
    min_temp_idx = 0
    max_temp_idx = 0
    for i in range(1, len(temperatures)):
        if temperatures[i] < temperatures[min_temp_idx]:
            min_temp_idx = i
        if temperatures[i] > temperatures[max_temp_idx]:
            max_temp_idx = i
    
    # Calculate statistics
    stats = calculate_statistics(temperatures)
    
    # Print analysis results
    print(f"Temperature Analysis for {location}")
    print(f"Mean temperature: {stats['mean']:.2f}°C")
    print(f"Median temperature: {stats['median']:.2f}°C")
    print(f"Standard deviation: {stats['std_dev']:.2f}°C")
    print(f"Min temperature: {temperatures[min_temp_idx]:.2f}°C on {dates[min_temp_idx]}")
    print(f"Max temperature: {temperatures[max_temp_idx]:.2f}°C on {dates[max_temp_idx]}")
    
    # Visualization
    plt.figure(figsize=(10, 6))
    plt.plot(dates, temperatures, 'b-')
    plt.scatter(dates[min_temp_idx], temperatures[min_temp_idx], color='blue', s=100, 
                label=f'Min: {temperatures[min_temp_idx]:.1f}°C')
    plt.scatter(dates[max_temp_idx], temperatures[max_temp_idx], color='red', s=100, 
                label=f'Max: {temperatures[max_temp_idx]:.1f}°C')
    plt.axhline(y=stats['mean'], color='green', linestyle='--', 
                label=f'Mean: {stats['mean']:.1f}°C')
    
    plt.title(f'Temperature Variation: {location}')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.grid(True)
    
    return stats

def main():
    # Generate sample data: 30 days of temperatures
    np.random.seed(42)  # For reproducibility
    start_date = datetime(2023, 6, 1)
    dates = [start_date + timedelta(days=i) for i in range(30)]
    
    # Generate temperatures in Fahrenheit
    temperatures_f = np.random.normal(75, 8, size=len(dates))
    
    # Convert to Celsius for analysis
    # BUG: Using the faulty conversion function
    temperatures_c = [fahrenheit_to_celsius(temp) for temp in temperatures_f]
    
    try:
        # BUG: TypeError will occur here due to the range calculation bug
        stats = analyze_temperature_data(dates, temperatures_c, "Research Station Alpha")
        
        # Print temperature range
        # BUG: Key error will occur if the previous error is fixed
        print(f"Temperature range: {stats['temperature_range']:.2f}°C")  # Should use 'range'
        
    except Exception as e:
        # This will catch errors but won't help us understand where they occur
        print(f"Error in analysis: {str(e)}")

if __name__ == "__main__":
    main()
