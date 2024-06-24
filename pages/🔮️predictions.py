import pickle

import numpy as np
import streamlit as st
import pandas as pd

from utils import logo

df = pd.read_csv("data/songs_with_prediction.csv")
features = ['danceability', 'energy', 'loudness', 'mode', 'speechiness',
            'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'views']
#load model
def load_model():
    with open('data/model.pkl', 'rb') as f:
        model = pickle.load(f)

    return model


model = load_model()


def predict_genre():

    values = pd.DataFrame(columns=features)
    l = round(len(features) / 2)
    prediction = ""
    with st.form("Componi la tua canzone"):
        st.write("##### Componi la tua canzone")
        st.write(":grey[Utilizza gli sliders per definire le caratterstiche e clicca il tasto per scoprire il genere musicale]")
        first_features = features[:l]
        cols = st.columns(len(first_features))
        for col, feature in zip(cols, first_features):
            val = col.slider(feature, min_value=df[feature].min(), max_value=df[feature].max())
            values.loc[0, feature] = val

        second_features = features[l:]
        cols = st.columns(len(second_features))
        for col, feature in zip(cols, second_features):
            val = col.slider(feature, min_value=df[feature].min(), max_value=df[feature].max())
            values.loc[0, feature] = val

        submitted = st.form_submit_button("🔮️ Predici il genere!")
        if submitted:
            prediction = model.predict(values)[0]

    return prediction, values

# Function to calculate Euclidean distance
def euclidean_distance(row, user_features):
    return np.sqrt(np.sum((row - user_features) ** 2))


def pick_image(genre):
    if genre:
        st.subheader(f"La tua canzone è... :violet[{genre}]!")
        st.image(f"images/{genre}.jpeg")

def suggest_songs(genre, features):
    # Extract song features from the dataframe

    # Calculate distances
    df['distance'] = df[features.columns].apply(lambda row: euclidean_distance(row.values, features.values), axis=1)

    # Sort by distance
    df_sorted = df.loc[df["tag"] == genre].sort_values(by='distance')

    # Display top 5 most similar songs
    st.subheader('Top 3 canzoni simili')
    for _, song in df_sorted.head(3).iterrows():
        artist = song["artists"]
        track_name = song["track_name"]
        genre = song["tag"]
        st.write(f"♪ :violet[<b>{track_name}</b>] by <i>{artist}</i>", unsafe_allow_html=True)


def info_about_model():

    with st.expander("Scopri di più sulla rete neurale"):
        st.text("performance")


st.title("Rete neurale")
genre, values = predict_genre()
col1, col2 = st.columns(2)
with col1:
    pick_image(genre)
with col2:
    if genre:
        suggest_songs(genre, values)
info_about_model()
col1, col2, col3 = st.columns([1,2,1])
with col2:
    logo()