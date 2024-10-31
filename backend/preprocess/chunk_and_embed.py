from llama_index.core.node_parser import MarkdownNodeParser
from llama_index.core import Document
from openai import OpenAI
import os



def get_nodes(document: Document) -> list:
    """
    Break a document into smaller chunks of text, represented as a list of nodes.

    Args:
        document (Document): The document to break into nodes.

    Returns:
        list: A list of nodes representing the input document.
    """
    parser = MarkdownNodeParser()
    nodes = parser.get_nodes_from_documents([document])
    print(len(nodes))
    return nodes

def get_embedding(text: str) -> str:
    """
    Get a semantic embedding for a given text passage.

    Args:
        text (str): The text passage to embed.

    Returns:
        str: The semantic embedding of the text as a string.
    """
    client = OpenAI(
    api_key=os.environ["NVIDIA_API_KEY"],
    base_url="https://integrate.api.nvidia.com/v1"
    )

    response = client.embeddings.create(
        input=[text],
        model="nvidia/nv-embedqa-mistral-7b-v2",
        encoding_format="float",
        extra_body={"input_type": "passage", "truncate": "NONE"}
    )

    return response.data[0].embedding

def chunk_and_embed(document: str) -> str:
    nodes = get_nodes(document)
    embeddings = [get_embedding(node) for node in nodes]
    return nodes, embeddings