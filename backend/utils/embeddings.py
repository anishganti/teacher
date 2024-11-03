from openai import OpenAI
import os
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
