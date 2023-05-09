import json

# Load the JSON file
with open("./net/new_filtered_network.json") as f:
    data = json.load(f)

# Find all nodes in group 0
group0_nodes = [node for node in data['nodes'] if node['group'] == 0]

# Create a center node
center_node = {'id': 'center', 'group': -1}

# Add links from center node to all group 0 nodes
links = data['links']
for node in group0_nodes:
    links.append({'source': 'center', 'target': node['id'], 'value': 1})

# Add the center node to the nodes list
nodes = data['nodes']
nodes.append(center_node)

# Save the modified data as a new JSON file
new_data = {'nodes': nodes, 'links': links}
with open("./net/new_filtered_network_with_center.json", "w") as f:
    json.dump(new_data, f)
