# here sr means if you want to specify speech_recognition you can use sr
import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import time
import musiclibrary
import requests
from openai import OpenAI


def virtualai(command):

    client = OpenAI(
    api_key="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"
    )

    response = client.responses.create(
    model="gpt-5-nano",
    input= "you are a chatbot with speaking ability just answer in short like in one or two sentence from here: " + command,
    store=True,
    
    )

    return response.output_text

    # return completion.choices[0].message.content




# recognizer object which will recognize what I will talk
recognizer = sr.Recognizer()

newsapi = "0efb3f158fcd49b389d5e45e0d3f32b8"


def speak(text):
    print(f"🔊 Speaking: {text}")
    engine = pyttsx3.init()#initiliaze the engine locally and stop it so that it wont overlap with listening software it is a hardware problem
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    del engine
    print("✅ Done speaking.")


def processCommand(c):
    c = c.lower()
    print(c)
    if 'open google' in c:
        wb.open('https://google.com')
    elif 'open facebook' in c:
        wb.open('https://facebook.com')
    elif 'open instagram' in c:
        wb.open('https://instagram.com')
    elif 'open youtube' in c:
        wb.open('https://youtube.com')
    
    elif c.startswith("play"):
        print("play recognized")
        link = musiclibrary.music[c.split(" ")[1]]
        wb.open(link)
        
    elif "news" in c:
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=0efb3f158fcd49b389d5e45e0d3f32b8")
        # API endpoint
        url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=0efb3f158fcd49b389d5e45e0d3f32b8"

        # Make a GET request to the API
        response = requests.get(url)

        # Convert response to JSON
        data = response.json()

        # Extract article titles into a list
        headlines = [article['title'] for article in data.get('articles', [])]

            # Print the headlines
        print("Headlines:")
        if headlines:
            for i, title in enumerate(headlines[:5], start=1):  # read only 5 for brevity
                print(f"{i}. {title}")
                speak(f"Headline {i}: {title}")
                time.sleep(0.5)
        else:
            speak("Sorry, I couldn't find any news right now.")
    else:
        output = virtualai(c)
        speak(output)






if __name__ == "__main__":
    speak("Initializing .....")
    
    
    # listen for the wake word jarvis
    while(True):
        # obtain audio from the microphone
        r = sr.Recognizer()


        # recognize speech using Sphinx
        try:
            # recoginzer will try to reconize the sound using microphone for 2 second and give output in one second 
            with sr.Microphone() as source:
                
                
                print("Listening...")
                audio = r.listen(source, timeout=3 ,phrase_time_limit=5)#timeout is the maximum time it will analyze and then give the output
                print("recognizing")
            word = r.recognize_google(audio)
            # print(word.lower())
            #confirmation of wake word
            if(word.lower() == 'jarvis'):
                speak("say")
                print("jarvis is active")

                #Listen for command
                with sr.Microphone() as source:

                    #  r.adjust_for_ambient_noise(source, duration=1)
                    print("Listening...")
                    audio = r.listen(source, timeout=3)
                    print("recognizing")
                command = r.recognize_google(audio)
                processCommand(command)

               


        except sr.UnknownValueError:
            print("Could not understand audio")
        except Exception as e:
            print("Error; {0}".format(e))


     


