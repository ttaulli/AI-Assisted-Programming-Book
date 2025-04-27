#!/usr/bin/env python3
import csv
import random

# File path for the CSV
csv_file = 'demo_data.csv'

# Define sample data for generating random entries
domains = ['gmail.com', 'yahoo.com', 'outlook.com', 'example.com', 'company.net']
first_names = ['John', 'Jane', 'Michael', 'Sara', 'David', 'Emma', 'Robert', 'Lisa']
last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis']
statuses = ['free', 'premium', 'enterprise']

# Create the CSV file
with open(csv_file, 'w', newline='') as f:
    # Create a CSV writer
    writer = csv.writer(f)
    
    # Write header row
    writer.writerow(['id', 'email', 'name', 'age', 'subscription_status'])
    
    # Generate 5 records
    for i in range(1, 6):
        # Generate random data for each record
        first = random.choice(first_names)
        last = random.choice(last_names)
        domain = random.choice(domains)
        email = f'{first.lower()}.{last.lower()}@{domain}'
        name = f'{first} {last}'
        age = random.randint(18, 65)
        status = random.choice(statuses)
        
        # Write the record to the CSV
        writer.writerow([i, email, name, age, status])

print(f'Created demo data with 5 records in {csv_file}')