from matplotlib import pyplot as plt
from wordcloud import WordCloud
import streamlit as st

def generate_wordcloud(df, selection, column, title, max_words=50):

    text = " ".join(df[df[column] == selection]["clean_lyrics"])
    fig = plt.figure()
    wordcloud = WordCloud(
        background_color="rgba(255, 255, 255, 0)",
        mode="RGBA",
        max_words=max_words,
        collocations=False,
        colormap="plasma"

    ).generate(text)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title(title)

    return fig


def logo():
    st.image("images/MagicEraser_240620_165341.png")