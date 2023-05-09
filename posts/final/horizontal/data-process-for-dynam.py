import pandas as pd
from datetime import datetime

# Read the CSV file
df = pd.read_csv("filtered_by_month.csv")

# Define the US states list
us_states = ['District of Columbia', 'New York City', 'Alabama', 'Alaska', 'Arizona', 'Arkansas', 
             'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 
             'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan',
             'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
             'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
             'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia',
             'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

# Exclude rows where the 'name' column is 'United States'
df = df[df['State'] != 'United States']

# Extract the necessary columns and rename them
df = df[['Start Date', 'State', 'COVID-19 Deaths']]
df = df.rename(columns={'Start Date': 'date', 'State': 'name', 'COVID-19 Deaths': 'value'})

# Convert the date column to datetime format
df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y')

# Format the date column as '1970-01-01'
df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))

# Add the category column using the US states list
df['category'] = df['name'].apply(lambda x: us_states.index(x))

# Group the data by date, name, and category, and sum the values
df = df.groupby(['date', 'name', 'category'], as_index=False).sum()



# Add the index column and reorder the columns
df.insert(0, 'index', range(1, len(df) + 1))
df = df[['index', 'date', 'name', 'category', 'value']]
# Cast the index and name columns to string
df['index'] = df['index'].astype(str)
df['name'] = df['name'].astype(str)
# Save the output to a CSV file
df.to_csv('./horizontal/output.csv', index=False)
