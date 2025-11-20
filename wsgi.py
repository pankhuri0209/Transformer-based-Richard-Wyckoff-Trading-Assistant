"""
WSGI entry point for Render deployment.
This file imports the Flask app from the Wyckoff_chatbot directory.
"""
import sys
import os

# Add the Wyckoff_chatbot directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Wyckoff_chatbot'))

# Import the Flask app from Wyckoff_chatbot/app.py
from app import app

if __name__ == '__main__':
    app.run()
