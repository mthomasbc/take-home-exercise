import yaml

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        if data is None:
            print("Warning: YAML file is empty or not properly formatted.")
        return data

def main():
    data = load_yaml('sample.yaml')
    for item in data:
        print(item)

if __name__ == '__main__':
    main()