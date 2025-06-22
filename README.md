# 🧠 Research Paper Summarization Multi-Agent System

A multi-agent AI system that can search, process, classify, summarize, synthesize, and convert research papers into audio podcasts — making academic research more accessible and digestible.

## 🚀 Features

- 🔍 **Search**: Query research papers based on topics
- 📎 **Input Options**: Accept paper input via:
  - Online search
  - PDF upload
  - DOI references
- 🧠 **Agents**:
  - `search_agent`: Finds relevant papers
  - `process_agent`: Extracts text from URL/PDF/DOI
  - `classify_agent`: Categorizes based on user-defined keywords
  - `summarize_agent`: Summarizes each paper
  - `synthesis_agent`: Generates a cross-paper synthesis
  - `audio_agent`: Converts summaries into podcasts
- 🗃️ **Keyword Memory**: Stores topic-keyword mappings in `.spl` file
- 🔗 **Citation Tracking**: Inline citations + export to `citations.json`
- 🔊 **Audio Summary**: Text-to-speech podcast via `pyttsx3` (offline)

## 🛠️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/your-username/research-summarizer.git
cd research-summarizer
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # For Windows
# OR
source venv/bin/activate  # For macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create Environment File

Create a `.env` file in the root directory and add your API key (if required in the future).

```env
OPENAI_API_KEY=your_api_key_here
```

## 🧪 How to Run

```bash
python main.py
```

Follow the prompts to:
- Input a research topic
- Define classification keywords
- Choose how to input papers (search, PDF, DOI)

## 📁 Project Structure

```
research-summarizer/
├── agents/
│   ├── search_agent.py
│   ├── process_agent.py
│   ├── classify_agent.py
│   ├── summarize_agent.py
│   ├── synthesis_agent.py
│   └── audio_agent.py
├── utils/
│   ├── keyword_db_handler.py
│   └── paper_loader.py
├── data/
│   └── keywords.spl
├── main.py
├── requirements.txt
├── README.md
└── citations.json
```

## 🧠 Tech Stack

- Python 3.9+
- PyMuPDF (PDF parsing)
- requests (DOI fetching)
- pyttsx3 (offline TTS)
- JSON / custom `.spl` format for keyword tracking

## 📎 Sample Input / Output

**Prompt**:
```
Topic: AI in education
Keywords: chatbot, adaptive learning
```

**Summary Output**:
```
📄 Summary:
This paper explores the use of chatbots in online learning environments...
```

**Audio Output**:
```
summary_audio.mp3
```

**Citations**:
```
[1] Title - https://doi.org/xxx
```

## 📦 Future Improvements

- Add real-time scraping and OpenAI integration
- Multi-language support for summaries and audio
- Web dashboard or mobile app interface
- Dockerized deployment

## 📜 License

MIT License – feel free to use, modify, and distribute.

### 📽 Demo Video

[Click here to watch the demo](https://drive.google.com/file/d/1Yj1nVxYYeU_oEfjJ8NSDIYIISnsXtq5E/view?usp=sharing)
