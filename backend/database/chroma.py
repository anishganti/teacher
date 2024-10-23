import chromadb

client = chromadb.PersistentClient(path='/Users/anishganti/Desktop/teacher/backend/storage/embeddings)

# print(client.list_collections())

collection = client.get_collection(name="test")

results = collection.query(
    query_texts=["This is a query document about hawaii"], # Chroma will embed this for you
    n_results=4 # how many results to return
)

print(results)

#create a new collection
#call preprocessing to create chunks 
#call chroma to create embeddings 

