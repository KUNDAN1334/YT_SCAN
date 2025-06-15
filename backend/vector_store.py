import faiss
import numpy as np

def create_faiss_index(embeddings):
    embeddings = np.array(embeddings).astype('float32')
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

def get_top_k(index, query_embedding, k=5):
    query_embedding = np.array(query_embedding).astype('float32')
    D, I = index.search(query_embedding, k)
    return I[0]