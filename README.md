# S.H.I.V.A (Simple Highly Intelligent Virtual Assistant)

S.H.I.V.A is a voice-activated virtual assistant built using Python, which can recognize voice commands, respond with text-to-speech, and execute various tasks such as telling jokes, checking the time, and more. The assistant listens for specific commands and can be exited by voice.

## Features

- **Voice Recognition**: Recognizes and processes user voice commands using Google Speech Recognition.
- **Text-to-Speech**: Responds to user input using the `pyttsx3` library.
- **Jokes**: Tells random jokes upon request.
- **Weather Placeholder**: Responds to weather inquiries with placeholder responses (can be expanded to fetch real-time data).
- **Reminders Placeholder**: Takes reminder requests (functionality not fully implemented).
- **Time Inquiry**: Responds with the current time.
- **Voice-Activated Exit**: Stops listening when the user says "exit" or "stop."

## Requirements

To run this project, you need Python and the following libraries:

- Python 3.x
- `SpeechRecognition`
- `pyttsx3`
- `pyaudio` (for microphone input)

## Installation

1. Clone the repository or download the source files.
2. Install the necessary Python packages:

    ```bash
    pip install SpeechRecognition pyttsx3 pyaudio
    ```

## How to Run

1. Make sure your microphone is enabled.
2. Run the Python script:

    ```bash
    python assistant.py
    ```

3. The assistant will start listening for your commands. You can try commands like:
   - "Hello"
   - "Tell me a joke"
   - "What's the weather?"
   - "Set a reminder"
   - "What time is it?"
   - "Exit" or "Stop" to terminate the assistant.

## Available Commands

- **Greetings**: Say "hello" or ask "how are you" to interact with the assistant.
- **Check the Time**: Ask "What time is it?" to get the current time.
- **Tell a Joke**: Ask "Tell me a joke" or "Make me laugh" to hear a random joke.
- **Weather Inquiry**: Ask "What's the weather?" to get a placeholder response (this can be expanded with real-time weather data).
- **Set a Reminder**: Ask "Set a reminder" and specify the reminder (functionality not fully implemented).
- **Exit**: Say "Exit" or "Stop" to stop the assistant.

## Customization

You can easily extend the assistant by adding more commands and functionality, such as fetching real-time data (e.g., weather, news) or integrating with task management systems.

## Known Issues

- The reminders feature is currently a placeholder and not fully functional.
- The weather feature is a placeholder and does not fetch live data.
- The assistant requires an active internet connection to recognize voice commands via Google Speech Recognition.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

