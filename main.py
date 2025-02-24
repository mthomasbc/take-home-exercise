import yaml

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        print(data)

def main():
    load_yaml('sample.yaml')

if __name__ == '__main__':
    main()