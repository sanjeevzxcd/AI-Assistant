"""
Example: Extending the AI Assistant

This file shows how to add custom commands to the AI Assistant.
"""

from assistant import AIAssistant


class CustomAssistant(AIAssistant):
    """Extended AI Assistant with custom commands"""
    
    def process_command(self, command):
        """Override to add custom commands"""
        if not command:
            return None
        
        command = command.lower().strip()
        
        # Custom command: Calculator
        if 'calculate' in command or 'compute' in command:
            # Simple example: handle "calculate 2 plus 3"
            if 'plus' in command or '+' in command:
                try:
                    parts = command.replace('calculate', '').replace('compute', '')
                    parts = parts.replace('plus', '+')
                    result = eval(parts)
                    return f"The result is {result}"
                except:
                    return "I couldn't calculate that. Try something like 'calculate 2 plus 3'"
            return "Please specify a calculation, like 'calculate 2 plus 3'"
        
        # Custom command: Jokes
        elif 'joke' in command or 'funny' in command:
            jokes = [
                "Why do programmers prefer dark mode? Because light attracts bugs!",
                "Why did the programmer quit his job? Because he didn't get arrays!",
                "What's a programmer's favorite place? Foo Bar!"
            ]
            import random
            return random.choice(jokes)
        
        # Custom command: Motivational quote
        elif 'motivate' in command or 'motivation' in command:
            quotes = [
                "The only way to do great work is to love what you do. - Steve Jobs",
                "Innovation distinguishes between a leader and a follower. - Steve Jobs",
                "Code is like humor. When you have to explain it, it's bad. - Cory House"
            ]
            import random
            return random.choice(quotes)
        
        # Fall back to parent class for standard commands
        return super().process_command(command)


if __name__ == "__main__":
    print("\n" + "="*50)
    print("Custom AI Assistant Demo")
    print("="*50 + "\n")
    
    assistant = CustomAssistant()
    
    # Test custom commands
    test_commands = [
        "tell me a joke",
        "motivate me",
        "calculate 5 plus 3",
        "what time is it",  # Standard command
    ]
    
    for command in test_commands:
        print(f"User: {command}")
        response = assistant.process_command(command)
        if response:
            print(f"{assistant.name}: {response}\n")
    
    print("="*50)
    print("You can extend the assistant with your own commands!")
    print("="*50)
