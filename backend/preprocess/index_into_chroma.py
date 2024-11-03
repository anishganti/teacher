from database.chroma import ChromaDBCollection
def index_into_chroma(collection_name: str, documents: list, embeddings: list, metadatas: list, ids: list):
    """
    Index a list of documents, their embeddings, and metadata into a Chroma collection.

    Args:
        collection_name (str): The name of the Chroma collection to index into.
        documents (list): A list of strings, each of which is a document to index.
        embeddings (list): A list of embeddings, one for each document in documents.
        metadatas (list): A list of metadata dictionaries, one for each document in documents.
        ids (list): A list of ids, one for each document in documents.

    Returns:
        None
    """
    collection = ChromaDBCollection(collection_name)
    collection.add(documents, embeddings, metadatas, ids)
