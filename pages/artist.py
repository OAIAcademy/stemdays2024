import streamlit as st
import pandas as pd
from streamlit_carousel import carousel

def logo():
    st.image("images/MagicEraser_240620_165341.png")

def banner_info ():
    col1, col2 = st.columns(2)

    with col1:
        st.image("images/chrisbrown.jpg", width=230) #immagine se nei top 5

    with col2:
        st.title("Chris Brown") #nome persona
        st.header("Genere musicale: Rb") #genere predominante dell'artista
        st.text("You don't know what you did, did to me, \nyour body lightweight speaks to me") #ritornello canzone più popolare pe rl'artista

def word_cloud ():
    #codice word cloud, immagine ?
    st.image("images/wcdiprova.gif")

def primi_grafici() :
    col1, col2 = st.columns(2)

    with col1:
        st.image("images/chrisbrown.jpg")
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
    st.text("! Eventuali immagini, grafici e informazioni potrebbero non essere reperibili per tutti gli artisti, avendo a disosizione un database limitato.")

logo()

option = st.selectbox(
    "Seleziona l'artista",
    (["Chris Brown", "ABBA", "Arctic Monkeys", "Kids Bops", "Ariana Grande", "Lady Gaga"]), help="Seleziona un artista o inizia a scrivere sulla barra per vedere le opzioni", placeholder="Choose an option", index=0)

banner_info()
disclaimer ()
word_cloud()
primi_grafici()
secondi_grafici()