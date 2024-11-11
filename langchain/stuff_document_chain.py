from langchain.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain.output_parsers import PydanticOutputParser

from langchain_core.documents import Document
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

from dotenv import load_dotenv
load_dotenv()

model = ChatTongyi(
    model_name = 'qwen-max',
    model_kwargs = {'temperature': 0.01}
)

def get_docs(role: str='student') -> list[Document]:
    docs = []
    if role == 'student':
        docs = [
            Document(page_content='李明喜欢红色但不喜欢黄色'),
            Document(page_content='李华喜欢绿色但他更喜欢橙色')
        ]
    elif role == 'teacher':
        docs = [
            Document(page_content='张老师喜欢紫色'),
            Document(page_content='李老师喜欢黄色和蓝色')
        ]
    return docs

prompt1 = PromptTemplate.from_template('每个人喜欢的颜色是什么:\n\n{context}')
favorite_color_base_docs_chain = create_stuff_documents_chain(
    llm = model,
    prompt = prompt1,
    output_parser = StrOutputParser()
)
res1 = favorite_color_base_docs_chain.invoke({
    'context': get_docs(),
})
print(res1)

favorite_color_base_attached_docs_chain = {'context': get_docs} | favorite_color_base_docs_chain
res2 = favorite_color_base_attached_docs_chain.invoke('teacher')
print(res2)

prompt2 = PromptTemplate.from_template('谁喜欢{color}: \n\n{context}')
who_like_certain_color_chain = {
    'context': RunnableLambda(lambda x :x['role']) | favorite_color_base_attached_docs_chain,
    'color': RunnableLambda(lambda x : x['color'])
    } | prompt2 | model
res3 = who_like_certain_color_chain.invoke({
    'role': 'student',
    'color': '红色'
})
print(res3)