import requests
from urllib.parse import urlparse
import errno

def validate_url(url):
    try:
        result = urlparse(url)
        print("got through here")
        return all([result.scheme in ["http", "https"], result.netloc]) 
    #all() check if every attribute is true then returns true else False
    # netloc is used for domain name
    except Exception as e:
        print(e)
        return False

def analyze_headers(response):
    key_pairs = list(response.headers.keys())
    print(key_pairs)


def check_status_code(response):
    code = response.status_code
    match code//100:
        case 1:
            print(f"Request under process.\nStatus code : {code}")

        case 2:
            print(f"Successful.\nStatus code : {code}")

        case 3:
            print(f"Redirection.\nStatus code : {code}")

        case 4:
            print(f"Client Error.\nStatus code : {code}")

        case 5:
            print(f"Server Error.\nStatus code : {code}")
    analyze_headers(response)


def main():
    url = input("Enter the URL of the website: ")
    if(validate_url(url)):
        try:
            response = requests.get(url, timeout=5.0)
            check_status_code(response)
        except requests.exceptions.Timeout:
            print("The request timed out. The server is taking too long to respond.")


main()