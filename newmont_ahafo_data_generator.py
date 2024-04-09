from faker import Faker
import pandas as pd
import numpy as np
import random

fake = Faker()

# Generate sample data
data = []
for _ in range(100000):
    date = pd.Timestamp(np.random.choice(pd.date_range(start='2020-01-01', end='2023-12-31')))
    shift = random.choice(['Morning', 'Afternoon', 'Night'])
    employee_id = fake.uuid4().split('-')[0]
    employee_name = fake.name()
    department = random.choice(['Mining', 'Safety', 'Maintenance'])
    job_title = random.choice(['Supervisor', 'Technician', 'Operator'])
    location = random.choice(['Pit', 'Plant', 'Office'])
    equipment_id = fake.uuid4().split('-')[0]
    equipment_type = random.choice(['Excavator', 'Dump Truck', 'Drill Rig'])
    equipment_status = random.choice(['Operational', 'Under Maintenance', 'Out of Service'])
    production_tonnage = round(np.random.uniform(100, 1000), 2)
    maintenance_cost = round(np.random.uniform(1000, 10000), 2)
    safety_incident = random.choice(['Yes', 'No'])
    environmental_incident = random.choice(['Yes', 'No'])
    community_relations = random.choice(['Good', 'Fair', 'Poor'])
    gold_price = round(np.random.uniform(1500, 2000), 2)
    production_cost = round(np.random.uniform(100000, 500000), 2)
    revenue = round(production_tonnage * gold_price, 2)
    profit = round(revenue - production_cost, 2)
    data.append([date, shift, employee_id, employee_name, department, job_title, location,
                 equipment_id, equipment_type, equipment_status, production_tonnage,
                 maintenance_cost, safety_incident, environmental_incident,
                 community_relations, gold_price, production_cost, revenue, profit])

# Create DataFrame
columns = ['Date', 'Shift', 'Employee_ID', 'Employee_Name', 'Department', 'Job_Title', 'Location',
           'Equipment_ID', 'Equipment_Type', 'Equipment_Status', 'Production_Tonnage',
           'Maintenance_Cost', 'Safety_Incident', 'Environmental_Incident',
           'Community_Relations', 'Gold_Price', 'Production_Cost', 'Revenue', 'Profit']
df = pd.DataFrame(data, columns=columns)
df.to_csv('newmont_ahafo_south_mine_dataset.csv', index=False)