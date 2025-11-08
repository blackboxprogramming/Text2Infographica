from transformers import pipeline

# This uses a model to extract keywords that help build a focused YouTube query
def generate_search_query(summary):
    keyword_extractor = pipeline("text2text-generation", model="google/flan-t5-small")

    prompt = f"Extract a concise YouTube search query from this summary:\n{summary}"
    response = keyword_extractor(prompt, max_new_tokens=20)[0]["generated_text"]
    return response.strip()
