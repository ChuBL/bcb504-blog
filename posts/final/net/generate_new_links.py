import json

with open('./net/filtered_network.json') as f:
    data = json.load(f)

nodes = []
new_links = []
sources = set([link['source'] for link in data['links']])
targets = set([link['target'] for link in data['links']])

for node in sources.union(targets):
    if node in sources:
        nodes.append({"id": node, "group": 0})
    else:
        for source in sources:
            new_node_id = f"{node}({source})"
            nodes.append({"id": new_node_id, "group": 1})
            for link in data['links']:
                if link['source'] == source and link['target'] == node:
                    new_links.append({"source": source, "target": new_node_id, "value": link['value']})

new_data = {"nodes": nodes, "links": new_links}

with open('./net/new_filtered_network.json', 'w') as f:
    json.dump(new_data, f, indent=4)
