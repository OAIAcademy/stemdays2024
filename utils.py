from matplotlib import pyplot as plt
from wordcloud import WordCloud


def generate_wordcloud(df, selection, column, title, max_words=50):

    text = " ".join(df[df[column] == selection]["clean_lyrics"])
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
    plt.show()