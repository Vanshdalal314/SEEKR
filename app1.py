import gradio as gr
import time
from src.helper import get_pdf_text, get_text_chunks, get_vector_store, get_conversational_chain

# Global session state
conversation = None
chat_history = []

def process_pdfs(pdf_files):
    global conversation, chat_history
    chat_history = []
    raw_text = get_pdf_text(pdf_files)
    text_chunks = get_text_chunks(raw_text)
    vector_store = get_vector_store(text_chunks)
    conversation = get_conversational_chain(vector_store)
    return "✅ PDF processed. You can now ask questions."

def chat(user_question):
    global conversation, chat_history
    if conversation is None:
        return "⚠️ Please upload and process a PDF first."
    response = conversation({'question': user_question})
    chat_history = response['chat_history']
    
    output = ""
    for i, message in enumerate(chat_history):
        if i % 2 == 0:
            output += f"👤 **User**: {message.content}\n"
        else:
            output += f"🤖 **Reply**: {message.content}\n"
    return output

with gr.Blocks() as demo:
    gr.Markdown("# 📄 SEEKR: Information Retrieval System")
    
    with gr.Row():
        pdf_input = gr.File(file_types=[".pdf"], file_count="multiple", label="Upload your PDF files")
        process_btn = gr.Button("Submit & Process")
    
    status = gr.Textbox(label="Status", interactive=False)

    question = gr.Textbox(lines=1, placeholder="Ask a question from your PDF...")
    answer = gr.Markdown()

    process_btn.click(process_pdfs, inputs=pdf_input, outputs=status)
    question.submit(chat, inputs=question, outputs=answer)

demo.launch()