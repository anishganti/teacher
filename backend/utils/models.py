from openai import OpenAI
import os
import requests

client = OpenAI(
    api_key=os.environ["NVIDIA_API_KEY"],
    base_url="https://integrate.api.nvidia.com/v1"
)

def get_embedding(text: str, input_type: str) -> str:
    """
    Get a semantic embedding for a given text passage.

    Args:
        text (str): The text passage to embed.

    Returns:
        str: The semantic embedding of the text as a string.
    """
    response = client.embeddings.create(
        input=[text],
        model="nvidia/nv-embedqa-mistral-7b-v2",
        encoding_format="float",
        extra_body={"input_type": input_type, "truncate": "NONE"}
    )

    return response.data[0].embedding

def chat(query: str): 
    """
    Send a query to the LLM and get the response.

    Args:
        query (str): The query to send to the LLM.

    Returns:
        str: The response from the LLM.
    """
    
    completion = client.chat.completions.create(
        model="meta/llama-3.1-8b-instruct",
        messages=[{"role":"user","content":f"{query}"}],
        temperature=0.2,
        top_p=0.7,
        max_tokens=1024,
        stream=False
    )

    return completion.chunk.choices[0].delta.content

def rerank(documents: list, query: str) -> list:
    invoke_url = "https://ai.api.nvidia.com/v1/retrieval/nvidia/nv-rerankqa-mistral-4b-v3/reranking"

    headers = {
        "Authorization": os.environ["NVIDIA_API_KEY"],
        "Accept": "application/json",
    }

    payload = {
    "model": "nvidia/nv-rerankqa-mistral-4b-v3",
    "query": {
        "text": f"{query}"
    },
    "passages": [{"text": f"{document}"} for document in documents]
    }

    session = requests.Session()

    response = session.post(invoke_url, headers=headers, json=payload)

    response.raise_for_status()
    response_body = response.json()
    return response_body["rankings"]