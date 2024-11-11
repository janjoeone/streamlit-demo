from dataclasses import dataclass, field
from typing import List, Optional
from serpapi import Client
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

@dataclass
class SearchResultItem:
    title: str
    link: str
    snippet: str

@dataclass
class SearchResults:
    results: list[SearchResultItem]

SearchResultItem = SearchResultItem(
    title='官宣！36岁易建联宣布退役：21年生涯落幕 开启人生新篇章',
    link='https://new.qq.com/rain/a/20230830A003Z400',
    snippet='北京时间8月30日，广东男篮球员易建联，正式宣布退役，告别21年篮球生涯，阿联说自己会继续前行，去迎接新的篇章。'
)

# 初始化openai客户端
openai_client = OpenAI(
    api_key = os.environ.get('OPENAI_API_KEY'),
    base_url = os.environ.get('OPENAI_BASE_URL')
)
# 初始化google搜索客户端
google_client = Client(
    api_key = os.environ.get('SERPAPI_KEY')
)

# 请求google搜索获取搜索结果，并组装为特定数据类型返回
def get_search_results(query:str) -> SearchResults:
    params = {
        "engine": "google",
        "q": query,
    }

    results = google_client.search(params)
    organic_results = results["organic_results"]
    search_results = SearchResults(
        results = [
            SearchResultItem(
                title = organic_result['title'],
                link = organic_result['link'],
                snippet = organic_result['snippet']
            )
            for organic_result in organic_results
        ]
    )
    return search_results

def search_prompt(query:str, search_results:SearchResults) -> str:
    _prompt = f"""根据搜索引擎的结果，回答用户的问题。
    SEARCH_RESULTS: {search_results}
    USER_QUERY: {query}
    """
    return _prompt

# 请求openai获取结果，流式输出
def chat(prompt:str) -> str:
    stream = openai_client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
        model='gpt-3.5-turbo',
        stream=True
    )
    whole_content = ''
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            chunk_content = chunk.choices[0].delta.content,
            print(chunk_content, end='', flush=True)
            whole_content += chunk_content
    print()
    return whole_content

# query = input('User:')
# chat(search_prompt(query, get_search_results(query)))
print(get_search_results('查理芒格现在怎么样了'))