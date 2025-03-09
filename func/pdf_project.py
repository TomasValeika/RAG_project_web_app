from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def load_pdf_document(pdf):
    """
    Load pdf document and split into chunks
    """
    read_pdf = PyPDFLoader(pdf)
    document = read_pdf.load()

    split_text = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = split_text.split_documents(document)

    return chunks
