import streamlit as st
import joblib
import numpy as np
import pandas as pd

from funcs import calculate_impact

model = joblib.load("Spotify_SongDanceability_Predicter.pkl")

model_info = joblib.load("model_info.pkl")

print(model_info["features"])

st.title("Predict a Songs Danceability")
st.write("This is a ridge linear regression model")
st.write("Due to the small dataset size the accuracy is 34%")

coefficients = {
        'bpm': -8.524041,
        'energy_%': -0.148007,
        'acousticness_%': -0.157870,
        'in_spotify_playlists': -0.759353,
        'speechiness_%': 4.130521,
        'valence_%': 0.249765,
        'artist_count': 5.496007
    }

col1, col2 = st.columns(2)

with col1:
    st.subheader('Feature Impact Percentages')

    impact_percentages = calculate_impact(coefficients)
    impact_df = pd.DataFrame.from_dict(impact_percentages, orient='index', columns=['Impact %'])
    impact_df = impact_df.sort_values(by='Impact %', ascending=False)

    st.write(impact_df)

    st.bar_chart(impact_df)

with col2:
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






