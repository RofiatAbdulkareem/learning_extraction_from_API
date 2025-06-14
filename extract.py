import requests
import pandas as pd

url = 'https://jsonplaceholder.typicode.com/users'

response = requests.get(url)

def extract_api():
    if response.status_code ==200:
        data = response.json()
        df = pd.json_normalize(data) #pd.DataFrame
    return df    

print(extract_api())