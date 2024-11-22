import sys
import pyttsx3

def text_to_audio_local(input_file, output_file):
    try:
        # Lire le contenu du fichier texte
        print(f"Lecture du fichier texte : {input_file}")
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
        
        if not text.strip():
            print("Le fichier texte est vide.")
            return

        # Initialiser le moteur de synthèse vocale
        print("Initialisation du moteur de synthèse vocale...")
        engine = pyttsx3.init()

        # Configurer les paramètres de voix (facultatif)
        voices = engine.getProperty('voices')
        print(f"Voix disponibles : {len(voices)}")
        for voice in voices:
            print(f"Voix disponible: {voice.name}, Langues: {voice.languages}")
            if 'fr_FR' in voice.languages:  # Utilise une voix française si disponible
                print(f"Voix sélectionnée : {voice.name}")
                engine.setProperty('voice', voice.id)
                break

        # Configurer la vitesse (facultatif)
        print("Configuration de la vitesse...")
        engine.setProperty('rate', 150)  # Ajustez pour changer la vitesse

        # Création du fichier audio
        print(f"Création du fichier audio : {output_file}")
        engine.say(text)
        engine.save_to_file(text, output_file)
        engine.runAndWait()

        print(f"Fichier audio créé avec succès : {output_file}")

    except FileNotFoundError:
        print(f"Erreur : Le fichier {input_file} n'existe pas.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        output_file = input_file.replace('.txt', '.wav')
        text_to_audio_local(input_file, output_file)
    else:
        print("Utilisation : python main.py fichier_texte.txt")