from preprocess.pdf_to_markdown import parse_documents, add_page_numbers, store_documents
from preprocess.chunk_and_embed import chunk_and_embed
from preprocess.index_into_chroma import index_into_chroma
from utils.document_serializer import serialize, deserialize
from dotenv import load_dotenv
import json


load_dotenv()
def main():
    """
    Main function to parse documents from a specified folder and store them in a JSON file.

    This function defines the folder path, uses the `parse_documents` function to read and parse the files
    in the folder, and then stores the parsed documents using the `store_documents` function.
    """
    #folder = "/Users/anishganti/Desktop/teacher/backend/storage/raw/deeplearningbook"
    #folder = "/Users/anishganti/Desktop/teacher/backend/storage/processed"
    #documents = parse_documents()
    #documents = add_page_numbers(documents)
    #store_documents(folder,documents)

    
    document_path = '/Users/anishganti/Desktop/teacher/backend/storage/processed/deeplearningbooksample.pdf/deeplearningbooksample.pdf_1.json'
    
    with open(document_path, 'r') as f:
        document = json.load(f)
        document = deserialize(document)
        documents, embeddings, metadatas, ids = chunk_and_embed(document)
        index_into_chroma("deeplearningbooksample", documents, embeddings, metadatas, ids)

if __name__ == "__main__":
    main()