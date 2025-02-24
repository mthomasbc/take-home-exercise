import yaml

with open('sample.yaml', 'r') as file:
    data = yaml.safe_load(file)

print(data)