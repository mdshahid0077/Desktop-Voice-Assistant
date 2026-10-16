import speech_recognition as sr    #Used to recognize speech from the microphone
import webbrowser   #Used to open website in the web browser
import pyttsx3  #Used to convert text to speech
import subprocess # Used to open windows apps
import musicLibrary
import datetime #Used to get current date and time
from dotenv import load_dotenv
from openai import OpenAI #Import the openai client
import re
import logging

load_dotenv()

client = OpenAI() #Create an OpenAI client

logging.basicConfig(
    filename = "jarvis.log",
    level = logging.INFO,
    format = "%(asctime)s - %(levelname)s - %(message)s"
)

logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)

#Define a function to make Jarvis speak
def speak(text):
    print("Speaking", text)
    engine = pyttsx3.init()  #Initialize the text to speech engine
    engine.say(text)
    engine.runAndWait()

conversation = []

def aiProcess(command):
    conversation.append({
        "role": "user",
        "content": command
    })

    logging.info(f"Processing command: {command}")
    try:
        response = client.responses.create(
            model = "gpt-5.6",
            tools = [
                {"type": "web_search"}
                ],
                instructions = "You are Jarvis, a helpful virtual assistant. Give short, clear and natural answers suitable for voice. Do not mention or read source URLs, citations, or web-search details aloud.",
                input = conversation[-10:]
        )
        answer = response.output_text
        logging.info("AI response received successfully")

        conversation.append({
                "role": "assistant",
                "content": answer
            })
        answer = re.sub(r'\s*\(\s*\[[^\]]+\]\([^)]+\)\s*\)', '', answer)

        if "[" in answer:
            answer = answer.split("[")[0]
        return answer
    except Exception as e:
        logging.error(f"AI Error: {e}")
        return "Sorry, I am having trouble processing your request."


r = sr.Recognizer() #Create a speech recognizer object




#Process the command given by the user
def processCommand(command):

    #Check if the user wants to open Youtube
    if "open youtube" in command.lower():
        #Open Youtube in the webbrowser
        webbrowser.open("https://youtube.com")

    elif "open google" in command.lower():
        webbrowser.open("https://google.com")

    elif "open notepad" in command.lower():
        subprocess.Popen("notepad.exe")

    elif "open spotify" in command.lower():
        subprocess.Popen("spotify.exe")

    elif command.lower().startswith("play"):
        songs = command.lower().replace("play ","")
        link = musicLibrary.music[songs]
        webbrowser.open(link)

    elif "time" in command.lower(): #Check if the user ask for the current time
        time = datetime.datetime.now()
        current_time = time.strftime("%H:%M") #Format the current time as hours and minutes
        speak(f"The current time is {current_time}")

    elif "date" in command.lower():
        today = datetime.datetime.now()
        current_date = today.strftime("%d-%m-%y")
        speak(f"Today's date is {current_date}")

    elif "day" in command.lower():
        current_day = datetime.datetime.now().strftime("%A")
        speak(f"Today is {current_day}")

    #If none of the command mathed
    else:
        output = aiProcess(command)
        speak(output)



if __name__ == "__main__":
    speak("Initializing Jarvis...")

#Keep Jarvis running continously
while True:

        #Try to run Jarvis code safely
        try:
            #Open the microphone as the audio source
            with sr.Microphone() as source:
                print("Listening...")   #Show the Jarvis is ready to listen
                r.adjust_for_ambient_noise(source, duration=2)  #Adjust the recognizer for background noise
                audio = r.listen(source)#Listen to the user's voice through the microphone
                print("Processing...")#Show that the recorded audio is being processed
                word = r.recognize_google(audio)#Convert the recorded audio into text using Google Speech Recognition
                print("You said:", word)#Display the recognized speech in the terminal

            if word.lower() == "jarvis": #Check if the user said the wake word "Jarvis"
                print("I am listening...")#Display a message when the wake word is detected
                speak("Yes sir...")# Make Jarvis respond to wake word

            else:
                continue

            #Open the microphone to listen for the user's command
            with sr.Microphone() as source:
                print("Jarvis active:") #Show that Jarvis is ready to receive the command
                audio = r.listen(source)
                command = r.recognize_google(audio)
                print("Command", command)

                processCommand(command)
            

        #Handle error
        except Exception as e:
            print(e)