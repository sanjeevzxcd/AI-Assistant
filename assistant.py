"""
Main AI Assistant module
"""

import sys
from speech_recognition_module import SpeechRecognizer
from text_to_speech import TextToSpeech
from utils import (
    get_current_time,
    get_current_date,
    search_wikipedia,
    search_web,
    get_weather,
    open_website
)
from config import (
    ASSISTANT_NAME,
    WAKE_WORD,
    ENABLE_VOICE_INPUT,
    ENABLE_VOICE_OUTPUT,
    DEBUG_MODE
)


class AIAssistant:
    """Main AI Assistant class"""
    
    def __init__(self):
        self.name = ASSISTANT_NAME
        self.wake_word = WAKE_WORD
        
        # Initialize voice modules
        self.tts = TextToSpeech() if ENABLE_VOICE_OUTPUT else None
        self.speech_recognizer = SpeechRecognizer() if ENABLE_VOICE_INPUT else None
        
        # Check if voice features are available
        self.voice_input_available = (
            self.speech_recognizer and 
            self.speech_recognizer.is_available() if ENABLE_VOICE_INPUT else False
        )
        self.voice_output_available = (
            self.tts and 
            self.tts.is_available() if ENABLE_VOICE_OUTPUT else False
        )
    
    def speak(self, text):
        """Speak or print text"""
        if self.voice_output_available:
            self.tts.speak(text)
        else:
            print(f"{self.name}: {text}")
    
    def listen(self):
        """Listen for voice input or read from console"""
        if self.voice_input_available:
            return self.speech_recognizer.listen()
        else:
            try:
                return input("You: ").lower()
            except EOFError:
                return None
    
    def process_command(self, command):
        """Process user command and return response"""
        if not command:
            return None
        
        command = command.lower().strip()
        
        # Greeting
        if any(word in command for word in ['hello', 'hi', 'hey']):
            return f"Hello! I'm {self.name}. How can I help you today?"
        
        # Time
        elif any(phrase in command for phrase in ['what time', 'current time', 'time now']):
            time = get_current_time()
            return f"The current time is {time}"
        
        # Date
        elif any(phrase in command for phrase in ['what date', 'current date', 'date today', "what's the date", "today's date"]):
            date = get_current_date()
            return f"Today is {date}"
        
        # Weather
        elif 'weather' in command:
            # Extract city name (simple approach)
            if ' in ' in command:
                city = command.split(' in ')[-1].strip()
            elif ' at ' in command:
                city = command.split(' at ')[-1].strip()
            else:
                city = "London"  # Default city
            return get_weather(city)
        
        # Wikipedia
        elif any(phrase in command for phrase in ['wikipedia', 'wiki', 'tell me about', 'what is', 'who is']):
            # Extract search query
            query = command
            for phrase in ['wikipedia', 'wiki', 'tell me about', 'what is', 'who is']:
                query = query.replace(phrase, '').strip()
            if query:
                return search_wikipedia(query)
            else:
                return "What would you like me to search for?"
        
        # Web search
        elif any(phrase in command for phrase in ['search for', 'google', 'search']):
            query = command
            for phrase in ['search for', 'google', 'search']:
                query = query.replace(phrase, '').strip()
            if query:
                return search_web(query)
            else:
                return "What would you like me to search for?"
        
        # Open website
        elif any(phrase in command for phrase in ['open', 'visit']):
            if 'website' in command or 'site' in command:
                query = command
                for phrase in ['open', 'visit', 'website', 'site']:
                    query = query.replace(phrase, '').strip()
                if query:
                    return open_website(query)
            return "Please specify a website to open."
        
        # Exit commands
        elif any(word in command for word in ['exit', 'quit', 'bye', 'goodbye', 'stop']):
            return "exit"
        
        # Help
        elif 'help' in command:
            return self._get_help_message()
        
        # Unknown command
        else:
            return "I'm not sure how to help with that. Try asking for 'help' to see what I can do."
    
    def _get_help_message(self):
        """Return help message with available commands"""
        return """Here are some things I can help you with:
- Ask for the time: "What time is it?"
- Ask for the date: "What's the date?"
- Get weather: "What's the weather in London?"
- Wikipedia search: "Tell me about Python programming"
- Web search: "Search for AI news"
- Open websites: "Open youtube.com"
- Exit: "Bye" or "Exit"
"""
    
    def run(self):
        """Main loop for the assistant"""
        print(f"\n{self.name} initialized!")
        print(f"Voice input: {'Enabled' if self.voice_input_available else 'Disabled (text input mode)'}")
        print(f"Voice output: {'Enabled' if self.voice_output_available else 'Disabled (text output mode)'}")
        print(f"\nSay 'help' to see available commands or 'exit' to quit.\n")
        
        self.speak(f"Hello! I'm {self.name}. How can I help you?")
        
        while True:
            try:
                # Listen for command
                if self.voice_input_available:
                    print("\nListening...")
                
                command = self.listen()
                
                if command is None:
                    continue
                
                if DEBUG_MODE:
                    print(f"Command received: {command}")
                
                # Process command
                response = self.process_command(command)
                
                if response == "exit":
                    self.speak("Goodbye!")
                    break
                
                if response:
                    self.speak(response)
            
            except KeyboardInterrupt:
                print("\n")
                self.speak("Goodbye!")
                break
            except Exception as e:
                print(f"Error: {e}")
                if DEBUG_MODE:
                    import traceback
                    traceback.print_exc()
