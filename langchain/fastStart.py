from langchain_community.llms.tongyi import Tongyi
from langchain.prompts.prompt import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

def translate():
    model = Tongyi(
        model_name = 'qwen-max',
        model_kwargs = {
            'temperature': 0.01
        }
    )
    prompt_template = PromptTemplate.from_template('你是英语翻译官，对用户的输入翻译成英文，不要解释。\n\n{input}')
    user_input = input("请输入要翻译的中文:")
    print("1.用户输入的内容是:", user_input)
    prompt = prompt_template.format(input=user_input)
    print(f"2.生成翻译英文的Prompts:\n'''\n{prompt}\n''")
    print("3.开始调用大语言模型进行翻译")
    res = model.invoke(prompt)
    print("4.输出翻译后的英文内容: ", res)

translate()