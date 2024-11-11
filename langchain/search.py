from pydantic import BaseModel
from serpapi import Client
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi

load_dotenv()

class SearchResultItem(BaseModel):
    title: str
    link: str
    snippet: str

class SearchResults(BaseModel):
    results: list[SearchResultItem]

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

prompt = PromptTemplate.from_template("""根据搜索引擎的结果，回答用户的问题。
    SEARCH_RESULTS: {search_results}
    USER_QUERY: {query}
    """)

model = Tongyi(
    model_name = 'qwen-max',
    model_kwargs = {'temperature': 0.01}
)

chain = {
     'search_results': lambda x : get_search_results(x),
     'query': lambda x : x,
} | prompt | model

query = '易建联是什么时间退役的？'

res = chain.invoke(query)

print(res)