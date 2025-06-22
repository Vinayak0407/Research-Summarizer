import fitz  # PyMuPDF
import requests
import json

# Load text content from a PDF file
def load_pdf(filepath):
    try:
        doc = fitz.open(filepath)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        print(f"[paper_loader] ✅ Extracted text from PDF: {filepath}")
        return text.strip()
    except Exception as e:
        print(f"[paper_loader] ❌ Error reading PDF: {e}")
        return ""

# Load paper content using a DOI (uses CrossRef API)
def load_doi(doi):
    try:
        headers = {"Accept": "application/vnd.crossref.unixsd+xml"}
        url = f"https://api.crossref.org/works/{doi}"
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            title = data['message'].get('title', ['No title'])[0]
            abstract = data['message'].get('abstract', '')

            if abstract:
                print(f"[paper_loader] ✅ Retrieved abstract for DOI: {doi}")
                return f"{title}\n\n{abstract}"
            else:
                print(f"[paper_loader] ⚠️ No abstract found for DOI: {doi}")
                return title
        else:
            print(f"[paper_loader] ❌ DOI not found or inaccessible: {doi}")
            return ""
    except Exception as e:
        print(f"[paper_loader] ❌ Error fetching DOI: {e}")
        return ""
