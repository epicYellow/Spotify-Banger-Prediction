import streamlit as st
import joblib
import numpy as np
import pandas as pd

model = joblib.load("Spotify_SongDanceability_Predicter.pkl")

model_info = joblib.load("model_info.pkl")

print(model_info["features"])

st.title("Predict a Songs Danceability")
st.write("This is a ridge linear regression model")
st.write("Due to the small dataset size the accuracy is 34%")

bpm = st.number_input(f"Enter Song bpm", min_value=65, max_value=300)
energy_ = st.number_input(f"Enter Song Energy %", min_value=1, max_value=100)
acousticness_ = st.number_input(f"Enter Accousticness %", min_value=1, max_value=100)
in_spotify_playlists = st.number_input(f"Enter in total spotify playlist", min_value=1)
speechiness_ = st.number_input(f"Enter Speechiness %", min_value=1, max_value=100)
valence_ = st.number_input(f"Enter Song Positive %", min_value=1, max_value=100)
artist_count = st.number_input(f"Enter artist count", min_value=1, max_value=10)

test_data = {
    'bpm': np.log(bpm),
    'energy_%': energy_,
    'acousticness_%': acousticness_,
    'in_spotify_playlists': np.log(in_spotify_playlists),
    'speechiness_%': np.log(speechiness_),
    'valence_%': valence_,
    'artist_count': np.log(artist_count)
}

input_df = pd.DataFrame(test_data, index=[0])

if st.button("Make Prediction"):
    prediction = model.predict(input_df)
    st.write(f"Predicted Danceability: {prediction[0][0]} %")






