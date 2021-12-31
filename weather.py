import sys
import requests
import os
from argparse import ArgumentParser

parser = ArgumentParser(description="Get the current weather information for your zipcode")
parser.add_argument('zip', help="zip/postal code to get weather for")
parser.add_argument('--country', default="kz", help="Country zip/postal belongs to, default is 'kz'")

args = parser.parse_args()

api_key = os.getenv("OWI_API_KEY")

if not api_key:
    print("Error: no 'OWM_API_KEY' provided")
    sys.exit(1)
url = f"http://api.openweathermap.org/data/2.5/weather?zip={args.zip},{args.country}&appid={api_key}"

res = requests.get(url)
print(res)
