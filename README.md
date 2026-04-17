📘 Quizly API
Overview
Quizly is an AI-powered backend that converts YouTube videos into interactive quizzes.
The system:
Downloads YouTube videos
Extracts audio
Transcribes speech to text
Generates AI-based questions
Stores quizzes in database
This enables users to quickly transform educational videos into interactive learning experiences.
🚀 Features
🎥 YouTube Video Processing
🎙 Speech-to-Text Transcription
🤖 AI Question Generation
🔐 Secure Authentication
📊 Quiz CRUD API
⚡ Modular Django Architecture
🏗 Project Structure
quiz_project/
│
├── core/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── quiz_app/
│   ├── api/
│   │   ├── views.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── permissions.py
│   │   └── helpers.py
│   │
│   ├── models.py
│   └── authentication.py
│
├── auth_app/
│   ├── api/
│   │   ├── views.py
│   │   ├── serializers.py
│   │   └── urls.py
│   │
│   └── models.py
│
├── manage.py
├── requirements.txt
└── .env
⚙️ Requirements
Before running the project ensure you have:
Python 3.10+
pip
virtualenv
FFmpeg (Required)
⚠️ IMPORTANT: Install FFmpeg
FFmpeg is required for:
Audio extraction
Video processing
Whisper transcription
Without FFmpeg, quiz generation will not work.
Install FFmpeg
Download:
https://ffmpeg.org/download.html
Verify Installation
ffmpeg -version
If installed correctly you should see version information.
⚙️ Installation
Clone repository
git clone <repository_url>
cd Quizly
Create virtual environment
Windows
python -m venv env
env\Scripts\activate
Linux / macOS
python3 -m venv env
source env/bin/activate
Install dependencies
pip install -r requirements.txt
🌱 Environment Variables
Create .env file
cp .env.example .env
Example:
DJANGO_SECRET_KEY=

GEMINI_API_KEY=
Never commit .env to Git.
🚀 Run Server
Run migrations
python manage.py migrate
Create superuser
python manage.py createsuperuser
Start server
python manage.py runserver
Server available at:
http://127.0.0.1:8000/
🔐 Authentication
Authentication uses:
Access Token
Refresh Token
HttpOnly Cookies
🔐 Auth Endpoints
Register
POST /api/register/
{
"username": "username",
"password": "password",
"confirmed_password": "password",
"email": "email@example.com"
}
Login
POST /api/login/
{
"username": "username",
"password": "password"
}
Logout
POST /api/logout/
Refresh Token
POST /api/token/refresh/
🎥 Quiz Endpoints
Create Quiz
POST /api/createQuiz/
{
"url": "https://youtube.com/..."
}
Get All Quizzes
GET /api/quizzes/
Get Quiz
GET /api/quizzes/{id}/
Update Quiz
PATCH /api/quizzes/{id}/
Delete Quiz
DELETE /api/quizzes/{id}/
🧠 Processing Flow
YouTube URL
     ↓
Video Download (yt-dlp)
     ↓
Audio Extraction (FFmpeg)
     ↓
Speech-to-Text (Whisper)
     ↓
AI Question Generation (Gemini)
     ↓
Database Storage
     ↓
API Response
📦 Key Technologies
Django
Django REST Framework
SimpleJWT
yt-dlp
Whisper
Google Gemini
FFmpeg