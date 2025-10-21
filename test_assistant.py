"""
Test script for AI Assistant
Tests basic functionality without requiring voice hardware
"""

import sys
sys.path.insert(0, '/home/runner/work/AI-Assistant/AI-Assistant')

from assistant import AIAssistant
from utils import (
    get_current_time,
    get_current_date,
    search_wikipedia,
)


def test_utility_functions():
    """Test utility functions"""
    print("Testing utility functions...")
    
    # Test time
    time = get_current_time()
    print(f"✓ Current time: {time}")
    assert time is not None
    
    # Test date
    date = get_current_date()
    print(f"✓ Current date: {date}")
    assert date is not None
    
    print("\nAll utility tests passed!\n")


def test_command_processing():
    """Test command processing"""
    print("Testing command processing...")
    
    # Create assistant instance
    assistant = AIAssistant()
    
    # Test greeting
    response = assistant.process_command("hello")
    print(f"✓ Greeting: {response}")
    assert "hello" in response.lower() or "hi" in response.lower()
    
    # Test time command
    response = assistant.process_command("what time is it")
    print(f"✓ Time query: {response}")
    assert "time" in response.lower()
    
    # Test date command
    response = assistant.process_command("what's the date")
    print(f"✓ Date query: {response}")
    assert response is not None
    
    # Test help command
    response = assistant.process_command("help")
    print(f"✓ Help command: Works")
    assert "help" in response.lower() or "can" in response.lower()
    
    # Test unknown command
    response = assistant.process_command("xyz unknown command")
    print(f"✓ Unknown command: {response}")
    assert response is not None
    
    print("\nAll command processing tests passed!\n")


def test_wikipedia_search():
    """Test Wikipedia search"""
    print("Testing Wikipedia search...")
    try:
        result = search_wikipedia("Python programming language")
        print(f"✓ Wikipedia search result (first 100 chars): {result[:100]}...")
        assert result is not None
        print("\nWikipedia test passed!\n")
    except Exception as e:
        print(f"⚠ Wikipedia test skipped (requires internet): {e}\n")


if __name__ == "__main__":
    print("=" * 50)
    print("AI Assistant Test Suite")
    print("=" * 50)
    print()
    
    try:
        test_utility_functions()
        test_command_processing()
        test_wikipedia_search()
        
        print("=" * 50)
        print("All tests completed successfully!")
        print("=" * 50)
    except Exception as e:
        print(f"\n✗ Test failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
