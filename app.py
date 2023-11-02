import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the model
model = joblib.load("Spotify_SongDanceability_Predicter.pkl")

# Load the model information
model_info = joblib.load("model_info.pkl")

print(model_info["features"])

st.title("Predict a Songs Danceability")
st.write("This is a ridge linear regression model")
st.write("Due to the small dataset size the accuracy is 34%")

feature_values = {}

for feature in model_info["features"]:
    if feature == 'artist_count':
        feature_values[feature] = st.number_input(f"Enter {feature}", min_value=1, max_value=8)
    elif feature == 'valence_%': 
        st.markdown("""---""")
        st.write("The musical positiveness:")
        feature_values[feature] = st.number_input(f"Enter {feature}", min_value=1)
    elif feature == 'in_spotify_playlists': 
        st.markdown("""---""")
        st.write("In how many spotify playlists:")
        feature_values[feature] = st.number_input(f"Enter {feature}", min_value=1)
    elif feature == 'speechiness_%': 
        st.markdown("""---""")
        st.write("How much they sing in %")
        feature_values[feature] = st.number_input(f"Enter {feature}", min_value=1)
    elif feature == 'bpm': 
        st.markdown("""---""")
        st.write("300bpm limit")
        feature_values[feature] = st.number_input(f"Enter {feature}", min_value=65, max_value=300)
    else:
        feature_values[feature] = st.number_input(f"Enter {feature}", min_value=1)
        
        
columns_to_log = ['bpm', 'in_spotify_playlists', 'speechiness_%', 'artist_count'] 

# After collecting input values
if st.button("Make Prediction"):
    input_features = [feature_values[feature] for feature in model_info["features"]]
    input_data = pd.DataFrame([input_features], columns=model_info["features"])
    prediction = model.predict(input_data)[0]
    st.write(f"Predicted Danceability: {prediction[0]} %")






