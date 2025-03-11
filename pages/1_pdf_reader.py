from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain.chains.retrieval import create_retrieval_chain
from langchain_ollama import ChatOllama
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st

from func.pdf_project import load_pdf_document

st.set_page_config(page_title="PDF reader", page_icon=":closed_book:")
st.title("Ollama Project Dockument Reader")

upload_file = st.file_uploader("Upload PDF Document", type="pdf")

# get data from file
if upload_file is not None:
    temp_file = "data/temp_pdf/temp.pdf"
    with open(temp_file, "wb") as file:
        file.write(upload_file.getvalue())
        file_name = upload_file.name

    chunks = load_pdf_document(temp_file)

    st.write("Reading document...")

    embedding = OllamaEmbeddings(model="nomic-embed-text")

    vector_db = FAISS.from_documents(chunks, embedding)

    retriever = vector_db.as_retriever()

    llm = ChatOllama(model="llama3.2:3b")

    system_prompt = (
        "You are helpful assistant. Use the given context to answer the question."
        "If you don't know the answer, say you don't know."
        "{context}"
    )

    # Prompt template
    prompt = ChatPromptTemplate.from_messages(
        [("system", system_prompt), ("human", "{input}")]
    )

    question_answer_chain = create_stuff_documents_chain(llm, prompt)

    chain = create_retrieval_chain(retriever, question_answer_chain)

    question = st.text_input("Ask questions about the document: ")

    if question is not None:
        response = chain.invoke({"input": question})["answer"]

        st.write(response)
