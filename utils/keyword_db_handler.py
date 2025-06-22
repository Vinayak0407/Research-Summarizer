import os

KEYWORDS_FILE = "keywords.spl"

def add_keyword(topic, keyword):
    data = {}

    # Load existing keywords
    if os.path.exists(KEYWORDS_FILE):
        with open(KEYWORDS_FILE, "r", encoding="utf-8") as file:
            for line in file:
                t, *keys = line.strip().split("|")
                data[t] = keys

    # Add the new keyword
    if topic not in data:
        data[topic] = []

    if keyword not in data[topic]:
        data[topic].append(keyword)
        print(f"[keyword_db] ✅ Added '{keyword}' under topic '{topic}'")

    # Write back to file
    with open(KEYWORDS_FILE, "w", encoding="utf-8") as file:
        for t, keys in data.items():
            file.write(f"{t}|{'|'.join(keys)}\n")


def read_keywords():
    keywords_by_topic = {}
    if os.path.exists(KEYWORDS_FILE):
        with open(KEYWORDS_FILE, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split("|")
                if parts:
                    topic = parts[0]
                    keywords = parts[1:] if len(parts) > 1 else []
                    keywords_by_topic[topic] = keywords
    return keywords_by_topic
