from google.cloud import bigquery
import pandas as pd

# Connect to BigQuery
client = bigquery.Client(project="datalab-2026")

print("✅ Connected to BigQuery!")

# Extract - Read raw data
query = """
    SELECT
        Date_Time,
        EXTRACT(HOUR FROM Date_Time) AS hour,
        EXTRACT(DAYOFWEEK FROM Date_Time) AS day_of_week,
        EXTRACT(MONTH FROM Date_Time) AS month,
        Lat,
        Lon,
        Base
    FROM `datalab-2026.uber_analysis.raw_trips`
"""

print("⏳ Extracting data...")
df = client.query(query).to_dataframe()
print(f"✅ Extracted {len(df)} rows!")

# Transform - Add a time category column
def get_time_category(hour):
    if 6 <= hour < 12:
        return "Morning"
    elif 12 <= hour < 17:
        return "Afternoon"
    elif 17 <= hour < 21:
        return "Evening"
    else:
        return "Night"

print("⏳ Transforming data...")
df["time_category"] = df["hour"].apply(get_time_category)
print("✅ Transformation complete!")
print(df.head())

# Load - Write back to BigQuery as a new table
print("⏳ Loading to BigQuery...")
destination = "datalab-2026.uber_analysis.transformed_trips"
df.to_gbq(destination, project_id="datalab-2026", if_exists="replace")
print("✅ Data loaded to BigQuery!")
print("🎉 ETL Pipeline Complete!")