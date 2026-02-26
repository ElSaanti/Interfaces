import streamlit as st
from PIL import Image

st.title("MI PRIMER PAGINA CON STREAMLIT")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Facilmente puedo realizar backend y frontend.")
Image = Image.open("Interfaces Mult2.jpg")

st.image(image, caption= "Interfaces Mult2")


texto = st.text_input("Escribe algo", "Este es mi texto")
st.write("El texto escrito es", texto)

st.subheader("Ahora usemos 2 Columnas")
