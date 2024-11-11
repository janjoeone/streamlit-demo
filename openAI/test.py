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


# 请求google搜索获取搜索结果，并组装为特定数据类型返回
def get_search_results(query:str) -> SearchResults:
    organic_results = [
    {
      "position": 1,
      "title": "查理·芒格去世，享年99岁！（附生前最后一次万字访谈）",
      "link": "https://www.sohu.com/a/739929162_120913760",
      "redirect_link": "https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.sohu.com/a/739929162_120913760&ved=2ahUKEwj68dL_j7SJAxXfMlkFHSAuD9kQFnoECBYQAQ",
      "displayed_link": "https://www.sohu.com › ...",
      "favicon": "https://serpapi.com/searches/67211cafcc4879ba4f5e286e/images/3342d60ce4d502e81b7a27cec9979001a96be84050e61617c95e4a49319a6a69.webp",
      "date": "Nov 29, 2023",
      "snippet": "查理·芒格去世，享年99岁！（附生前最后一次万字访谈） ... 当地时间周二（11月28日），伯克希尔-哈撒韦在其子公司美国商业资讯网站上发布声明表示，董事会副主席 ...",
      "snippet_highlighted_words": [
        "查理",
        "芒格"
      ],
      "source": "搜狐"
    },
    {
      "position": 2,
      "title": "芒格去世，这是他生前最后一次深度访谈长文",
      "link": "https://finance.sina.cn/2023-11-29/detail-imzwfvuw3990628.d.html",
      "redirect_link": "https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://finance.sina.cn/2023-11-29/detail-imzwfvuw3990628.d.html&ved=2ahUKEwj68dL_j7SJAxXfMlkFHSAuD9kQFnoECBgQAQ",
      "displayed_link": "https://finance.sina.cn › detail-imzw...",
      "favicon": "https://serpapi.com/searches/67211cafcc4879ba4f5e286e/images/3342d60ce4d502e81b7a27cec9979001dc530a3ecd0aae95bef9536b5168dee1.webp",
      "date": "Nov 29, 2023",
      "snippet": "伯克希尔哈撒韦公司公告称，当地时间11月28日上午，查理·芒格在加州一家医院安详地离世。伯克希尔CEO、股神巴菲特在声明中表示：“没有查理的灵感、智慧和 ...",
      "snippet_highlighted_words": [
        "查理",
        "芒格"
      ],
      "source": "新浪财经"
    },
    {
      "position": 3,
      "title": "查理·芒格：光芒背后的智者，微光也同样耀眼",
      "link": "https://www.futunn.com/learn/detail-charlie-munger-the-wise-man-behind-the-light-the-glimmer-is-just-as-dazzling-54045-231193064",
      "redirect_link": "https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.futunn.com/learn/detail-charlie-munger-the-wise-man-behind-the-light-the-glimmer-is-just-as-dazzling-54045-231193064&ved=2ahUKEwj68dL_j7SJAxXfMlkFHSAuD9kQFnoECBoQAQ",
      "displayed_link": "https://www.futunn.com › learn › det...",
      "favicon": "https://serpapi.com/searches/67211cafcc4879ba4f5e286e/images/3342d60ce4d502e81b7a27cec99790013a415bba84b4f47a2ff22e2ca1d18381.webp",
      "snippet": "今天一早看到消息：查理·芒格于当地时间周二（11月28日）去世，享年99岁，距离他的100岁生日只有一个月。 从此，人间少了一位传奇的投资大佬，少了一位满身智慧的老人，也少了 ...",
      "snippet_highlighted_words": [
        "查理",
        "芒格"
      ],
      "source": "富途牛牛"
    },
    {
      "position": 4,
      "title": "查理·芒格去世：巴菲特的好搭档，金句频出的亿万富翁",
      "link": "https://cn.nytimes.com/obits/20231129/charles-t-munger-dead/",
      "redirect_link": "https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://cn.nytimes.com/obits/20231129/charles-t-munger-dead/&ved=2ahUKEwj68dL_j7SJAxXfMlkFHSAuD9kQFnoECB4QAQ",
      "displayed_link": "https://cn.nytimes.com › obits › cha...",
      "favicon": "https://serpapi.com/searches/67211cafcc4879ba4f5e286e/images/3342d60ce4d502e81b7a27cec9979001573ee661865fdabd0aae808537e6835b.webp",
      "date": "Nov 29, 2023",
      "snippet": "查理·芒格于周二在加州圣巴巴拉去世，享年99岁。 他放弃了已功成名就的律师事业，成为沃伦·巴菲特的合伙人和金句频出的挚友，两人联手将一家江河日下的新 ...",
      "source": "纽约时报中文网"
    },
    {
      "position": 5,
      "title": "芒格离世，他和那个价值投资的“巨星时代”",
      "link": "https://wallstreetcn.com/articles/3703070",
      "redirect_link": "https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://wallstreetcn.com/articles/3703070&ved=2ahUKEwj68dL_j7SJAxXfMlkFHSAuD9kQFnoECBsQAQ",
      "displayed_link": "https://wallstreetcn.com › articles",
      "favicon": "https://serpapi.com/searches/67211cafcc4879ba4f5e286e/images/3342d60ce4d502e81b7a27cec9979001914536c32d8b645bfa4d5e1877c348b2.webp",
      "date": "Nov 28, 2023",
      "snippet": "一位投资巨人离世！ 伯克希尔哈撒韦公司正式公告：当地时间11月28日上午，查理·芒格（Charlie Munger）在美国加利福尼亚州一家医院安详地离世。",
      "snippet_highlighted_words": [
        "查理",
        "芒格"
      ],
      "source": "华尔街见闻"
    },
    {
      "position": 6,
      "title": "缅怀查理芒格：这位投资天才为我们留下了什么遗产？",
      "link": "https://www.moomoo.com/hans/community/discussion/remembering-charlie-munger-what-s-the-legacy-from-this-investing-1183845537",
      "redirect_link": "https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.moomoo.com/hans/community/discussion/remembering-charlie-munger-what-s-the-legacy-from-this-investing-1183845537&ved=2ahUKEwj68dL_j7SJAxXfMlkFHSAuD9kQFnoECDQQAQ",
      "displayed_link": "https://www.moomoo.com › discussion",
      "favicon": "https://serpapi.com/searches/67211cafcc4879ba4f5e286e/images/3342d60ce4d502e81b7a27cec9979001f6ae24785821e0865a85555c0e661571.webp",
      "snippet": "巴菲特公司伯克希尔哈撒韦公告称， 昨晚11月28日当地时间上午， 公司首席副董事长查理·芒格在加州一家医院安详离世。 世上又少一位世界投资大师巴菲特在声明中表示： “没有 ...",
      "snippet_highlighted_words": [
        "查理",
        "芒格"
      ],
      "source": "Moomoo"
    },
    {
      "position": 7,
      "title": "查理·芒格去世回顾他的理念、经历与感悟",
      "link": "https://app-web.chnfund.com/wind/202311/t20231129_4294146.html",
      "redirect_link": "https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://app-web.chnfund.com/wind/202311/t20231129_4294146.html&ved=2ahUKEwj68dL_j7SJAxXfMlkFHSAuD9kQFnoECDUQAQ",
      "displayed_link": "https://app-web.chnfund.com › wind",
      "favicon": "https://serpapi.com/searches/67211cafcc4879ba4f5e286e/images/3342d60ce4d502e81b7a27cec997900198867b270e413f1e0179532140c346b8.webp",
      "date": "Nov 29, 2023",
      "snippet": "美国当地时间11月28日，伯克希尔·哈撒韦在其官网上发布公告表示：查理·芒格的家人告知公司，芒格已于当天早上在加州一家医院中安详去世。芒格先生享年99 ...",
      "snippet_highlighted_words": [
        "查理",
        "芒格"
      ],
      "source": "中国基金报"
    },
    {
      "position": 8,
      "title": "人物｜工作完成！投资巨人查理·芒格去世，享年99岁",
      "link": "https://m.21jingji.com/article/20231129/herald/312d6beb68c6d2a978a51ff42f3dbc08.html",
      "redirect_link": "https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://m.21jingji.com/article/20231129/herald/312d6beb68c6d2a978a51ff42f3dbc08.html&ved=2ahUKEwj68dL_j7SJAxXfMlkFHSAuD9kQFnoECDIQAQ",
      "displayed_link": "https://m.21jingji.com › herald",
      "favicon": "https://serpapi.com/searches/67211cafcc4879ba4f5e286e/images/3342d60ce4d502e81b7a27cec99790016ad3f85e23c8df8b5c10858ede0138a5.webp",
      "date": "Nov 29, 2023",
      "snippet": "查理·芒格（Charlie Munger）没能等到庆祝自己的元旦百岁寿辰，这位沃伦·巴菲特（Warren Buffett）的老得力助手、长期商业伙伴11月28日去世，享年99岁。",
      "snippet_highlighted_words": [
        "庆祝"
      ],
      "source": "21财经"
    },
    {
      "position": 9,
      "title": "拒绝上福布斯富豪榜，不签捐赠承诺：查理·芒格的真实人生",
      "link": "https://www.zgcsj.com/gyr/2023-12-06/1187.shtml",
      "redirect_link": "https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.zgcsj.com/gyr/2023-12-06/1187.shtml&ved=2ahUKEwj68dL_j7SJAxXfMlkFHSAuD9kQFnoECC8QAQ",
      "displayed_link": "https://www.zgcsj.com › gyr",
      "date": "Dec 6, 2023",
      "snippet": "亿万富翁查理·芒格(Charlie Munger)去世，享年99 岁。 除了伯克希尔副董事长、投资智者、价值策略大师，芒格身上的标签还有房地产律师、出版 ...",
      "snippet_highlighted_words": [
        "查理",
        "芒格"
      ],
      "source": "中国慈善家"
    }
  ]
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

print(get_search_results('查理芒格现在怎么样了'))
