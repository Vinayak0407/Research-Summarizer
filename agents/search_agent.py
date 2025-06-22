import requests

def search_papers(query, limit=5):
    print(f"[search_agent] Searching papers for: {query}")
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit={limit}&fields=title,url,abstract"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        papers = []
        for paper in data.get("data", []):
            title = paper.get("title", "No title")
            paper_url = paper.get("url", "")
            abstract = paper.get("abstract", "")
            papers.append((title, paper_url, abstract))
        return papers

    except Exception as e:
        print(f"[search_agent] ❌ Error searching papers: {e}")
        return []
