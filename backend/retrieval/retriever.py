from database.chroma import ChromaDBCollection
from utils.models import rerank

def retrieve(collection: str, query: str) -> None:
    """
    Retrieves documents from a collection that match the given query.

    Args:
        collection (str): The name of the collection to query.
        query (str): The query to search for.

    Returns:
        List of documents that match the query.
    """
    collection = ChromaDBCollection(collection)
    results = collection.query(query)
    rankings = rerank(results, query)

    reranked_results = []

    for i in range(len(rankings)):
        index = rankings[i]["index"]
        reranked_results.append(results[index])

    return reranked_results