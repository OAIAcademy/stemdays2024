import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_excel("data/songs_with_predictions.csv")

st.title("Descrizione dei dati")

def show_metrics():

    col1, col2, col3 = st.columns(3)
    col1.metric(label="Canzoni", value=len(df), delta_color="off")
    col2.metric(label="Cantanti", value=df["artists"].nunique(), delta_color="off")
    col3.metric(label="Generi", value=df["tags"].nunique(), delta_color="off")

def plot_pie():

    plt.pie(
        df["tags"].value_counts(), 
        labels=df["tags"].value_counts().index
        )
    plt.show()


col1, col2 = st.columns(2)
pie = plot_pie()
col1.pyplot(pie)
