import asyncio
import requests
import json
import threading
import time
import subprocess
import sys
import os

def start_server():
    """Start the backend server in a subprocess"""
    # Change to backend directory and start the server
    os.chdir("backend")
    process = subprocess.Popen([
        sys.executable, "-c",
        "import uvicorn; from src.main import app; uvicorn.run(app, host='127.0.0.1', port=8000)"
    ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process

def test_rag_system():
    """Test the RAG system with the mock database"""
    print("Starting RAG system test...")

    # Start the server in a separate process
    print("Starting backend server...")
    server_process = start_server()

    # Wait a few seconds for the server to start
    time.sleep(5)

    try:
        # Test the root endpoint
        print("Testing root endpoint...")
        response = requests.get("http://localhost:8000/")
        if response.status_code == 200:
            print("✓ Root endpoint working")
        else:
            print(f"✗ Root endpoint failed with status {response.status_code}")
            return False

        # Test the chat endpoint with a simple query
        print("Testing chat endpoint...")
        chat_payload = {
            "query": "What is humanoid robotics?",
            "history": []
        }

        response = requests.post(
            "http://localhost:8000/chat",
            json=chat_payload,
            headers={"Content-Type": "application/json"}
        )

        if response.status_code == 200:
            result = response.json()
            print("✓ Chat endpoint working")
            print(f"Response: {result.get('response', 'No response field')[:100]}...")
        else:
            print(f"✗ Chat endpoint failed with status {response.status_code}")
            print(f"Error: {response.text}")
            return False

        # Test the selected text endpoint
        print("Testing selected text endpoint...")
        selected_payload = {
            "query": "What does this text say?",
            "selected_text": "This is a sample selected text for testing.",
            "history": []
        }

        response = requests.post(
            "http://localhost:8000/chat/selected",
            json=selected_payload,
            headers={"Content-Type": "application/json"}
        )

        if response.status_code == 200:
            result = response.json()
            print("✓ Selected text endpoint working")
            print(f"Response: {result.get('response', 'No response field')[:100]}...")
        else:
            print(f"✗ Selected text endpoint failed with status {response.status_code}")
            print(f"Error: {response.text}")
            return False

        print("✓ All tests passed! RAG system is working correctly.")
        return True

    except Exception as e:
        print(f"✗ Test failed with exception: {e}")
        return False
    finally:
        # Terminate the server process
        server_process.terminate()
        server_process.wait()

if __name__ == "__main__":
    success = test_rag_system()
    if success:
        print("\n🎉 RAG system test completed successfully!")
        print("The system is ready to use with mock database functionality.")
    else:
        print("\n❌ RAG system test failed.")
        sys.exit(1)