from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
import pandas as pd
import streamlit as st
import os
import glob
from docx import Document

from func.read_data_from_file import (
    read_csv,
    read_excel,
    read_word,
    get_recomendation_id,
)


st.set_page_config(
    page_title="Movie Recommendation", page_icon=":movie_camera:", layout="wide"
)

st.title("Film Recommendation With AI :robot_face:")

st.header("Upload file")

uploaded_file = st.file_uploader(
    label="You can upload one file with extentions .csv, .xlsx, .docx",
    type=["csv", "xlsx", "docx"],
)

if "db_movies" not in st.session_state:
    st.session_state.db_movies = None

if uploaded_file is not None:
    # if not None remove all files from directory
    files_in_temp = glob.glob(os.path.join("data/temp_files/", "*"))
    for file in files_in_temp:
        try:
            os.remove(file)
            print(f"{file} removed")
        except Exception as e:
            print(f"Error removig {file}: {e}")

    # upload new file
    file_name = uploaded_file.name
    if file_name.endswith(".csv"):
        temp_file = f"data/temp_files/{file_name}"

        csv_file = read_csv(
            temp_file=temp_file, uploaded_file=uploaded_file, file_name=file_name
        )

        csv_file.to_csv(
            f"data/temp_files/one_col.txt",
            index=False,
            header=False,
            lineterminator="\n",
        )

    elif file_name.endswith(".xlsx"):
        temp_file = f"data/temp_files/{file_name}"

        excel_file = read_excel(
            temp_file=temp_file, uploaded_file=uploaded_file, file_name=file_name
        )

        excel_file.to_csv(
            f"data/temp_files/one_col.txt",
            index=False,
            header=False,
            lineterminator="\n",
        )

    else:
        temp_file = f"data/temp_files/{file_name}"

        word_file = read_word(
            temp_file=temp_file, uploaded_file=uploaded_file, file_name=file_name
        )

        word_file.to_csv(
            f"data/temp_files/one_col.txt",
            index=False,
            header=False,
            lineterminator="\n",
        )

        st.write("New file uploaded and processed")

        # preapare data for vectorization
        raw_data = TextLoader(r"data\temp_files\one_col.txt", encoding="utf-8").load()
        spliter = CharacterTextSplitter(chunk_size=0, chunk_overlap=0, separator="\n")
        splited_documents = spliter.split_documents(raw_data)

        st.write("Vectorizing and creating FAISS database...")

        embeddings = OllamaEmbeddings(model="nomic-embed-text")
        db_movies = FAISS.from_documents(
            documents=splited_documents, embedding=embeddings
        )

        db_movies.save_local("movies_db")
        st.session_state.db_movies = db_movies
        st.write("Database created successfully!")

# get data from created db
if st.session_state.db_movies is None:
    try:
        embeddings = OllamaEmbeddings(model="nomic-embed-text")
        st.session_state.db_movies = FAISS.load_local(
            "movies_db", embeddings, allow_dangerous_deserialization=True
        )
    except Exception as e:
        st.warning("No database found...")

query = st.text_input("What kind of film do you want to watch?")
if query and st.session_state.db_movies is not None:
    answer = st.session_state.db_movies.similarity_search(query=query, k=3)

    st.dataframe(get_recomendation_id(answer))
