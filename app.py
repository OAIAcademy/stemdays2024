import streamlit as st
from streamlit_carousel import carousel
from streamlit_option_menu import option_menu
import pandas as pd

df = pd.read_csv("data/songs_with_prediction.csv")


def introduzione():
    st.image("images/MagicEraser_240620_165341.png")

#def carosello_foto():


def carosello():
    test_items = [
        dict(
            title="Slide 1",
            text="A tree in the savannah",
            img="https://www.rollingstone.com/wp-content/uploads/2018/06/rs-4444-rectangle.jpg?w=624&h=422&crop=1"
        ),
        dict(
            title="Slide 2",
            text="A wooden bridge in a forest in Autumn",
            img="https://img.freepik.com/free-photo/beautiful-wooden-pathway-going-breathtaking-colorful-trees-forest_181624-5840.jpg?w=1380&t=st=1688825780~exp=1688826380~hmac=dbaa75d8743e501f20f0e820fa77f9e377ec5d558d06635bd3f1f08443bdb2c1",
        ),
        dict(
            title="Slide 3",
            text="A distant mountain chain preceded by a sea",
            img="https://img.freepik.com/free-photo/aerial-beautiful-shot-seashore-with-hills-background-sunset_181624-24143.jpg?w=1380&t=st=1688825798~exp=1688826398~hmac=f623f88d5ece83600dac7e6af29a0230d06619f7305745db387481a4bb5874a0",
        ),
    ]
    carousel(items=test_items)


def side_menu():
    # 2. horizontal menu
    page = option_menu(
        None, ["Home + US!", "Artist", "Stats", 'Predictions'],
        icons=['house', 'music-note', "bar-chart", 'gear'], #https://icons.getbootstrap.com/
        menu_icon="cast", default_index=0, orientation="horizontal"
    )
    if page == "Stats":
        st.switch_page(page="pages/📊 stats.py")
    if page == "Artist":
        st.switch_page(page="pages/♪ artist.py")
    if page == "Predictions":
        st.switch_page(page="pages/🔮️predictions.py")
    # Use the custom class in a container


def about_us():
    st.header("About US!")
    st.subheader("I membri del team")
    st.text("//")
    st.subheader("Il progetto")
    st.text("//")


introduzione()
side_menu()
carosello()

st.divider()
about_us()
