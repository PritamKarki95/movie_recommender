import os
from joblib import load
from sklearn.metrics.pairwise import cosine_similarity

# Load model files
BASE_DIR = os.path.dirname(__file__)
vecto = load(os.path.join(BASE_DIR, 'vecto.joblib'))
tfidf_matrix = load(os.path.join(BASE_DIR, 'tfidf_matrix.joblib'))
movies = load(os.path.join(BASE_DIR, 'movies_df.joblib'))

# Recommend function
def recommend(names='', genre='', crew='', language=''):
    user_input = f"{names} {genre} {crew} {language}".lower()
    user_vect = vecto.transform([user_input])
    scores = cosine_similarity(user_vect, tfidf_matrix).flatten()
    ind = scores.argsort()[-6:][::-1]

    recommendations = []
    for i in ind[1:6]:
        recommendations.append(movies.iloc[i]['names'])

    return recommendations
