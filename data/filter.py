import ijson
import json

filtered = []

# Open the large JSON file for reading
with open('./raw/drug-data-1.json', 'r') as f:
    # Parse each item in the top-level array
    items = ijson.items(f, 'results.item')  # 'item' refers to each object in the array

    # Filter the data as needed
    for item in items:
        if 'symptom' in item and 'medication' in item:
            filtered.append({
                'symptom': item['symptom'],
                'medication': item['medication']
            })

# Write filtered results to a new file
with open('filtered.json', 'w') as f:
    json.dump(filtered, f, indent=2)

print("Filtered data written to filtered.json")
