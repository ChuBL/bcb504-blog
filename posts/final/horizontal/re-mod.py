import re

# Read the CSV file
with open('output.csv', 'r') as file:
    csv_data = file.read()

# Define the regex pattern
pattern = r'(?<=,)([a-zA-Z ]+)(?=,)'

# Define the replacement string
replace_str = r'"\1"'

# Replace the matches with the original text enclosed in quotes
csv_data = re.sub(pattern, replace_str, csv_data)

# Write the updated CSV file
with open('output2.csv', 'w') as file:
    file.write(csv_data)
