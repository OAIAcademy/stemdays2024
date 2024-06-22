import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from utils import generate_wordcloud

st.set_option('deprecation.showPyplotGlobalUse', False)


df = pd.read_csv("data/songs_with_prediction.csv")
music_features = [
    "danceability",
    "energy",
    "loudness",
    "speechiness",
    "acousticness",
    "instrumentalness",
    "liveness",
    "valence",
    "tempo"
]

st.title("Descrizione dei dati")

def show_metrics():

    col1, col2, col3 = st.columns(3)
    col1.metric(label="Canzoni", value=len(df), delta_color="off")
    col2.metric(label="Cantanti", value=df["artists"].nunique(), delta_color="off")
    col3.metric(label="Generi", value=df["tag"].nunique(), delta_color="off")

def plot_pie():

    plt.figure(figsize=(10, 6))
    plt.pie(
        df["tag"].value_counts(),
        labels=df["tag"].value_counts().index,
        autopct="%1.2f%%"
        )
    my_circle = plt.Circle((0, 0), 0.5, color='white')
    p = plt.gcf()
    p.gca().add_artist(my_circle)
    plt.show()


def plot_music_feature_distribution(feature):

    plt.figure(figsize=(16, 9))
    feature_per_tag = df.groupby("tag")[feature].mean().sort_values(ascending=True)
    plt.barh(feature_per_tag.index, feature_per_tag)
    plt.title(f"{feature.capitalize()} media per genere musicale ")
    plt.show()


show_metrics()
col1, col2 = st.columns(2)

col1.subheader("Distribuzione dei generi musicali")
pie = plot_pie()
col1.pyplot(pie)
feature = col2.selectbox("Seleziona una feature", music_features)
barchart = plot_music_feature_distribution(feature)
col2.pyplot(barchart)

st.subheader("Text mining")
col1, col2 = st.columns(2)

artist = col1.selectbox("Seleziona un artista", sorted(df["artists"].unique()))
wordcloud = generate_wordcloud(df=df, selection=artist, column="artists", title=f"{artist} Wordcloud")
col1.pyplot(wordcloud)


genre = col2.selectbox("Seleziona un genere", df["tag"].unique())
wordcloud = generate_wordcloud(df=df, selection=genre, column="tag", title=f"{genre.upper} Wordcloud")
col2.pyplot(wordcloud)
