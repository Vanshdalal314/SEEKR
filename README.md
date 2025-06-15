
# 📄 SEEKR: AI-Powered PDF Question Answering System

SEEKR is an AI assistant that lets you upload PDF files and ask questions in natural language. It uses Google Gemini Pro + FAISS to provide accurate answers based on your document content, with support for multi-turn conversations.

---

## 🚀 Features

- 📁 Upload multiple PDF files
- 🔍 Chunk-based semantic search using FAISS
- 🤖 Gemini Pro (Google Generative AI) for intelligent answering
- 💬 Conversational memory with multi-turn chat
- 🌓 Light/Dark Mode support (Streamlit)
- 🖥️ Available via **Streamlit** and **Gradio** interfaces

---

## 🗂️ File Structure



SEEKR/
│
├── src/
│   ├── **init**.py
│   └── helper.py          # Core logic: text extraction, chunking, vector store, conversational chain
│
├── .env                   # Store your GOOGLE\_API\_KEY here
├── app.py                 # Streamlit front-end app
├── app1.py                # Gradio interface (optional)
├── requirements.txt       # All Python dependencies
├── setup.py               # For packaging (optional)
├── test.py                # Script for local testing
└── research/
└── trials.ipynb       # Experimentation and trials notebook


## 🧪 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
````


## 🔑 Setup Environment

Create a `.env` file and add your Google API key:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

### Streamlit:

```bash
streamlit run app.py
```

### Gradio:

```bash
python app1.py
```

---

## 🧠 Tech Stack

* **LangChain** + `langchain_google_genai`
* **Google Generative AI (Gemini)**
* **FAISS** for vector similarity search
* **Streamlit** and **Gradio** for UI

---

## 📌 License

This project is under the MIT License.

---

## ✨ Author

[Vansh Dalal](https://github.com/Vanshdalal314)

```
```
