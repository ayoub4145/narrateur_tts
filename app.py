import streamlit as st
from narrator import extract_text_from_pptx, text_to_speech
import os
st.title("Narrateur vocal de présentation PowerPoint")
st.markdown("""
    ### Instructions
    1. Uploadez un fichier PowerPoint (.pptx).
    2. Le texte de chaque diapositive sera extrait et converti en audio.
    3. Vous pourrez écouter chaque diapositive en cliquant sur le lecteur audio.
""")
uploaded_file = st.file_uploader("Uploader un fichier .pptx", type=["pptx"])
# Définir le répertoire de sortie
if uploaded_file:
    slides = extract_text_from_pptx(uploaded_file)
    for i, slide in enumerate(slides):
        st.markdown(f"### Diapositive {i+1}")
        st.text(slide)
        output_file = f"audio_slide_{i+1}.mp3"
        text_to_speech(slide, output_file)
        st.audio(output_file)


st.markdown("Developpé par [Ayoub BERHILI](https://github.com/ayoub4145)")