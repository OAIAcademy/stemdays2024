import streamlit as st
from streamlit_carousel import carousel
from streamlit_option_menu import option_menu
import pandas as pd

df = pd.read_csv("data/songs_with_prediction.csv")

st.set_page_config(initial_sidebar_state="collapsed")


def introduzione():
    st.image("images/MagicEraser_240620_165341.png")

#def carosello_foto():


def carosello():
    test_items = [
        dict(
            title="US!",
            text="Pausa pranzo!",
            img=r"C:\Users\Marco Valentini\PycharmProjects\stemdays2024\images\carosello_pranzo.jpg"
        ),
        dict(
            title="US!",
            text="Al lavoro",
            img=r"C:\Users\Marco Valentini\PycharmProjects\stemdays2024\images\carosello_computer.jpg",
        ),
        dict(
            title="US!",
            text="Team building",
            img=r"C:\Users\Marco Valentini\PycharmProjects\stemdays2024\images\carosello_team.jpg",
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
        st.switch_page(page="pages/📊stats.py")
    if page == "Artist":
        st.switch_page(page="pages/♪artist.py")
    if page == "Predictions":
        st.switch_page(page="pages/🔮️predictions.py")
    # Use the custom class in a container


def about_us():
    st.header("About US!")
    st.subheader("I membri del team")
    st.text("Membri del team:\nCartello Rebecca\n"
            "Costa Gaia\n"
            "Musso Arianna\n"
            "Radicioni Letizia\n"
            "Tedeschi Anna\n"
            "\nSupporto:\n"
            "Antonia\n"
            "Marco\n"
            "Emiliano\n")
    st.subheader("Il progetto")
    st.caption("Il progetto StemDays è un'esperienza di empowerment e tecnologia rivolto alle ragazze per avvicinarle alle materie scientifiche e al mondo del coding contro gli stereotipi di genere che vedono sempre più spesso le ragazze allontanarsi da materie scientifiche perché spesso associate al genere maschile. L'ambiente di lavoro creato è un ambiente inclusivo, di collaborazione, e senza pregiudizi di alcun genere. In questo progetto abbiamo deciso di elaborare dati presi da Spotify dell'anno 2022. Abbiamo addestrato una rete neurale sulla base di questi dati per predirre il genere della canzone data; in più abbiamo analizzato i dati per genere e per artista, creando grafici e wordclouds.")


introduzione()
side_menu()
carosello()

st.divider()
about_us()
