"""
AI Assistant - Main Entry Point
A voice-enabled AI assistant that can help with various tasks
"""

import sys
from assistant import AIAssistant


def main():
    """Main function to run the AI Assistant"""
    print("=" * 50)
    print("AI Assistant")
    print("=" * 50)
    
    try:
        assistant = AIAssistant()
        assistant.run()
    except Exception as e:
        print(f"Failed to start assistant: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
