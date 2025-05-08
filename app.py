import streamlit as st
from narrator import extract_text_from_pptx, text_to_speech

st.title("Narrateur vocal de présentation PowerPoint")

uploaded_file = st.file_uploader("Uploader un fichier .pptx", type=["pptx"])
if uploaded_file:
    slides = extract_text_from_pptx(uploaded_file)
    for i, slide in enumerate(slides):
        st.markdown(f"### Diapositive {i+1}")
        st.text(slide)
        output_file = f"audio_slide_{i+1}.mp3"
        text_to_speech(slide, output_file)
        st.audio(output_file)
