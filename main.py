import yaml
import requests
import time
from urllib.parse import urlparse

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        if data is None:
            print("Warning: YAML file is empty or not properly formatted.")
        return data

def get_domain(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return domain

def make_requests(item):
    url = item.get("url")
    method = item.get("method","GET")
    body = item.get("body", None)
    headers = item.get("headers", {})
    success = False

    start_time = time.time()

    if method == "GET":
        response = requests.get(url, headers=headers)
    elif method == "POST":
        response = requests.post(url, data=body, headers=headers)
    else:
        print("There is no method")

    print(f"Response from {url}: {response.status_code}")

    end_time = time.time()
    latency = (end_time - start_time) * 1000

    print(f"Response latency: {latency:.2f} ms")

    if latency <= 500.00 and 200 <= response.status_code < 300:
        success = True
        print("Domain is up")
    else:
        print("Domain is down")
    
    return get_domain(url), success

def main():
    data = load_yaml('sample.yaml')
    while True:
        for item in data:
            domain, success = make_requests(item)
            print(f"{domain} is {success}")
        
        time.sleep(15)

if __name__ == '__main__':
    main()