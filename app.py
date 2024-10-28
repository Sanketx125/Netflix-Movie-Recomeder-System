import streamlit as st
import pickle
import pandas as pd

def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]  
    distances = similarity[movie_index]
    movies_list = sorted( list( enumerate(distances)), reverse=True, key = lambda x : x[1])[1:6]

    recemmended_movies = []
    for i in movies_list:
        movie_id = i[0]
        # poster fetching from api
        recemmended_movies.append(movies.iloc[i[0]].title)
    return recemmended_movies

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title("Movies Recommender Systerm")

Selected_movie_name = st.selectbox(
'" Uncover the magic of cinema—search for a movie and dive into its story with just a click! "',
movies['title'].values)


if st.button('Recommend'):
    recemmendations = recommend(Selected_movie_name)
    for i in recemmendations:
        st.write(i)