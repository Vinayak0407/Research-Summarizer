from utils.keyword_db_handler import read_keywords

def classify_paper(content, current_topic=None):
    """
    Classify a research paper's content based on keywords stored in the .spl file.

    Args:
        content (str): The text content of the research paper.
        current_topic (str, optional): The topic user searched for. Not used for classification.

    Returns:
        str: The matched topic or "Unclassified"
    """
    topic_keywords = read_keywords()

    for topic, keywords in topic_keywords.items():
        for keyword in keywords:
            if keyword.lower() in content.lower():
                print(f"[classify_agent] Paper classified as: {topic}")
                return topic

    print("[classify_agent] Paper classified as: Unclassified")
    return "Unclassified"
