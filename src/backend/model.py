import chromadb
from langchain.llms import OpenAI

def connect_db():
    client = chromadb.Client()
    return client

def interpret_dream(dream_description):
    client = connect_db()
    collection = client.create_collection(name="dream_interpretations")

    # Sample data insertion (you can do this once or manage it separately)
    sample_data = [
        ("Dreaming of flying can symbolize freedom and escape.", "flying, freedom"),
        ("Seeing a snake in your dream may indicate hidden fears.", "snake, fear"),
        ("Water often represents emotions and the unconscious mind.", "water, emotions"),
    ]
    
    # Add sample data to the collection
    for text, tags in sample_data:
        collection.add(documents=[text], metadatas=[{"tags": tags}])

    # Query the collection for interpretations related to the dream description
    results = collection.query(query_texts=[dream_description], n_results=1)

    interpretation = "No relevant interpretation found."
    if results and results['documents']:
        interpretation = results['documents'][0]

    # Initialize OpenAI LLM
    llm = OpenAI(model='gpt-3.5-turbo')

    # Generate additional context or details using LLM
    response = llm(f"Provide more insights about this dream: {dream_description}")

    return interpretation, response