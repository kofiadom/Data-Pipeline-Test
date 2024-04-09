import psycopg2
import pandas as pd

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname='newmont_ahafo_database',
    user='username',
    password='my_password',
    host='postgres'
)
cur = conn.cursor()

# Define the CREATE TABLE statement
create_table_query = '''
CREATE TABLE IF NOT EXISTS newmont_ahafo_south_mine_dataset (
    Date DATE,
    Shift VARCHAR(50),
    Employee_ID VARCHAR(50),
    Employee_Name VARCHAR(255),
    Department VARCHAR(50),
    Job_Title VARCHAR(50),
    Location VARCHAR(50),
    Equipment_ID VARCHAR(50),
    Equipment_Type VARCHAR(50),
    Equipment_Status VARCHAR(50),
    Production_Tonnage FLOAT,
    Maintenance_Cost FLOAT,
    Safety_Incident VARCHAR(3),
    Environmental_Incident VARCHAR(3),
    Community_Relations VARCHAR(50),
    Gold_Price FLOAT,
    Production_Cost FLOAT,
    Revenue FLOAT,
    Profit FLOAT
);
'''

# Execute the CREATE TABLE statement
cur.execute(create_table_query)

# Read the CSV file
df = pd.read_csv('newmont_ahafo_south_mine_dataset.csv')

# Insert the data into the PostgreSQL database
for index, row in df.iterrows():
    cur.execute(
        "INSERT INTO newmont_ahafo_south_mine_dataset (Date, Shift, Employee_ID, Employee_Name, Department, Job_Title, Location, Equipment_ID, Equipment_Type, Equipment_Status, Production_Tonnage, Maintenance_Cost, Safety_Incident, Environmental_Incident, Community_Relations, Gold_Price, Production_Cost, Revenue, Profit) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (row['Date'], row['Shift'], row['Employee_ID'], row['Employee_Name'], row['Department'], row['Job_Title'], row['Location'], row['Equipment_ID'], row['Equipment_Type'], row['Equipment_Status'], row['Production_Tonnage'], row['Maintenance_Cost'], row['Safety_Incident'], row['Environmental_Incident'], row['Community_Relations'], row['Gold_Price'], row['Production_Cost'], row['Revenue'], row['Profit'])
    )

# Commit the changes and close the connection
conn.commit()
conn.close()