from openai import OpenAI
import os
import requests

path = os.environ.get('Path')
print(path)
url = 'https://api.openai.com/v1/chat/completions'
API_KEY = os.environ.get('OPENAI_API_KEY')
headers = {'Content-Type': 'application/json',  'Authorization': f'Bearer {API_KEY}'}
body = {
     "model": "gpt-4o-mini",
     "messages": [{"role": "user", "content": "Say Hello"}],
     "temperature": 0.7
   }
print(headers)
response = requests.post(url, json=body, headers=headers)
print(response.text)