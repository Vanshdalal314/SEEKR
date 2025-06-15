# import streamlit as st
# import time
# from src.helper import get_pdf_text, get_text_chunks, get_vector_store, get_conversational_chain

# def user_input(user_question):
#     response = st.session_state.conversation({'question': user_question})
#     st.session_state.chatHistory = response['chat_history']
#     for i, message in enumerate(st.session_state.chatHistory):
#         if i%2 == 0:
#             st.write("User: ",message.content)
#         else:
#             st.write("Reply: ",message.content)


# def main():
#     st.set_page_config("SEEKR: Information Retrieval System")
#     st.header("SEEKR: Information Retrieval System")

#     user_question = st.text_input("Ask a Question from your PDF files")

#     if "conversation" not in st.session_state:
#         st.session_state.conversation = None
#     if "chatHistory" not in st.session_state:
#         st.session_state.chatHistory = None
#     if user_question:
#         user_input(user_question)

#     with st.sidebar:
#         st.title("Menu:")
#         pdf_docs = st.file_uploader("Upload your PDF files and click on submit & process button", accept_multiple_files=True)
#         if st.button("Submit & Process"):
#             with st.spinner("Processing.."):
#                 time.sleep(2)
#                 raw_text = get_pdf_text(pdf_docs)
#                 text_chunks = get_text_chunks(raw_text)
#                 vector_store = get_vector_store(text_chunks)
#                 st.session_state.conversation = get_conversational_chain(vector_store)
#                 st.success("Done")

# if __name__ == "__main__":
#     main()

import streamlit as st
import time
from src.helper import get_pdf_text, get_text_chunks, get_vector_store, get_conversational_chain


def user_input(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chatHistory = response['chat_history']
    for i, message in enumerate(st.session_state.chatHistory):
        if i % 2 == 0:
            st.markdown(f'<div class="user-msg">🧑‍💼 <b>User:</b> {message.content}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bot-msg">🤖 <b>SEEKR:</b> {message.content}</div>', unsafe_allow_html=True)

def main():
    st.set_page_config("SEEKR", page_icon="📚", layout="wide")

    st.title("📚 SEEKR: Smart Information Retrieval from PDFs")

    # App Info
    st.markdown("""
    **SEEKR** is an AI assistant that lets you **upload PDFs** and ask questions about their content using **natural language**.
    - ⚡ Fast PDF parsing and chunking
    - 🔍 Search via FAISS & Gemini AI
    - 💬 Multi-turn conversation support
    """)

    st.subheader("💬 Ask a Question")

    # user_question = st.text_input("Type your question here...")

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory = None
    # if user_question:
    #     user_input(user_question)
    with st.form("chat_form", clear_on_submit=True):
        user_question = st.text_input("💬 Ask a question from your PDF documents:")
        submitted = st.form_submit_button("Send")
        if submitted and user_question:
            user_input(user_question)  # Shows the response immediately

    with st.sidebar:
        st.title("🧷 Upload Zone")
        pdf_docs = st.file_uploader("Upload your PDF files and click on submit & process button", accept_multiple_files=True, type=["pdf"])
        if st.button("📥 Submit & Process"):
            with st.spinner("Processing PDFs..."):
                time.sleep(1.5)
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                vector_store = get_vector_store(text_chunks)
                st.session_state.conversation = get_conversational_chain(vector_store)
                st.success("✅ Ready to Chat!")

    st.markdown("---")
    st.markdown("<center>🧠 Powered by LangChain + Gemini | SEEKR © 2025</center>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
