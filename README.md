# Language Accent Text-to-Speech (Python)

A command-line Python program that converts user-provided text into speech using Google Text-to-Speech (gTTS), with support for **multiple languages and accents**.

The program dynamically displays all supported languages, allows the user to select a language code, converts the input text to speech, and saves it as an MP3 file.

---

## Features
- Displays **all available languages and accents** supported by gTTS
- Converts text or words into speech
- Allows **user-selected language/accent**
- Saves audio output as an `.mp3` file
- Automatically plays the generated audio
- Supports **repeated conversions** using a replay loop
- Input validation for replay choice (`yes` / `no`)

---

## How It Works
1. The program fetches all supported language codes using `tts_langs()`
2. Each language code and its name is printed to the console
3. The user:
   - Selects a language/accent code
   - Enters the text to convert
   - Provides a file name for saving the audio
4. The program:
   - Generates speech using `gTTS`
   - Saves the output as an MP3 file
   - Automatically plays the file
5. The user can repeat the process or exit the program

---

## Technologies Used
- Python
- `gTTS` (Google Text-to-Speech)
- `os` module for file handling and playback

---

## How to Run

### 1. Install dependencies
```bash
pip install gtts
