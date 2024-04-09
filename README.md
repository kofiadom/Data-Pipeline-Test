
## Newmont Ahafo South Mines Data Analysis Project

**Contributor:** Kofi Adom

**License:** MIT License (refer to [https://opensource.org/license/mit](https://opensource.org/license/mit)) for details.

## Overview

This project involves generating synthetic data for the Newmont Ahafo South Mines dataset, ingesting this data into a PostgreSQL database using Docker, and performing data analysis using DBeaver.

## Project Components

1. **Virtual Environment Setup**:
  - Created a virtual environment to manage project dependencies.

2. **Docker and PostgreSQL Setup**:
  - Downloaded Docker to manage containers.
  - Utilized a `docker-compose.yml` file to set up a PostgreSQL service.

3. **Data Generation**:
  - Used `newmont_ahafo_data_generator.py` to create a synthetic dataset for Newmont Ahafo South Mines.

4. **Data Ingestion**:
  - Utilized `ingest_data.py` to ingest the generated data into the PostgreSQL database.

5. **Database Management**:
  - Connected to the PostgreSQL database using DBeaver to manage and query the data.

6. **Analysis and Querying**:
  - Ran SQL queries on the ingested dataset using DBeaver to extract meaningful insights.

## Files Included

- `newmont_ahafo_data_generator.py`: Python script to generate synthetic data for the Newmont Ahafo South Mines dataset.
- `ingest_data.py`: Python script to ingest the generated data into the PostgreSQL database.
- `docker-compose.yml`: Docker Compose file to set up the PostgreSQL service.
- `queries.sql`: SQL file containing sample queries to run on the dataset.
- `requirements.txt`: File listing the project's Python dependencies.

## Instructions for Use

1. **Environment Setup**:
  - Ensure Python and Docker are installed.
  - Create and activate a virtual environment.

2. **Start the Docker Engine**

3. **Run docker-compose file**:
- Run `docker-compose up --build` to start the PostgreSQL service, install dependencies, generate the data and ingest it into PostgreSQL.

4. **Queries**:
  - Connect to the PostgreSQL database using DBeaver.
  - Run SQL queries from `queries.sql` to analyze the dataset.

## Conclusion

This project demonstrates how to generate synthetic data, ingest it into a PostgreSQL database, and perform data analysis using Docker, Python, and DBeaver. The generated dataset can be used for further analysis and decision-making processes.


