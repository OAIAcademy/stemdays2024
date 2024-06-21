import streamlit as st
import pandas as pd


st.title("Rete neurale")

df = pd.read_excel("data/songs_with_predictions.csv")
