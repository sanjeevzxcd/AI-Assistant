# AI-Assistant
A Python-based voice-enabled AI assistant that can help with various tasks including weather updates, web searches, Wikipedia queries, and more.

## Features

- 🎤 **Voice Input**: Speech recognition for hands-free interaction
- 🔊 **Voice Output**: Text-to-speech for spoken responses
- 🌤️ **Weather Updates**: Get current weather information for any city
- 🔍 **Web Search**: Quick Google searches
- 📚 **Wikipedia Integration**: Get information from Wikipedia
- ⏰ **Time & Date**: Ask for current time and date
- 🌐 **Website Opening**: Open websites in your browser
- ⌨️ **Text Mode**: Works with or without voice capabilities

## Installation

1. Clone the repository:
```bash
git clone https://github.com/sanjeevzxcd/AI-Assistant.git
cd AI-Assistant
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. For voice input support, you may need to install PyAudio system dependencies:

**On Ubuntu/Debian:**
```bash
sudo apt-get install portaudio19-dev python3-pyaudio
```

**On macOS:**
```bash
brew install portaudio
```

**On Windows:**
PyAudio should install directly via pip.

## Configuration

Edit `config.py` to customize your assistant:

- `ASSISTANT_NAME`: Change the assistant's name
- `SPEECH_LANGUAGE`: Set the language for speech recognition
- `TTS_RATE`: Adjust speech speed
- `WEATHER_API_KEY`: Add your OpenWeatherMap API key for weather features
- `DEBUG_MODE`: Enable detailed logging

## Usage

Run the assistant:
```bash
python main.py
```

The assistant will start in voice mode if a microphone is available, or text mode otherwise.

### Example Commands

- **Greetings**: "Hello", "Hi"
- **Time**: "What time is it?"
- **Date**: "What's the date today?"
- **Weather**: "What's the weather in London?"
- **Wikipedia**: "Tell me about Python programming"
- **Web Search**: "Search for AI news"
- **Open Website**: "Open youtube.com"
- **Help**: "Help"
- **Exit**: "Exit", "Bye", "Quit"

## Project Structure

```
AI-Assistant/
├── main.py                      # Main entry point
├── assistant.py                 # Core assistant logic
├── speech_recognition_module.py # Voice input handling
├── text_to_speech.py           # Voice output handling
├── utils.py                    # Utility functions
├── config.py                   # Configuration settings
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## Requirements

- Python 3.7+
- Internet connection (for speech recognition, weather, Wikipedia, etc.)
- Microphone (optional, for voice input)
- Speakers (optional, for voice output)

## API Keys

To use weather features, you'll need:
- **OpenWeatherMap API Key**: Sign up at [openweathermap.org](https://openweathermap.org/api) and add your key to `config.py`

## Troubleshooting

**Voice input not working:**
- Check if your microphone is properly connected
- Ensure PyAudio is correctly installed
- The assistant will fall back to text input mode automatically

**Voice output not working:**
- The assistant will fall back to text output mode automatically
- Check if pyttsx3 is properly installed

**Import errors:**
- Make sure all dependencies are installed: `pip install -r requirements.txt`

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is open source and available for personal use.

## Author

Created for self use by sanjeevzxcd
