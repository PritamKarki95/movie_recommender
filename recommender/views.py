import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
from .ml_model import recommend  # Your ML function

TMDB_API_KEY = settings.TMDB_API_KEY

def index(request):
    return render(request, 'index.html')

def get_movie_details(movie_name):
    """Search TMDB for movie by name and return poster, rating, and crew."""
    url = f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie_name}"
    response = requests.get(url).json()
    if response['results']:
        movie_id = response['results'][0]['id']
        title = response['results'][0]['title']
        poster_path = response['results'][0].get('poster_path')
        rating = response['results'][0].get('vote_average', 'N/A')

        # Get crew
        credits_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={TMDB_API_KEY}"
        credits_response = requests.get(credits_url).json()
        crew_members = credits_response.get('crew', [])
        cast_members = credits_response.get('cast', [])

        directors = [c['name'] for c in crew_members if c['job'] == 'Director']
        top_cast = [c['name'] for c in cast_members[:3]]  # Top 3 cast

        crew_info = ", ".join(directors + top_cast)

        return {
            'title': title,
            'poster': f"https://image.tmdb.org/t/p/original{poster_path}" if poster_path else '',
            'rating': rating,
            'crew': crew_info
        }
    else:
        return {
            'title': movie_name,
            'poster': '',
            'rating': 'N/A',
            'crew': 'N/A'
        }

def recommend_movies(request):
    name = request.GET.get('name', '')
    genre = request.GET.get('genre', '')
    crew = request.GET.get('crew', '')
    language = request.GET.get('language', '')

    # Your ML model returns a list of recommended movie titles
    recommended_titles = recommend(names=name, genre=genre, crew=crew, language=language)

    # Fetch full movie info for each title
    results = [get_movie_details(title) for title in recommended_titles]

    return JsonResponse({'recommendations': results})
