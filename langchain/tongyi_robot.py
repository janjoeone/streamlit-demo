from langchain.prompts import PromptTemplate
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain.output_parsers import PydanticOutputParser
from datetime import datetime

from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

class LogModel(BaseModel):
    user_input: str = Field(description='用户输入的内容')
    llm_output: str = Field(description='大模型的输出')

prompt = PromptTemplate.from_template("按照如下的格式回答用户的问题\n {_format}\n{query}")

model = ChatTongyi(
    model_name = 'qwen-max',
    model_kwargs = {'temperature': 0.01}
)

parser = PydanticOutputParser(pydantic_object=LogModel)

while True:
    user_input = input('User: ')
    if user_input == 'quit':
        break
    res = model.invoke(prompt.format(
        _format = parser.get_format_instructions(),
        query = user_input,
    ))
    logModelObj = parser.parse(res.content)
    print(f'AI: {logModelObj.llm_output}')
    _time = datetime.now().strftime('%H:%M:%S')
    print(f'{_time}: INFO: USER: {logModelObj.user_input}, AI: {logModelObj.llm_output}')


