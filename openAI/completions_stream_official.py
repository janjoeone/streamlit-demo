from openai import OpenAI, Stream
import os

client = OpenAI(
    api_key = os.environ.get('OPENAI_API_KEY'),
    base_url = os.environ.get('OPENAI_BASE_URL')
)

# completions API
stream = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": 'say hello',
        },
    ],
    model='gpt-3.5-turbo',
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end='')
