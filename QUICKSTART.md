# Quick Start Guide

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sanjeevzxcd/AI-Assistant.git
   cd AI-Assistant
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **(Optional) Install system dependencies for voice features:**
   
   **Ubuntu/Debian:**
   ```bash
   sudo apt-get install portaudio19-dev espeak
   ```
   
   **macOS:**
   ```bash
   brew install portaudio espeak
   ```
   
   **Windows:**
   - PyAudio and pyttsx3 should work out of the box
   - If issues occur, install from pre-built wheels

## Running the Assistant

### Interactive Mode (Recommended)

```bash
python main.py
```

This starts the assistant in interactive mode where you can talk to it or type commands.

### Demo Mode

```bash
python demo.py
```

This runs a demonstration of the assistant's capabilities.

### Test Mode

```bash
python test_assistant.py
```

This runs automated tests to verify the assistant is working correctly.

## Basic Usage Examples

Once the assistant is running, try these commands:

```
You: Hello
Assistant: Hello! I'm Assistant. How can I help you today?

You: What time is it?
Assistant: The current time is 03:45 PM

You: What's the date today?
Assistant: Today is Tuesday, October 21, 2025

You: Tell me about Python programming
Assistant: [Returns Wikipedia summary about Python]

You: Search for AI news
Assistant: Opening web search for: AI news

You: Help
Assistant: [Shows list of available commands]

You: Exit
Assistant: Goodbye!
```

## Customizing the Assistant

### Method 1: Edit config.py

Change settings like assistant name, language, speech rate, etc.

### Method 2: Extend the Assistant Class

See `example_custom_commands.py` for how to add your own commands:

```python
from assistant import AIAssistant

class MyAssistant(AIAssistant):
    def process_command(self, command):
        if 'my_custom_command' in command:
            return "Custom response"
        return super().process_command(command)

assistant = MyAssistant()
assistant.run()
```

## Troubleshooting

**Problem:** "Could not initialize microphone"
- **Solution:** Install PyAudio or use text input mode (works automatically)

**Problem:** "Could not initialize text-to-speech engine"
- **Solution:** Install espeak/espeak-ng or use text output mode (works automatically)

**Problem:** Weather feature not working
- **Solution:** Add your OpenWeatherMap API key to `config.py`

**Problem:** Wikipedia/Web features not working
- **Solution:** Check your internet connection

## Features

✅ Voice and text input/output
✅ Time and date queries
✅ Weather information
✅ Wikipedia searches
✅ Web searches
✅ Website opening
✅ Extensible command system
✅ Automatic fallback to text mode
✅ Help system

## Next Steps

1. Add your API keys to `config.py` for additional features
2. Customize the assistant name and settings
3. Add your own custom commands (see `example_custom_commands.py`)
4. Integrate with other services and APIs

Enjoy your AI Assistant! 🤖
