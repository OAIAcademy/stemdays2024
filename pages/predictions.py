import streamlit as st
import pandas as pd


st.title("Rete neurale")

df = pd.read_csv("data/songs_with_prediction.csv")
