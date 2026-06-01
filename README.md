# Peter - AI Voice Assistant

Peter is a personal AI voice assistant built with Python. It can listen to your voice commands, process them, and perform various actions like opening websites, playing music, fetching the latest news, or answering general questions using the Gemini API.

## Features

- **Voice Recognition**: Listens for the wake word "Peter" or other greetings ("hello", "hi", "wake up").
- **Web Navigation**: Open popular websites instantly (e.g., "open youtube").
- **Google Search**: Perform Google searches via voice (e.g., "search Python tutorials").
- **Music Playback**: Play specific songs from a pre-configured library.
- **News Updates**: Fetch and read out the latest news headlines about Nepal using NewsAPI.
- **AI Conversationalist**: Ask general questions and get short, concise answers powered by Google's Gemini 3.5 Flash model.

## Technologies Used

- `speech_recognition` - For capturing and recognizing voice input.
- `pyttsx3` - For text-to-speech output (offline).
- `google-genai` - For handling conversational queries with Gemini AI.
- `requests` - For fetching data from the NewsAPI.
- `python-dotenv` - For securely managing API keys.

## Setup Instructions

1. **Clone the repository** (if you haven't already).
2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirement.txt
   ```
4. **Environment Variables**:
   Create a `.env` file in the root directory and add your API keys:
   ```env
   news_api=YOUR_NEWS_API_KEY
   gemini_api=YOUR_GEMINI_API_KEY
   ```
5. **Run the assistant**:
   ```bash
   python main.py
   ```

## Usage

Once running, say "Hey Peter" or "Wake up" to activate the assistant. Then give it a command like:
- *"Open GitHub"*
- *"Play [Song Name]"*
- *"Tell me the news"*
- *"What is the capital of France?"*
- *"Stop"* (to deactivate)
