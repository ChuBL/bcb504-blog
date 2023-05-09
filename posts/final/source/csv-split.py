import pandas as pd

# Read the input CSV file
input_file = 'Conditions_Contributing_to_COVID-19_Deaths__by_State_and_Age__Provisional_2020-2023.csv'
df = pd.read_csv(input_file)

# Split the DataFrame based on the "Group" column values
df_by_total = df[df['Group'] == 'By Total']
df_by_month = df[df['Group'] == 'By Month']
df_by_year = df[df['Group'] == 'By Year']

# Write the DataFrames to separate CSV files
df_by_total.to_csv('by_total.csv', index=False)
df_by_month.to_csv('by_month.csv', index=False)
df_by_year.to_csv('by_year.csv', index=False)
