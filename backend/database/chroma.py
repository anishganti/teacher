import chromadb
from utils.embeddings import get_embedding

class ChromaDBClient: 
    def __init__(self, path='/Users/anishganti/Desktop/teacher/backend/storage/embeddings'):
        """
        Initialize the ChromaDB client.

        The client is created with the default path of /Users/anishganti/Desktop/teacher/backend/storage/embeddings.
        """
        self.client = self.create_client(path)

    def create_client(self, path):
        """
        Create a ChromaDB client that persists to disk.

        Args:
            path (str): The path to the directory where the data will be stored.
                Defaults to '/Users/anishganti/Desktop/teacher/backend/storage/embeddings'.

        Returns:
            chromadb.PersistentClient: The client.
        """
        client = chromadb.PersistentClient(path=path)
        return client    
    
class ChromaDBCollection:
    def __init__(self, name):
        self.client = ChromaDBClient()
        self.collection = self.get_or_create_collection(name)

    def get_or_create_collection(self, name):
        """
        Get or create a collection with the given name.

        Args:
            name (str): The name of the collection.

        Returns:
            Collection: The collection object.
        """
        collection = self.client.client.get_or_create_collection(name=name)
        return collection

    def query(self, query_text, n_results=1):
        """
        Query the collection with the given query texts and return the top n results.

        Args:
            query_text (str): The query text.
            n_results (int): The number of results to return.

        Returns:
            List[Document]: The list of results.
        """
        query_embedding = get_embedding(query_text)

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )

    def add(self, documents, embeddings, metadatas, ids):
        """
        Add the given documents, embeddings, metadatas, and ids to the collection.

        Args:
            documents (List[Document]): The documents to add.
            embeddings (List[Embeddings]): The embeddings to add.
            metadatas (List[Metadata]): The metadatas to add.
        """
        self.collection.add(
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas, 
            ids=ids
        )

