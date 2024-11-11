from langchain.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

# prompt template
prompt = PromptTemplate.from_template("参考下面的格式回答用户的问题\n {_format}\n{query}\n")

# model
model = ChatTongyi(
    model_name = 'qwen-max',
    model_kwargs = {'temperature': 0.01}
)

# output parser
class Joke(BaseModel):
    content: str = Field(description='笑话的内容')
    reason: str = Field(description='为什么好笑')
parser = PydanticOutputParser(pydantic_object=Joke)

# chain
chain = prompt | model | parser

res = chain.invoke({
    '_format': parser.get_format_instructions(),
    'query': '讲一个笑话'
})

print(res)