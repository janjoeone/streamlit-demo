from openai import OpenAI
import os
import requests
import json

api_key = os.environ.get('OPENAI_API_KEY')
base_url = os.environ.get('OPENAI_BASE_URL')

headers = {'Content-Type': 'application/json',  'Authorization': f'Bearer {api_key}'}
body = {
     "model": "gpt-3.5-turbo",
     "messages": [
         {
             "role": "user",
             "content": "Say Hello"
         }
     ],
     "temperature": 0.7,
     "stream": True
}

response = requests.post(f'{base_url}/chat/completions', json=body, headers=headers, stream=True)

for line in response.iter_lines():
    if not line:
        continue
    data = json.loads(line.decode('utf-8').lstrip('data: '))
    finish_reason = data['choices'][0]['finish_reason']
    if finish_reason == 'stop':
        break
    print(data['choices'][0]['delta']['content'], end='')
print()