"""
Text-to-speech module for AI Assistant
"""

import pyttsx3
from config import TTS_RATE, TTS_VOLUME, DEBUG_MODE


class TextToSpeech:
    """Handle text-to-speech functionality"""
    
    def __init__(self):
        self.engine = None
        self._initialize_engine()
    
    def _initialize_engine(self):
        """Initialize the text-to-speech engine"""
        try:
            self.engine = pyttsx3.init()
            self.engine.setProperty('rate', TTS_RATE)
            self.engine.setProperty('volume', TTS_VOLUME)
        except Exception as e:
            print(f"Warning: Could not initialize text-to-speech engine: {e}")
            print("Voice output will not be available.")
    
    def speak(self, text):
        """Convert text to speech"""
        if not self.engine:
            print(f"Assistant: {text}")
            return
        
        try:
            if DEBUG_MODE:
                print(f"Speaking: {text}")
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Error during speech synthesis: {e}")
            print(f"Assistant: {text}")
    
    def is_available(self):
        """Check if text-to-speech is available"""
        return self.engine is not None
