from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import HumanMessagePromptTemplate
from langchain.schema import AIMessage,SystemMessage,HumanMessage

from dotenv import load_dotenv
load_dotenv()

chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content=(
                '你是一个翻译官，将用户的文本翻译为英语'
            )
        ),
        HumanMessage(content='你好'),
        AIMessage(content='Hello'),
        HumanMessagePromptTemplate.from_template('{text}')
    ]
)

print(chat_template.format_messages(text='我喜欢踢足球'))

model = ChatTongyi(
    model_name = 'qwen-max'
)

chain = chat_template | model

res = chain.invoke({'text': '我喜欢踢足球'})

print(res)