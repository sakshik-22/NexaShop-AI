from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_recommendations(target_id: int, products: list):
    """
    Given a target product ID and a list of all products,
    returns the top 4 recommended items based on content similarity.
    """
    if len(products) < 2:
        return []

    # Prepare texts by combining category name and description
    texts = []
    target_idx = None

    for idx, p in enumerate(products):
        if p.id == target_id:
            target_idx = idx
        # basic string rep
        cat_name = p.category.name if p.category else ""
        texts.append(f"{cat_name} {p.name} {p.description}")

    if target_idx is None:
        return []

    vectorizer = TfidfVectorizer(stop_words='english')
    try:
        tfidf_matrix = vectorizer.fit_transform(texts)
    except ValueError:
       return [] # in case texts are empty or only stopwords

    cos_sim = cosine_similarity(tfidf_matrix[target_idx:target_idx+1], tfidf_matrix).flatten()

    # Get indices sorted by similarity (descending), omitting the target item itself
    similar_indices = cos_sim.argsort()[::-1]
    
    recommendations = []
    for i in similar_indices:
        if i != target_idx:
            recommendations.append(products[i])
        if len(recommendations) == 4: # return top 4
            break

    return recommendations
