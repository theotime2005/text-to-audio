import sys
from gtts import gTTS

def text_to_audio_local(input_file, output_file):
    try:
        # Read the content of the text file
        print(f"Reading text file: {input_file}")
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()

        if not text.strip():
            print("The text file is empty.")
            return

        # Create the audio file using gTTS
        print(f"Creating audio file: {output_file}")
        tts = gTTS(text, lang='fr')
        tts.save(output_file)

        print(f"Audio file created successfully: {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        output_file = input_file.replace('.txt', '.wav')
        text_to_audio_local(input_file, output_file)
    else:
        print("Usage: python main.py text_file.txt")