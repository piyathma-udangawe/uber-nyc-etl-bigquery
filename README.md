# Uber NYC ETL Pipeline — BigQuery

## Overview
End-to-end ETL pipeline that extracts, transforms, and loads 
1M+ Uber NYC trip records using Python and Google BigQuery.

## Architecture
Raw CSV → BigQuery (raw_trips) → Python ETL → BigQuery (transformed_trips)

## Tech Stack
- Python 3
- Google BigQuery
- Pandas
- pandas-gbq
- Google Cloud SDK

## What It Does
- Extracts 1M+ Uber trip records from BigQuery
- Transforms timestamps into time categories (Morning, Afternoon, Evening, Night)
- Loads cleaned data back to BigQuery as a new table

## Key Findings
| Time Category | Total Trips |
|---|---|
| Evening | 282,061 |
| Afternoon | 266,321 |
| Night | 243,659 |
| Morning | 236,095 |

Evening is the busiest time for Uber in NYC.

## How to Run
1. Set up GCP project and BigQuery dataset
2. Install dependencies:
   pip install google-cloud-bigquery pandas pandas-gbq
3. Authenticate:
   gcloud auth application-default login
4. Run:
   python etl.py

## Dataset
Uber NYC Raw Trip Data — September 2014
Source: FiveThirtyEight GitHub
