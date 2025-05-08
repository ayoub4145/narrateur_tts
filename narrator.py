from pptx import Presentation
from gtts import gTTS
import os
import glob

def extract_text_from_pptx(file_path):
    try:
        prs = Presentation(file_path)
        slide_texts = []
        for slide in prs.slides:
            text = ""
            for shape in slide.shapes:
                if hasattr(shape, "text"):
                    text += shape.text + " "
            slide_texts.append(text.strip())
        return slide_texts
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred while extracting text: {e}")
        return []

def text_to_speech(text, output_path, lang='fr'):
    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(output_path)
    except Exception as e:
        print(f"An error occurred while generating audio: {e}")
        
def clean_output_directory(output_dir):
    try:
        # Vérifie si le répertoire existe
        if os.path.exists(output_dir):
            # Supprime tous les fichiers .mp3 dans le répertoire
            files = glob.glob(os.path.join(output_dir, "*.mp3"))
            for file in files:
                os.remove(file)
            print(f"Tous les fichiers dans '{output_dir}' ont été supprimés.")
        else:
            # Crée le répertoire s'il n'existe pas
            os.makedirs(output_dir)
            print(f"Le répertoire '{output_dir}' a été créé.")
    except Exception as e:
        print(f"Une erreur est survenue lors du nettoyage du répertoire : {e}")   




