# ML-Powered Movie Recommendation System
A full-stack movie recommendation system built with Django, HTML/CSS/JS, and a machine learning model using Content-Based Filtering. Users can select their preferences (genre, language, crew, reference movie) and get personalized movie suggestions with poster images and ratings using the TMDB API.

## 🚀 Features
🎞 Recommend movies based on:

Genre

Actor / Crew

Original Language

Reference Movie

🧠 Machine Learning with Content-Based Filtering (scikit-learn)


🌐 TMDB API integration for:

Movie posters

Ratings

Details



💻 Frontend built with HTML, CSS, and JavaScript

🔗 Backend handled with Django (Python)

⚙️ Installation
1. Clone the repo
git clone 
cd movie-recommendation-system

2. Create and activate virtual environment (optional but recommended)
python -m venv env
source env/bin/activate     # On Windows: env\Scripts\activate

3. Install dependencies
pip install -r requirements.txt
If you don’t have requirements.txt, list the packages you used manually like:
pip install django scikit-learn pandas requests

4. Set your TMDB API key
Create a .env file or add it in settings.py:
TMDB_API_KEY = 'your_tmdb_api_key_here'

5. Run the server
python manage.py runserver

## 🧠 Machine Learning Logic
The model uses Content-Based Filtering.

Features used: genre, crew, orig_lang, and reference movie.

Movie similarity is calculated using TF-IDF or cosine similarity.

Built with pandas, scikit-learn.

## 📦 API Integration
TMDB API is used to fetch real-time:

Movie posters

Ratings

Movie metadata

## 💡 How to Use
Go to the homepage.

Select your preferred genre, actor, language, and a movie you like.

Click “Recommend.”

Scroll to see suggested movies with posters and ratings.



