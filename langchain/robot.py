from langchain.chains.conversation.base import ConversationChain
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import MessagesPlaceholder

# model
model = ChatTongyi(model_name = 'qwen-max', streaming=True)

memory_key = 'history'

#prompt
chat_prompt_template = ChatPromptTemplate.from_messages([
    ('system', '你是一个友好的聊天机器人'),
    MessagesPlaceholder(variable_name=memory_key),
    ('human', '{input}')
])

memory = ConversationBufferMemory(memory_key=memory_key, return_message=True)

# chain
chain = ConversationChain(
    llm = model,
    prompt = chat_prompt_template,
    memory = memory,
)

while True:
    user_input = input('User: ')
    if user_input == 'exit':
        break
    print("AI: ", end='')
    for chunk in chain.stream({'input': user_input}):
        print(chunk['response'], end='')
    print()