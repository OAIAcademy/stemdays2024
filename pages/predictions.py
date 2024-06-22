import pickle

import streamlit as st
import pandas as pd


st.title("Rete neurale")
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

    st.write(values)
    prediction = model.predict(values)
    st.write(prediction)







predict_genre()