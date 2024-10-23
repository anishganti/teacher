# bring in our LLAMA_CLOUD_API_KEY
from dotenv import load_dotenv

from llama_parse import LlamaParse
from llama_index.core.node_parser import MarkdownNodeParser
from llama_index.core import SimpleDirectoryReader, Settings, VectorStoreIndex

from llama_index.llms.nvidia import NVIDIA
from llama_index.embeddings.nvidia import NVIDIAEmbedding
from llama_index.postprocessor.nvidia_rerank import NVIDIARerank

load_dotenv()
Settings.text_splitter = SentenceSplitter(chunk_size=500)
Settings.llm = NVIDIA(model="meta/llama3-70b-instruct")
Settings.embed_model = NVIDIAEmbedding(model="NV-Embed-QA", truncate="END")

parser = LlamaParse(
    result_type="markdown"
)

# use SimpleDirectoryReader to parse our file
file_extractor = {".pdf": parser}
documents2 = SimpleDirectoryReader(
    "./data", file_extractor=file_extractor
).load_data()

index2 = VectorStoreIndex.from_documents(documents2)
query_engine2 = index2.as_query_engine(similarity_top_k=20)

response = query_engine2.query(
    "What was the net gain in housing units in the Mission in 2021?"
)

query_engine3 = index2.as_query_engine(
    similarity_top_k=40, node_postprocessors=[NVIDIARerank(top_n=10)]
)

response = query_engine3.query(
    "How many affordable housing units were completed in 2021?"
)

print(response)


