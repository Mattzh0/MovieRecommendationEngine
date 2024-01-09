import streamlit as st
import pickle
import requests

st.markdown("<h1 style='text-align: center;'>Movie Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Built by Matthew Zhang</h2>", unsafe_allow_html=True)
st.image("banner.jpg", caption="", use_column_width=True, output_format="JPEG")

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list=movies['title'].values

def get_poster(movie_id):
  api_key="1bd0058d27c0ecdde1eca207ea286ef0"
  url = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US".format(movie_id, api_key)
  data=requests.get(url)
  data=data.json()
  poster_path = data['poster_path']
  full_path = "https://image.tmdb.org/t/p/w500" + poster_path
  return full_path

def recommend(movie):
  index = movies[movies['title']==movie].index[0]

  distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])

  rec_movies = []
  rec_posters= []
  for i,d in distances[1:6]:
    movies_id = movies.iloc[i].id
    rec_movies.append(movies.iloc[i].title)
    rec_posters.append(get_poster(movies_id))
  return rec_movies, rec_posters

selectvalue = st.selectbox("Select a movie from the dropdown to show recommended movies!", movies_list)

if st.button("Show Recommendations!"):
  movie_name, movie_poster = recommend(selectvalue)
  c1, c2, c3, c4, c5 = st.columns(5)
  with c1:
    st.text(movie_name[0])
    st.image(movie_poster[0])
  with c2:
    st.text(movie_name[1])
    st.image(movie_poster[1])
  with c3:
    st.text(movie_name[2])
    st.image(movie_poster[2])
  with c4:
    st.text(movie_name[3])
    st.image(movie_poster[3])
  with c5:
    st.text(movie_name[4])
    st.image(movie_poster[4])