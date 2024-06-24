import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from utils import generate_wordcloud, logo


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

    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="Canzoni", value=len(df), delta_color="off")
    col2.metric(label="Cantanti", value=df["artists"].nunique(), delta_color="off")
    col3.metric(label="Generi musicali", value=df["tag"].nunique(), delta_color="off")
    col4.metric(label="Ultima release", value=df["year"].max(), delta_color="off")


def plot_pie():

    fig = plt.figure()
    plt.pie(
        df["tag"].value_counts(),
        labels=df["tag"].value_counts().index,
        autopct="%1.2f%%",
        )

    my_circle = plt.Circle((0, 0), 0.5, color='white')
    p = plt.gcf()
    p.gca().add_artist(my_circle)

    return fig


def plot_music_feature_distribution(feature):

    fig = plt.figure(figsize=(16, 9))
    feature_per_tag = df.groupby("tag")[feature].mean().sort_values(ascending=True)
    plt.barh(feature_per_tag.index, feature_per_tag)
    plt.title(f"{feature.capitalize()} media per genere musicale", fontsize=20)

    return fig


def worcloud_section():
    st.subheader("Text mining")
    genre = st.selectbox("Seleziona un genere", df["tag"].unique())
    wordcloud = generate_wordcloud(df=df, selection=genre, column="tag", title=f"")
    st.pyplot(fig=wordcloud)


def gli_artisti_piu_cercati() :
    col1, col2 = st.columns(2)

    with col1:
        st.image("images/Chris Brown.jpg")
        espansione = st.expander("TOP 5 artisti più ascoltati")
        with espansione:
            st.text('lista')

    with col2:
        st.image("images/bennyblanco.jpg")
        espansione = st.expander("TOP 5 artisti meno ascoltati")
        with espansione:
            st.text('lista')


def i_generi_piu_cercati():
    col1, col2 = st.columns(2)

    with col1:
        st.image("images/pop.jpg", width=345)
        espansione = st.expander("Distribuzione per genere")
        with espansione:
            st.text('grafico')

    with col2:
        st.image("images/rb.jpg", width=345)
        espansione = st.expander("TOP 5 canzoni più ascoltate")
        with espansione:
            st.text('lista')



show_metrics()

st.subheader("Distribuzione dei generi musicali")
col1, col2 = st.columns(2)
pie = plot_pie()
col1.pyplot(fig=pie)

feature = col2.selectbox("Seleziona una feature", music_features)
barchart = plot_music_feature_distribution(feature)
col2.pyplot(fig=barchart)
worcloud_section()

st.title("LE CLASSIFICHE PIU POPOLARI !!!")
gli_artisti_piu_cercati()
i_generi_piu_cercati()

col1, col2, col3 = st.columns([1,2,1])
with col2:
    logo()
