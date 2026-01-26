A Django-based web application with REST API and LLM integration for working with devices and documents.

Features:
User registration and authentication
REST API built with Django REST Framework
Device management
Chat / LLM logic powered by LangChain
Document search and web search
File upload and processing (PDF, DOCX, TXT)

Tech Stack:
Python
Django
Django REST Framework
django-allauth
LangChain
FAISS
HuggingFace / Google GenAI

Installation:
1. Clone the repository
git clone <repo_url>
cd <project_folder>
2. Create a virtual environment
python -m venv venv
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt

Configuration:
Create a .env file or set environment variables:
SECRET_KEY=your_secret_key
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key

Rename test_settings.py to settings.py and configure the database settings.

Run the project:
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

The application will be available at:
http://127.0.0.1:8000/auth/

Notes:
This project is a pet project