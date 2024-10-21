# %%
import speech_recognition as sr
import pyttsx3
import time

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Take voice command from the user with timeout handling."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1  # Adjusts the pause threshold before recognition
        try:
            audio = recognizer.listen(source, timeout=10)  # Stops listening after 10 seconds if no input
        except sr.WaitTimeoutError:
            print("Listening timed out.")
            return "None"

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')  # Recognize with Google API
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return "None"
    return query

# Function to tell a joke
def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you get if you cross a snowman and a vampire? Frostbite!",
        "Why did the bicycle fall over? Because it was two-tired!",
        "Why don't programmers like nature? It has too many bugs!"
    ]
    speak(jokes[int(time.time()) % len(jokes)])  # Tell a random joke based on current time

# Function to check the weather (placeholder)
def check_weather():
    speak("Currently, I cannot fetch live weather data, but it seems like a sunny day!")

# Main function to keep the assistant running
if __name__ == "__main__":
    while True:
        command = take_command().lower()  # Take voice command and convert it to lowercase
        if command == "none":
            continue  # If no valid command is heard, keep listening
        
        # Exit or stop command
        if "exit" in command or "stop" in command:
            speak("Goodbye!")
            break  # Exit the loop and stop listening

        # Greeting commands
        elif "hello" in command:
            speak("Hello! How can I assist you today?")
        elif "how are you" in command:
            speak("I'm just a bunch of code, but I'm doing great! How about you?")
        
        # Command to check the assistant's name
        elif "your name" in command:
            speak("My name is S.H.I.V.A, your virtual assistant.")

        # Joke command
        elif "tell me a joke" in command or "make me laugh" in command:
            tell_joke()

        # Placeholder command to check weather
        elif "weather" in command:
            check_weather()

        # Reminder command (placeholder)
        elif "set a reminder" in command:
            speak("What would you like me to remind you about?")
            reminder = take_command().lower()
            speak(f"I will remind you to {reminder}. Please note, reminders are not yet fully functional.")

        # Time command
        elif "time" in command:
            current_time = time.strftime("%I:%M %p")
            speak(f"The current time is {current_time}.")

        # Default case: Echo back the command
        else:
            speak(f"You said: {command}")



