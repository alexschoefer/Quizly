# 📘 Quizly API

Quizly is an AI-powered backend that converts YouTube videos into interactive quizzes.
The system downloads videos, extracts audio, transcribes speech, and generates structured quiz questions using AI.

---

# 🚀 Features

* 🎥 YouTube Video Processing
* 🎙 Speech-to-Text Transcription
* 🤖 AI Question Generation
* 🔐 Authentication System
* 📊 Quiz CRUD API
* ⚡ Modular Django Architecture

---

# 🏗 Project Structure

```
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
```

---

# ⚙️ Requirements

* Python 3.10+
* pip
* virtualenv
* FFmpeg (Required)

---

# ⚠️ Important: Install FFmpeg

FFmpeg is required for extracting audio from YouTube videos and running transcription.
Without FFmpeg, quiz generation will fail.

## Install FFmpeg

Download FFmpeg:

```
https://ffmpeg.org/download.html
```

Verify installation:

```
ffmpeg -version
```

If installed correctly, version information will be displayed.

---

# ⚙️ Installation

## Clone Repository

```
git clone repository_url
cd Quizly
```

## Create Virtual Environment

### Windows

```
python -m venv env
env\Scripts\activate
```

### Linux / macOS

```
python3 -m venv env
source env/bin/activate
```

## Install Dependencies

```
pip install -r requirements.txt
```

---

# 🌱 Environment Variables

Create a `.env` file:

```
cp .env.example .env
```

Example:

```
GEMINI_API_KEY=your_gemini_api_key_here
DJANGO_SECRET_KEY=your-secret_django-key
```

---

# 🚀 Run Server

```
python manage.py migrate
python manage.py runserver
```

---

## Creating a Superuser

To access admin features or perform administrative tasks, create a superuser account:

1. Run `python manage.py createsuperuser`
2. Follow the prompts to enter a username, email, and password.
3. Use the superuser credentials to log in via the Django admin panel at `http://127.0.0.1:8000/admin/` or for API authentication.

This is useful for testing permissions, managing users, and accessing protected endpoints.

---

# 🔐 Authentication Endpoints

## Register

`POST /api/register/`

```json
{
  "username": "username",
  "password": "password",
  "confirmed_password": "password",
  "email": "email@example.com"
}
```

---

## Login

`POST /api/login/`

---

## Logout

`POST /api/logout/`

---

## Refresh Token

`POST /api/token/refresh/`

---

# 🎥 Quiz Endpoints

## Create Quiz

`POST /api/createQuiz/`

```json
{
"url": "https://youtube.com/..."
}
```

---

## Get All Quizzes

`GET /api/quizzes/`

---

## Get Quiz

`GET /api/quizzes/{id}/`

---

## Update Quiz

`PATCH /api/quizzes/{id}/`

---

## Delete Quiz

`DELETE /api/quizzes/{id}/`

---

# 🧠 Processing Flow

```
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
Quiz Storage
```

---

# 📦 Key Technologies

* Django
* Django REST Framework
* SimpleJWT
* yt-dlp
* Whisper
* Google Gemini
* FFmpeg

---

# Error Codes

| Code | Description  |
| ---- | ------------ |
| 200  | Success      |
| 201  | Created      |
| 204  | Deleted      |
| 400  | Bad Request  |
| 401  | Unauthorized |
| 403  | Forbidden    |
| 404  | Not Found    |
| 500  | Server Error |

---

# 🤝 Contributing

Contributions are welcome.
Please open an issue or submit a pull request.

---

# 📄 License

MIT License © alexschoefer
