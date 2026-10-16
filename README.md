# Desktop Voice Assistant (Jarvis) with AI Integration

An intelligent desktop voice assistant built in Python that executes local system commands, web automation, and integrates OpenAI's API for dynamic real-time query responses.

## Features
- **Wake-word Detection:** Continuously listens for the wake-word ("Jarvis") using Google Speech Recognition.
- **Voice Response:** Converts text output into synthesized speech using `pyttsx3`.
- **System Automation:** Hands-free execution to launch desktop applications (Notepad, Spotify) and web navigation (YouTube, Google).
- **Music Playback:** Custom local audio library mapping for automated song playback.
- **AI-Powered Conversations:** Leverages OpenAI models with web search capabilities for complex or open-ended questions.
- **Event Logging:** Built-in logging (`jarvis.log`) to monitor conversation flows and handle network or API exceptions cleanly.

## Tech Stack
- **Language:** Python 3.10+
- **Speech & Audio:** `SpeechRecognition`, `pyttsx3`
- **AI & Web Services:** OpenAI API, `webbrowser`, `subprocess`
- **Environment & Logging:** `python-dotenv`, `logging`

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mdshahid0077/Desktop-Voice-Assistant.git
   cd Desktop-Voice-Assistant
