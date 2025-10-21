"""
Demo script for AI Assistant
Demonstrates basic usage and command processing
"""

from assistant import AIAssistant


def demo_basic_commands():
    """Demo basic commands"""
    print("\n" + "="*50)
    print("AI Assistant Demo - Basic Commands")
    print("="*50 + "\n")
    
    # Create assistant instance
    assistant = AIAssistant()
    
    # Demo commands
    commands = [
        "hello",
        "what time is it",
        "what's the date today",
        "tell me about Python programming language",
        "help",
    ]
    
    print("Running demo commands...\n")
    
    for command in commands:
        print(f"User: {command}")
        response = assistant.process_command(command)
        if response and response != "exit":
            print(f"{assistant.name}: {response}\n")
    
    print("="*50)
    print("Demo completed!")
    print("="*50 + "\n")


def demo_interactive_mode():
    """Demo interactive mode instructions"""
    print("\n" + "="*50)
    print("AI Assistant Demo - Interactive Mode")
    print("="*50 + "\n")
    
    print("To run the assistant in interactive mode, use:")
    print("  python main.py")
    print("\nThe assistant will:")
    print("  - Use voice input if a microphone is available")
    print("  - Use text input if no microphone is detected")
    print("  - Provide voice or text output based on availability")
    print("\nExample commands to try:")
    print("  - 'What time is it?'")
    print("  - 'What's the weather in London?'")
    print("  - 'Tell me about artificial intelligence'")
    print("  - 'Search for Python tutorials'")
    print("  - 'Open youtube.com'")
    print("  - 'Help' (to see all commands)")
    print("  - 'Exit' (to quit)")
    print("\n" + "="*50 + "\n")


if __name__ == "__main__":
    print("\n🤖 AI Assistant Demo\n")
    
    # Run basic commands demo
    demo_basic_commands()
    
    # Show interactive mode instructions
    demo_interactive_mode()
    
    print("For more information, see README.md")
    print("To install dependencies: pip install -r requirements.txt\n")
