from agents.search_agent import search_papers
from agents.process_agent import process_paper
from agents.classify_agent import classify_paper
from agents.summarize_agent import summarize_text
from agents.synthesis_agent import synthesize_summaries
from agents.audio_agent import generate_audio
from utils.keyword_db_handler import add_keyword
from utils.paper_loader import load_pdf, load_doi
import time
import json
import os

def main():
    print("Enter a research topic: ", end="")
    topic = input().strip()

    print(f"\n[main] Starting search for topic: {topic}")

    # ➕ Prompt for classification keywords
    print(f"\nEnter classification keywords for '{topic}' (comma-separated): ", end="")
    keywords_input = input().strip()
    keywords = [kw.strip() for kw in keywords_input.split(',') if kw.strip()]
    for kw in keywords:
        add_keyword(topic, kw)
        print(f"[main] ✅ Added keyword '{kw}' under topic '{topic}'")

    # ✅ Select Input Type
    print("\nSelect input type:\n1. Search papers\n2. Upload PDF\n3. Enter DOI")
    choice = input("Choice [1/2/3]: ").strip()

    papers = []

    if choice == "1":
        paper_results = search_papers(topic)
        for title, url, abstract in paper_results:
            papers.append((title, url, abstract))

    elif choice == "2":
        pdf_path = input("Enter PDF file path: ").strip().strip('"')
        if os.path.exists(pdf_path):
            content = load_pdf(pdf_path)
            papers.append((f"PDF Paper from {pdf_path}", pdf_path, content))
        else:
            print("[main] ❌ Invalid PDF path")

    elif choice == "3":
        doi = input("Enter DOI: ").strip()
        content = load_doi(doi)
        papers.append((f"DOI Paper from {doi}", doi, content))

    else:
        print("[main] ❌ Invalid choice")
        return

    summaries = []
    citations = []

    for idx, paper in enumerate(papers, 1):
        if len(paper) == 3:
            title, source, content = paper
        else:
            title, source = paper
            content = process_paper(source)

        print(f"\nFound paper: {title} ({source})")

        if content:
            label = classify_paper(content, topic)
            print(f"[main] 🏷️ Classification: {label}")

            summary = summarize_text(content)
            marked_summary = summary.strip() + f" [{idx}]"
            summaries.append(marked_summary)
            print(f"[main] 📄 Summary:\n{marked_summary}")

            citations.append({"title": title, "url": source})
        else:
            print("[main] ⚠️ Skipped due to empty content")

        time.sleep(1)

    # 🔬 Cross-paper synthesis
    if summaries:
        combined_summary = synthesize_summaries(summaries, topic)
        print(f"\n[main] 🔬 Cross-paper Synthesis:\n{combined_summary}")

        generate_audio(combined_summary, filename="summary_audio.mp3")
        print(f"[main] 🔊 Audio podcast generated: summary_audio.mp3")

    # 📚 Show citations
    if citations:
        print("\n[main] 📚 Citations:")
        for i, c in enumerate(citations, 1):
            print(f"[{i}] {c['title']} - {c['url']}")
        with open("citations.json", "w") as f:
            json.dump(citations, f, indent=2)

if __name__ == "__main__":
    main()
