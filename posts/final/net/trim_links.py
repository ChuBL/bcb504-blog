import json

# Load the JSON data
with open('./net/network.json', 'r') as f:
    data = json.load(f)

# Create a dictionary to store the max values for each source
max_values = {}

# Loop through the links to find the max value for each source
for link in data['links']:
    source = link['source']
    value = link['value']
    if source in max_values:
        max_values[source].append(value)
    else:
        max_values[source] = [value]

# Loop through the links again to filter out those with values less than the top 3
filtered_links = []
for link in data['links']:
    source = link['source']
    value = link['value']
    if len(max_values[source]) > 3 and value < sorted(max_values[source], reverse=True)[2]:
        continue
    filtered_links.append(link)

# Create a new dictionary with the filtered links
filtered_data = {
    'nodes': data['nodes'],
    'links': filtered_links
}

# Save the filtered data to a new JSON file
with open('./net/filtered_network.json', 'w') as f:
    json.dump(filtered_data, f, indent=4)
