from openai import OpenAI
import os

client = OpenAI(
    api_key = os.environ.get('OPENAI_API_KEY'),
    base_url = os.environ.get('OPENAI_BASE_URL')
)

# completions API
def chat(prompt, model = 'gpt-3.5-turbo'):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role" : "system",
                "content" : "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        model=model,
    )
    return chat_completion.choices[0].message.content

chat('America President is')