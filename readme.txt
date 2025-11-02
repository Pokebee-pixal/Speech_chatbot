🧠 Jarvis – Your Personal Voice Assistant

Jarvis is a Python-based AI voice assistant that listens for your voice commands, talks back to you using speech, opens websites, plays music, reads news headlines, and even chats intelligently using OpenAI GPT models.

⚙️ Features

✅ Listens for the wake word "Jarvis"
✅ Responds using natural speech output
✅ Can open websites like Google, YouTube, Facebook, etc.
✅ Can play songs using links from your custom music library
✅ Reads out latest news headlines (via News API)
✅ Can chat like an AI bot using the OpenAI GPT model

🧩 Requirements
🐍 Python Version

You’ll need Python 3.10 or newer.
Recommended: Python 3.11.5 (stable and compatible with most libraries)

📦 Install Required Packages

Open Command Prompt (CMD) and run these commands one by one 👇
it will download your necessary module
            pip install speechrecognition
            pip install pyttsx3
            pip install requests
            pip install openai
            pip install pyaudio


⚠️ Note:

On some systems, pyaudio may fail to install directly.
If that happens, download a compatible .whl file from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

and install it manually:

pip install PyAudio-0.2.11-cp311-cp311-win_amd64.whl


How to run 
1st after downloading every module just run it in vs code
2nd say jarvis when listening is written in the terminal 
3rd give it command like: open youtube/ facebook/ google/ instagram/ 
4th give it command like: play {song name which is in the music library you have given you can also add your favourite song in music library}
5th give it command which include word "news" and it will fetch news headlines
6th if your command match with none of the above it will go to integrated chatgpt
            