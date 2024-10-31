from llama_index.core import Document
from llama_index.core.schema import MetadataMode
def serialize(document):
    """
    Serializes a document object.

    Args:
        document (Document): A document object.

    Returns:
        dict: A dictionary representing the document.
    """

    document_dict = {
            "metadata": document.metadata,
            "text": document.text,
            "id_": document.id_,
            "excluded_embed_metadata_keys": document.excluded_embed_metadata_keys,
            "excluded_llm_metadata_keys": document.excluded_llm_metadata_keys,
            "relationships": document.relationships
    }

    return document_dict

def deserialize(document_dict):
    """
    Deserializes a document dictionary.

    Args:
        document_dict (dict): A dictionary representing the document.

    Returns:
        Document: A document object.
    """

    document = Document(
        text=document_dict["text"],
        metadata=document_dict["metadata"],
        id_=document_dict["id_"],
        excluded_embed_metadata_keys=document_dict["excluded_embed_metadata_keys"],
        excluded_llm_metadata_keys=document_dict["excluded_llm_metadata_keys"],
        relationships=document_dict["relationships"]
    )

    return document

    