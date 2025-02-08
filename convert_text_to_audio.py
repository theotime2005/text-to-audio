import sys
from gtts import gTTS


def text_to_audio_local(input_file, output_file, language, function):
    try:
        function("loading")
        # Read the content of the text file
        print(f"Reading text file: {input_file}")
        with open(input_file, "r", encoding="utf-8") as file:
            text = file.read()

        if not text.strip():
            print("The text file is empty.")
            function("error")
            return

        # Create the audio file using gTTS
        print(f"Creating audio file: {output_file}")
        tts = gTTS(text, lang=language)
        tts.save(output_file)

        print(f"Audio file created successfully: {output_file}")
        function("success")

    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
        function("error")
    except Exception as e:
        print(f"An error occurred: {e}")
        function("error")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        input_file = sys.argv[1]
        output_file = input_file.replace(".txt", ".wav")
        text_to_audio_local(input_file, output_file)
    else:
        print("Usage: python convert_text_to_audio.py text_file.txt")
