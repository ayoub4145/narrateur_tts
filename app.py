import streamlit as st
from narrator import extract_text_from_pptx, text_to_speech, extract_text_from_docx, extract_text_from_pdf
import os
st.set_page_config(page_title="Narrateur vocal de présentation PowerPoint", page_icon=":microphone:", layout="wide")
st.title("Narrateur vocal de documents (.pptx, .docx, .pdf)")
st.markdown("""
    ### Instructions
    1. Choisissez la langue et le ton (accent/région) de la voix.
    2. Uploadez un fichier (.pptx,.pdf,.docx).
    3. Le texte de chaque page/diapositive sera extrait et converti en audio.
    4. Vous pourrez écouter chaque diapositive en cliquant sur le lecteur audio.
""")
tld_options = {
    "fr": ["com (Standard)", "ca (Québec)"],
    "en": ["com (US)", "co.uk (UK)", "com.au (Australia)", "co.in (India)"],
    "es": ["com (Spain)", "com.mx (Mexico)"]
}
# Sélection de la langue
lang = st.selectbox("Langue", ["fr", "en", "es"])
tld_labels = tld_options.get(lang, ["com"])
# Sélection du ton (accent / région)
tld_label = st.selectbox("Accent / Ton", tld_labels)
tld = tld_label.split(" ")[0]  # extrait juste 'com', 'ca', etc.
uploaded_file = st.file_uploader("Uploader un fichier", type=["pptx", "docx", "pdf"])


# Définir le répertoire de sortie
output_dir = "output"

# Créer le répertoire de sortie s'il n'existe pas
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Définir le répertoire de sortie
if uploaded_file:
    file_type = uploaded_file.name.split('.')[-1].lower()
    if file_type == "pptx":
        slides = extract_text_from_pptx(uploaded_file)
    elif file_type == "docx":
        slides = extract_text_from_docx(uploaded_file)
    elif file_type == "pdf":
        slides = extract_text_from_pdf(uploaded_file)
    else:
        st.error("Format non pris en charge.")
        slides = []

    for i, slide_text in enumerate(slides):
        if slide_text.strip():
            output_file = f"audio_page_{i+1}.mp3"
            text_to_speech(slide_text, output_file,lang=lang,tld=tld)
            st.markdown(f"### Page {i+1}")
            st.text(slide_text.strip())
            st.audio(output_file)


# st.markdown("Developpé par [Ayoub BERHILI](https://github.com/ayoub4145)")
