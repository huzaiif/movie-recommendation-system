import streamlit as st
import pickle
import pandas as pd
import requests



def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=120e8ca156920dd61f4c98bc6628a2cb&language=en-US"
        response = requests.get(url, timeout=10)
        response.raise_for_status()   # raises error for bad response
        data = response.json()
        return "https://image.tmdb.org/t/p/w500/" + data.get('poster_path', "")
    except Exception as e:
        print("Error fetching poster:", e)
        return "https://via.placeholder.com/500x750?text=No+Image"


def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    'Select Movie?',
    movies['title'].values)

if st.button("Recommend"):
    names,posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])