"""
Speech recognition module for AI Assistant
"""

import speech_recognition as sr
from config import SPEECH_TIMEOUT, SPEECH_PHRASE_TIME_LIMIT, SPEECH_LANGUAGE, DEBUG_MODE


class SpeechRecognizer:
    """Handle speech recognition functionality"""
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = None
        self._initialize_microphone()
    
    def _initialize_microphone(self):
        """Initialize the microphone"""
        try:
            self.microphone = sr.Microphone()
            # Adjust for ambient noise
            with self.microphone as source:
                if DEBUG_MODE:
                    print("Adjusting for ambient noise... Please wait.")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
        except Exception as e:
            print(f"Warning: Could not initialize microphone: {e}")
            print("Voice input will not be available.")
    
    def listen(self):
        """Listen for audio input and convert to text"""
        if not self.microphone:
            return None
        
        try:
            with self.microphone as source:
                if DEBUG_MODE:
                    print("Listening...")
                audio = self.recognizer.listen(
                    source,
                    timeout=SPEECH_TIMEOUT,
                    phrase_time_limit=SPEECH_PHRASE_TIME_LIMIT
                )
            
            if DEBUG_MODE:
                print("Recognizing...")
            
            # Use Google Speech Recognition
            text = self.recognizer.recognize_google(audio, language=SPEECH_LANGUAGE)
            if DEBUG_MODE:
                print(f"Recognized: {text}")
            return text.lower()
        
        except sr.WaitTimeoutError:
            if DEBUG_MODE:
                print("No speech detected within timeout period.")
            return None
        except sr.UnknownValueError:
            if DEBUG_MODE:
                print("Could not understand audio.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from speech recognition service: {e}")
            return None
        except Exception as e:
            print(f"Error during speech recognition: {e}")
            return None
    
    def is_available(self):
        """Check if speech recognition is available"""
        return self.microphone is not None
