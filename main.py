import pyttsx3
from gtts import gTTS
print("Hello user. Welcome to Text to Speech Converter.")
engine = pyttsx3.init()
rate = engine.getProperty('rate')   #This fetches current rate (speed) at which the speech is being spoken. Rate is measured in (wpm).
engine.setProperty('rate', rate - 50)   # This sets the new rate (speed) for the speech engine.
engine.setProperty('volume', 1)   #This controls the volume of the speech. Value ranges from 0.0 to 1.0.
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  
 #This retrieves the available voices from the speech engine. The voices is a list of available voice objects and each object contains properties such as the voice’s ID, name, gender and language. Here we have only two voices i.e you can assign index as 0 or 1 .

input_text = input("Enter text here: ")
engine.say(input_text)
engine.runAndWait()

try:
    option = int(input("Enter '1' to download the audio speech or '0' to skip: "))
    if option == 1:
        tts = gTTS(text=input_text, lang='en')
        filename = "audio.mp3"
        tts.save(filename)
        print(f"Audio saved as {filename}")
        print("Thank you for using Text to Speech Converter!")
    elif option == 0:
        print("Thank you for using Text to Speech Converter!")
    else:
        print("Invalid choice. Please enter 0 or 1.")
except ValueError:
    print("Invalid input. Please enter a number (0 or 1).")

    
