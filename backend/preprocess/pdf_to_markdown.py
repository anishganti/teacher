import json
import os
from dotenv import load_dotenv
from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader
from utils.document_serializer import serialize

load_dotenv()

def create_parser(): 
    """
    Creates a LlamaParse parser for markdown format, splitting by page.

    Returns:
        dict: A file extractor with a single key-value pair, where
            the key is the file extension ".pdf" and the value is the
            LlamaParse parser.
    """
    parser = LlamaParse(
        result_type="markdown",
        split_by_page=True
    )

    file_extractor = {".pdf": parser}

    return file_extractor

def parse_documents():
    """
    Reads all files in a given folder and parses them using the LlamaParse parser.

    Args:
        folder (str): The path to the folder containing the files to parse.

    Returns:
        list: A list of documents, where each document is an object containing
            the text content of a page of a file, as well as additional metadata such as the file name.
    """
    documents = SimpleDirectoryReader(
        input_files=['/Users/anishganti/Desktop/teacher/backend/storage/raw/deeplearningbooksample.pdf'], file_extractor=create_parser()
    ).load_data()

    return documents

def add_page_numbers(documents):
    """
    Adds page numbers to each document in a list of documents.

    Args:
        documents (list): A list of documents, where each document is an object containing
            the text content of a page of a file, as well as additional metadata such as the file name.

    Returns:
        list: A list of documents, where each document is an object containing
            the text content of a page of a file, as well as additional metadata such as the file name
            and the page number.
    """
    for page_number, document in enumerate(documents, start=1):
        document.metadata["page_number"] = page_number

    return documents

def store_documents(folder, documents):
    """
    Stores the documents in a JSON file.

    Args:
        documents (list): A list of documents, where each document is an object containing
            the text content of a page of a file, as well as additional metadata such as the file name.
    """

    for document in documents:

        document_json = serialize(document)
        file_name = document.metadata["file_name"]
        page_num = document.metadata["page_number"]

        if not os.path.exists(f"{folder}/{file_name}"):
            os.makedirs(f"{folder}/{file_name}")

        with open(f"{folder}/{file_name}/{file_name}_{page_num}.json", "w") as f:
            json.dump(document_json, f)
