# src/create_sample_data.py

import pandas as pd
import numpy as np

# Create sample data
np.random.seed(42)
n_rows = 100

data = {
    'employee_id': range(1, n_rows + 1),
    'name': [f'Employee_{i}' for i in range(1, n_rows + 1)],
    'age': np.random.normal(35, 10, n_rows).round(),
    'salary': np.random.normal(60000, 15000, n_rows).round(2),
    'department': np.random.choice(['HR', 'IT', 'Sales', 'Engineering'], n_rows)
}

# Introduce some NULL values
df = pd.DataFrame(data)
df.loc[np.random.choice(df.index, 10), 'age'] = None
df.loc[np.random.choice(df.index, 10), 'salary'] = None

# Save to CSV
df.to_csv('data/raw_employees.csv', index=False)
print("Sample data created in data/raw_employees.csv")