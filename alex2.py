import speech_recognition as sr
import webbrowser
import pyttsx3

# Initialize text-to-speech
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print("You said:", command)
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Network error.")
        return ""
    
    return command

def alexa():
    speak("Hello, I am your assistant. What should I open?")
    while True:
        command = take_command()

        if "youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
        elif "google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        elif "facebook" in command:
            speak("Opening Facebook")
            webbrowser.open("https://www.facebook.com")
        elif "exit" in command or "quit" in command or "stop" in command:
            speak("Goodbye!")
            break   # ✅ works fine here
        elif command != "":
            speak("I can only open YouTube, Google, or Facebook right now.")
        




# Run the assistant
if __name__ == "__main__":
    alexa()
