# 🎬 Movie Recommendation System (Streamlit)

A **Content-Based Movie Recommendation Web Application** built using **Python** and **Streamlit** that suggests similar movies based on user selection.  
The system uses a **pre-computed similarity matrix** and fetches real-time movie posters from the **TMDB API** to deliver a fast, interactive, and visually appealing experience.

---

## 🚀 Features

- Interactive Web UI using **Streamlit**
- Content-Based Recommendation Engine
- Displays **Top 5 Similar Movies**
- Real-time Movie Poster Fetching (TMDB API)
- Custom CSS Styling for Modern UI
- Fast and Lightweight Performance
- Error Handling for Missing Images

---

## 🧠 How It Works

1. User selects a movie from the dropdown.
2. System finds the movie index in the dataset.
3. Uses a **Cosine Similarity Matrix** to calculate similarity.
4. Sorts similarity scores in descending order.
5. Selects the top 5 most similar movies.
6. Fetches movie posters from the TMDB API.
7. Displays movie titles and images in a clean column layout.

---

## 🛠 Tech Stack

### Frontend / UI
- Streamlit
- Custom CSS Styling

### Backend / Logic
- Python
- Pandas
- NumPy

### Machine Learning
- Scikit-Learn
- Cosine Similarity

### API Integration
- TMDB (The Movie Database)

---

## 📁 Project Structure

```
movie-recommender-streamlit/
├── app.py
├── notebook.ipynb
├── movies.pkl
├── similarity.pkl
│
├── data/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── assets/
│
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```


## 📊 Dataset

**Dataset Source:** TMDB 5000 Movie Dataset (Kaggle)

Files Used:
- `tmdb_5000_movies.csv`
- `tmdb_5000_credits.csv`

---

## ⚙️ Installation & Setup

### 1. Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/movie-recommender-streamlit.git
cd movie-recommender-streamlit
2. Create Virtual Environment
python -m venv venv
Activate Environment:

Windows

venv\Scripts\activate
Mac/Linux

source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Run Application
streamlit run app.py
Open in browser:

http://localhost:8501
📦 Requirements
streamlit
pandas
numpy
scikit-learn
requests
🔑 TMDB API Key
This project uses TMDB API to fetch movie posters.

Get a free API key from:
https://www.themoviedb.org/settings/api

Replace the API key inside app.py with your own key if needed.

🎯 Recommendation Algorithm
Content-Based Filtering

Cosine Similarity

TF-IDF / Count Vectorization (during model building)

Pre-computed Similarity Matrix for fast runtime performance

⚠️ Limitations
Works only for movies present in dataset

Similarity depends on dataset quality

Poster fetching requires internet connection

No genre or user preference filters yet

🔮 Future Improvements
Genre-based filtering

User login & personalization

Cloud deployment (Streamlit Cloud / Render / Heroku)

Larger dataset integration

Hybrid Recommendation System

Trailer preview integration

🧪 Optional Enhancements
Loading spinner while fetching posters

Search bar instead of dropdown

Dark / Light theme toggle

Favorites & Watchlist feature

Pagination for results

📜 License
This project is licensed under the MIT License.

👨‍💻 Author
Kalyan Burada

⭐ If you find this project useful, consider giving it a star!

---

This version is:
- Clean
- Properly formatted
- Recruiter-friendly
- Ready for portfolio / resume / placements.