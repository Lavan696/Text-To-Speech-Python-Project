🗣️ Text-to-Speech Converter using Python

This is a Text-to-Speech (TTS) mini-project built in Python using two powerful libraries: pyttsx3 (for offline speech) and gTTS (for generating downloadable audio using Google Text-to-Speech). It converts any user-provided text into human-like speech.

🛠️ Features
Converts typed text into speech using pyttsx3 (offline)

Option to download the audio using gTTS (Google Text-to-Speech API)

Customizes:

Speech speed (rate)

Voice (male/female)

Volume level

Simple command-line interface for ease of use

Handles invalid inputs gracefully

💡 How It Works
Greets the user and prompts for text input.

Uses pyttsx3 to convert the text into speech and play it aloud.

Asks the user whether to download the audio.

If selected, uses gTTS to save the speech as an audio.mp3 file.

Provides appropriate messages based on user choices.

✅ Example Run

Hello user. Welcome to Text to Speech Converter.
Enter text here: Hello, welcome to Python projects!
[Speech is played aloud]

Enter '1' to download the audio speech or '0' to skip: 1
Audio saved as audio.mp3
Thank you for using Text to Speech Converter!
🧰 Requirements
Python 3.x

pyttsx3

gTTS

Installation

pip install pyttsx3
pip install gTTS
⚠️ Note: gTTS requires an internet connection, while pyttsx3 works offline.

🔧 Configuration Highlights
Setting	Description
rate	Controls speech speed (words per min)
volume	Range from 0.0 (mute) to 1.0 (max)
voice index	Selects male (0) or female (1) voice

📂 Output
Plays the spoken version of the input text.

Optionally saves the audio as audio.mp3 in the current directory.

🛡️ Error Handling
Catches invalid inputs like non-numeric menu options.

Handles unexpected choices with user-friendly messages.
