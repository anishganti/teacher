from llama_index.core.node_parser import MarkdownNodeParser
from llama_index.core import Document
from openai import OpenAI
from backend.utils.models import get_embedding

def chunk_document(document: Document) -> list:
    """
    Break a document into smaller chunks of text, represented as a list of nodes.

    Args:
        document (Document): The document to break into nodes.

    Returns:
        list: A list of nodes representing the input document.
    """
    parser = MarkdownNodeParser()
    nodes = parser.get_nodes_from_documents([document])
    generate_node_ids(nodes)
    return nodes

def generate_node_ids(nodes: list) -> None:
    """
    Generate node_ids for a list of nodes.

    Assigns a unique identifier to each node in the form
    {document_name}_{page_number}_{node_number}, where document_name is the name
    of the document the node was extracted from, page_number is the page number
    the node was extracted from within the document, and node_number is the
    sequential number of the node within the document.

    Args:
        nodes (list): The list of nodes to assign ids to.
    """
    for node_number, node   in enumerate(nodes, start=1):
        node.metadata["node_number"] = node_number
        document_name = node.metadata["file_name"]
        page_number = node.metadata["page_number"]
        node.metadata["node_id"] = f"{document_name}_{page_number}_{node_number}"

def chunk_and_embed(document: str) -> str:
    """
    Process a document by chunking it into nodes, then embedding each node.

    Args:
        document (str): The document to be processed.

    Returns:
        tuple: A tuple containing three lists:
            - documents: List of text chunks from the document.
            - embeddings: List of embeddings corresponding to each text chunk.
            - metadatas: List of metadata for each text chunk.
    """
    nodes = chunk_document(document)
    documents = [node.text for node in nodes]
    embeddings = [get_embedding(node.text, input_type="passage") for node in nodes]
    metadatas = [node.metadata for node in nodes]
    ids = [node.metadata["node_id"] for node in nodes]

    return documents, embeddings, metadatas, ids