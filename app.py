import streamlit as st
import pickle
import requests
import os
from dotenv import load_dotenv

# ---------------- ENV LOAD ----------------
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    layout="wide",
    page_title="Movie Recommender",
    page_icon="🎬"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to bottom, #0f2027, #203a43, #2c5364);
    color: white;
}
h1 {
    color: #00d2ff;
    text-align: center;
    font-family: 'Trebuchet MS', sans-serif;
    text-shadow: 2px 2px 4px #000000;
}
.stSelectbox label {
    color: #ffffff !important;
    font-size: 1.2rem;
}
div.stButton > button {
    background: linear-gradient(45deg, #ff00cc, #333399);
    color: white;
    border: none;
    padding: 0.5rem 2rem;
    border-radius: 25px;
    font-size: 16px;
    font-weight: bold;
    width: 100%;
    transition: all 0.3s ease;
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
}
div.stButton > button:hover {
    transform: scale(1.02);
    box-shadow: 0 6px 20px rgba(255, 0, 204, 0.4);
    border: 1px solid white;
}
.movie-caption {
    text-align: center;
    font-weight: 600;
    color: #e0e0e0;
    margin-top: 5px;
    font-size: 14px;
    background-color: rgba(0,0,0,0.5);
    padding: 5px;
    border-radius: 5px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# ---------------- IMAGE FETCH ----------------
def fetch_image(movie_id):
    if not TMDB_API_KEY:
        return "https://via.placeholder.com/500x750?text=No+API+Key"

    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}&language=en-US"
        response = requests.get(url, timeout=5)
        data = response.json()

        if data.get('poster_path'):
            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
        else:
            return "https://via.placeholder.com/500x750?text=No+Image"
    except:
        return "https://via.placeholder.com/500x750?text=Error"

# ---------------- RECOMMENDATION ----------------
def recommend(movie):
    similar_movies_list = []
    similar_movies_poster = []

    movie_index = movies[movies['title'] == movie].index[0]
    distances = list(enumerate(similarity[movie_index]))
    recommend_movies_list_index = sorted(distances, reverse=True, key=lambda x: x[1])[1:6]

    for index in recommend_movies_list_index:
        similar_movies_list.append(movies.iloc[index[0]]['title'])
        similar_movies_poster.append(fetch_image(movies.iloc[index[0]].movie_id))

    return similar_movies_list, similar_movies_poster

# ---------------- UI ----------------
st.title("🎬 Movie Recommendation System")

movies_name = movies['title'].values

col_spacer1, col_main, col_spacer2 = st.columns([1, 2, 1])

with col_main:
    selected_movie = st.selectbox("Select a movie you like:", movies_name)
    st.write("")

    if st.button("🚀 Show Recommendations"):
        name, poster = recommend(selected_movie)

        st.markdown("---")
        st.subheader("Top 5 Picks for You:")
        st.write("")

        col1, col2, col3, col4, col5 = st.columns(5)

        cols = [col1, col2, col3, col4, col5]

        for i in range(5):
            with cols[i]:
                st.image(poster[i], use_container_width=True)
                st.markdown(f"<div class='movie-caption'>{name[i]}</div>", unsafe_allow_html=True)
