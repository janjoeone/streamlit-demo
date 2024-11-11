from openai import OpenAI
import os

client = OpenAI(
    api_key = os.environ.get('OPENAI_API_KEY'),
    base_url = os.environ.get('OPENAI_BASE_URL')
)

# Embeddings API
response = client.embeddings.create(
    model='text-embedding-ada-002',
    input='hello',
    encoding_format='float'
)

print(len(response.data[0].embedding))
