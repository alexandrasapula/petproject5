from langchain_tavily import TavilySearch
from django.conf import settings


def web_search(query, k=5):
    tool = TavilySearch(
        api_key=settings.TAVILY_API_KEY,
        max_results=k,
    )

    results = tool.invoke(query)

    return "\n".join(
        f"{r.get('title', 'No Title')}: {r.get('content', 'No Content')}"
        for r in results if isinstance(r, dict)
    )
