import csv
import json

# Read in the CSV file
filename = "./net/filtered_by_total.csv"
with open(filename, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    rows = [row for row in reader if row["State"] == "United States"]

# Create nodes dictionary
age_groups = list(set(row["Age Group"] for row in rows))
condition_groups = list(set(row["Condition Group"] for row in rows))
nodes = [{"id": group, "group": i} for i, group in enumerate(age_groups + condition_groups)]

# Create links dictionary
max_value = max(int(row["COVID-19 Deaths"]) for row in rows)
min_value = min(int(row["COVID-19 Deaths"]) for row in rows)
links = [{"source": row["Age Group"], "target": row["Condition Group"], "value": (int(row["COVID-19 Deaths"]) - min_value) / (max_value - min_value) * 100} for row in rows]

# Combine nodes and links into a single dictionary
network = {"nodes": nodes, "links": links}

# Write to a JSON file
with open("./net/network.json", "w") as outfile:
    json.dump(network, outfile, indent=4)
