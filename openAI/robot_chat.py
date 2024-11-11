from openai import OpenAI
import os

api_key = os.environ.get('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

chat_history = [
    {'role': 'system', 'content': 'You are a helpful assistant.'}
]

while True:
    user_input = input("User:")
    if user_input == "quit":
        break

    # 将用户输入追加至聊天记录
    chat_history.append({'role': 'user', 'content': user_input})
    stream = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=chat_history,
        stream=True
    )

    # 记录本次大模型返回的完整内容
    whole_content = ''

    for chunk in stream:
        if chunk.choices[0].delta.content:
            chunk_content = chunk.choices[0].delta.content
            print(chunk_content, end='')
            whole_content += chunk_content

    # 将大模型的回复追加至聊天记录
    chat_history.append({'role': 'assistant', 'content': whole_content})