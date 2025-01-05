import pandas as pd
import numpy as np

# Define the AQI ranges based on the provided table
ranges = {
    "Good": (0, 12, 0, 54),
    "Moderate": (12.1, 35.4, 55, 154),
    "Unhealthy for Sensitive Groups": (35.5, 55.4, 155, 254),
    "Unhealthy": (55.5, 150.4, 255, 354),
    "Very Unhealthy": (150.5, 250.4, 355, 424),
    "Hazardous": (250.5, 500, 425, 604)
}

# Helper function to generate realistic PM2.5 and PM10 values
def generate_values(category, size=100):
    pm25_min, pm25_max, pm10_min, pm10_max = ranges[category]
    pm25_values = np.random.uniform(pm25_min, pm25_max, size)
    pm10_values = np.random.uniform(pm10_min, pm10_max, size)
    return pm25_values, pm10_values

# Generate datasets simulating two sensors measuring at the same location
np.random.seed(42)

# First dataset: Normal sensor values
pm25_normal, pm10_normal = generate_values("Moderate", size=200)
df1 = pd.DataFrame({"PM25": pm25_normal, "PM10": pm10_normal})

# Second dataset: High-end sensor values (adding slight variations to simulate precision)
pm25_high_end = pm25_normal + np.random.normal(0, 10, 200)
pm10_high_end = pm10_normal + np.random.normal(0, 10, 200)
df2 = pd.DataFrame({"PM25": pm25_high_end, "PM10": pm10_high_end})

# Save datasets to CSV files
df1.to_csv("datasets/dataset.csv", index=False)
df2.to_csv("datasets/high_dataset.csv", index=False)

print("Datasets have been generated and saved as 'dataset.csv' and 'high_dataset.csv'.")
