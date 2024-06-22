import streamlit as st
from streamlit_carousel import carousel
import pandas as pd
import re

from utils import generate_wordcloud

df = pd.read_csv("data/songs_with_prediction.csv")


def get_chorus(text):
    chorus_pattern = re.compile(r"\[Chorus\]\n((.*\n)+?)(?=\[|\Z)")
    chorus_match = chorus_pattern.search(text)
    if chorus_match:
        chorus = chorus_match.group(1).strip()
    else:
        lines = text.strip().split('\n')
        chorus = '\n'.join(lines[:4])

    return chorus


def logo():
    st.image("images/MagicEraser_240620_165341.png")

def banner_info(artist):
    genre = df.loc[df["artists"] == artist]["tag"].value_counts().index[0]
    lyrics = df.loc[df["artists"] == artist].sort_values("popularity", ascending=False)["lyrics"].values[0]
    track_name = df.loc[df["artists"] == artist].sort_values("popularity", ascending=False)["track_name"].values[0]

    chorus = get_chorus(lyrics)
    col1, col2= st.columns([5, 2])

    with col1:
        st.title(artist)
        st.header(f"Genere musicale: {genre}") #genere predominante dell'artista
        st.text(f"{chorus}") #ritornello canzone più popolare pe rl'artista
        st.write(f"<i>({track_name})</i>", unsafe_allow_html=True)

    with col2:
        st.title("")
        st.write("")
        try:
            st.image(f"images/{artist}.jpg") #il nome dell'immagine deve essere uguale al nome dell'artista e in formato jpg
        except:
            pass


def word_cloud(artist):
    wordcloud = generate_wordcloud(df=df, selection=artist, column="artists", title="")
    st.pyplot(wordcloud)

def primi_grafici() :
    col1, col2 = st.columns(2)

    with col1:
        st.image("images/Chris Brown.jpg")
        espansione = st.expander("TOP 3 HITS")
        with espansione:
            st.text('lista')

    with col2:
        st.image("images/bennyblanco.jpg")
        espansione = st.expander("TOP 3 FLOPS")
        with espansione:
            st.text('lista')

def secondi_grafici():
    col1, col2 = st.columns(2)

    with col1:
        st.image("images/pop.jpg", width=345)
        espansione = st.expander("LIFENESS MEDIA")
        with espansione:
            st.text('lista')

    with col2:
        st.image("images/rb.jpg", width=345)
        espansione = st.expander("POPOLARITA' MEDIA")
        with espansione:
            st.text('lista')

def disclaimer ():
    st.warning("! Eventuali immagini, grafici e informazioni potrebbero non essere reperibili per tutti gli artisti, avendo a disosizione un database limitato.")

logo()

artist = st.selectbox(
    "Seleziona l'artista",
    df.groupby("artists")["popularity"].mean().sort_values(ascending=False).index,
    help="Seleziona un artista o inizia a scrivere sulla barra per vedere le opzioni",
    placeholder="Choose an option", index=0)

banner_info(artist)
disclaimer ()
word_cloud(artist)
primi_grafici()
secondi_grafici()