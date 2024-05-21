import json

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Example usage
data = read_json_file('sample.json')
# print(data)
# print(data['batters'])
print(data['batters']['batter'])
