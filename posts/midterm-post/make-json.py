import csv
import json
import pandas as pd

# read csv file into pandas DataFrame
df = pd.read_csv('teammates.csv', delimiter=',')

# initialize nodes and links lists
nodes = []
links = []

# initialize groups and assign them
groups = {}
group_counter = 1

for index, row in df.iterrows():
    for item in [row['from'], row['to']]:
        if group_counter > 20:
            break
        if item not in groups:
            nodes.append({"id": item, "group": group_counter})
            groups[item] = group_counter
            group_counter += 1

    if row['from'] not in groups or row['to'] not in groups:
        continue
    # scale weight to integer with minimum value of 1
    weight = max(1, int(float(row['weight'].strip('%'))))/5

    links.append({"source": row['from'], "target": row['to'], "value": weight})

# create final JSON object
data = {"nodes": nodes, "links": links}

# write JSON data to output file
with open('output.json', 'w') as outfile:
    json.dump(data, outfile, indent=2)
