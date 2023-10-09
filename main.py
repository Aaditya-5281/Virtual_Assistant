import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import openai
import pywhatkit

import datetime
import random

apikey = "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"
chatStr = ""
# https://youtu.be/Z3ZAJoi4x6Q
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Aaditya: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

def say(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)
    engine.setProperty('volume', 2.0)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            say(f"{query}")
            return query,True
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis",False

if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("Jarvis A.I")
    while True:
        print("Listening...")
        query,response = takeCommand()
        # todo: Add more sites
        if response==True:
            sites={
                "youtube": "https://www.youtube.com",
                "wikipedia": "https://www.wikipedia.com",
                "google": "https://www.google.com",
                "instagram": "https://www.instagram.com",
                "chatgpt": "https://chat.openai.com/?model=text-davinci-002-render-sha",
                "github": "https://github.com/Aaditya-5281",
                "gmail": "https://mail.google.com/mail/u/0/#inbox",
            }


            for site in sites.keys():
                if f"Open {site}".lower() in query.lower():
                    say(f"Opening {site} sir...")
                    webbrowser.open(sites.get(site))
            # todo: Add a feature to play a specific song
            if "music" in query:
                musicPath = "p.mp3"
                os.system(f"start {musicPath}")

            elif "time" in query:
                time = datetime.datetime.now().strftime("%I:%M %p")
                print("Time:",f"{time}")
                say(f"The Time is {time}")

            elif "How r u".lower() in query.lower():
                print("I am Fine Sir")
                say(f"I am Fine Sir")

            elif "date" in query:
                day = datetime.datetime.now().day
                month = datetime.datetime.now().month
                year = datetime.datetime.now().year
                print("DATE:",f"Today is {day}")
                say(f"Today is {day}")

            # windows Application opening
            elif "Open Notepad".lower() in query.lower():
                say(f"Opening Notepad")
                os.system("C:/Windows/notepad.exe")

            elif "Open Whatsapp".lower() in query.lower():
                say(f"Opening Whatsapp")
                os.system("C:/Windows/WhatsApp.exe")

            # Openai API
            elif "Using artificial intelligence".lower() in query.lower():
                ai(prompt=query)

            elif "exit".lower() in query.lower():
                exit()

            elif "reset chat".lower() in query.lower():
                chatStr = ""

            else:
                print("Processing...")
                search={query}
                pywhatkit.search(search)





        # say(query)