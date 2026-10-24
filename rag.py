import json
import re
# import urllib.request
import requests

API_KEY = ""  # enter your OpenRouter token here
EMBED_MODEL = "nvidia/nemotron-3-embed-1b:free"
GUIDE_FILE = "user_guide.md"


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    return dot / (((sum(x * x for x in a) ** 0.5) or 1) * ((sum(x * x for x in b) ** 0.5) or 1))


def embed(texts):
    # request = urllib.request.Request(
    #     "https://openrouter.ai/api/v1/embeddings",
    #     data=json.dumps({"model": EMBED_MODEL, "input": texts}).encode(),
    #     headers={"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"},
    # )
    response = requests.post(
        "https://openrouter.ai/api/v1/embeddings",
        data=json.dumps({"model": EMBED_MODEL, "input": texts}).encode(),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {API_KEY}"},
    )
    response = response.json()
    data = sorted(response["data"], key=lambda d: d["index"])
    return [d["embedding"] for d in data]


with open(GUIDE_FILE, encoding="utf-8") as f:
    guide = f.read()
chunks = [c for c in map(str.strip, re.split(r"\n(?=#+ )", guide)) if "\n" in c]
vectors = embed(chunks)

question = input("Your question: ")
query_vector = embed([question])[0]

best_chunk = max(zip(chunks, vectors), key=lambda pair: cosine(pair[1], query_vector))[0]
print()
print(best_chunk)
