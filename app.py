import pickle
import streamlit as st
import requests

# Function to fetch movie poster
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# Function to recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

# Streamlit layout
st.set_page_config(page_title="Content Based Movie Recommender System", page_icon="🎬")

# Main header and description
st.title('Content Based Movie Recommender System')
st.write("Discover your next favorite movie!")

# Movie selection dropdown
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movies['title'].values  # Use movies['title'].values instead of undefined movie_list
)

# Recommendation button
if st.button('Show Recommendations'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    
    # Display recommendations in a row of cards
    col1, col2, col3, col4, col5 = st.columns(5)
    
    for i in range(5):
        with locals()[f"col{i+1}"]:
            st.image(recommended_movie_posters[i], caption=recommended_movie_names[i], use_column_width=True)

# Add some styling to the recommendation cards
st.markdown(
    """
    <style>
        .st-image {
            border-radius: 10px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s;
        }
        .st-image:hover {
            transform: scale(1.05);
        }
    </style>
    """,
    unsafe_allow_html=True
)
