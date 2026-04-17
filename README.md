<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Quizly API Documentation</title>

<style>

body {
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
background: #0f172a;
color: #e2e8f0;
margin: 0;
padding: 0;
line-height: 1.6;
}

.container {
max-width: 1100px;
margin: auto;
padding: 40px 20px;
}

h1,h2,h3 {
color: #f8fafc;
}

h1 {
font-size: 42px;
border-bottom: 2px solid #334155;
padding-bottom: 10px;
}

h2 {
margin-top: 50px;
border-bottom: 1px solid #1e293b;
padding-bottom: 6px;
}

.card {
background: #020617;
padding: 20px;
border-radius: 12px;
margin-top: 20px;
border: 1px solid #1e293b;
}

pre {
background: #020617;
padding: 20px;
border-radius: 10px;
overflow-x: auto;
border: 1px solid #1e293b;
}

.endpoint {
background: #020617;
border-left: 4px solid #38bdf8;
padding: 16px;
margin-top: 15px;
border-radius: 6px;
}

.badge {
background: #1e293b;
padding: 4px 10px;
border-radius: 20px;
font-size: 12px;
margin-right: 8px;
}

.warning {
background: #3f1d1d;
border-left: 4px solid #ef4444;
padding: 16px;
margin-top: 20px;
border-radius: 8px;
}

.footer {
text-align:center;
margin-top:60px;
opacity:0.6;
}

</style>

</head>

<body>

<div class="container">

<h1>📘 Quizly API</h1>

<p>
Quizly is an AI-driven backend service that converts YouTube videos into interactive quizzes.
The system downloads video audio, performs speech-to-text transcription, and generates
structured quiz questions using modern AI models.
</p>

<h2>🚀 Core Features</h2>

<div class="card">

<ul>
<li>🎥 YouTube Video Processing</li>
<li>🎙 Speech-to-Text Transcription</li>
<li>🤖 AI Question Generation</li>
<li>🔐 Secure Authentication</li>
<li>📊 Quiz CRUD API</li>
<li>⚡ Modular Django Architecture</li>

</ul>

</div>


<h2>🏗 Project Structure</h2>

<pre>

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

</pre>


<h2>⚙️ Requirements</h2>

<div class="card">

<ul>
<li>Python 3.10+</li>
<li>pip</li>
<li>virtualenv</li>
<li>FFmpeg (Required)</li>

</ul>

</div>


<h2>⚠️ Important: Install FFmpeg</h2>

<div class="warning">

<p>
FFmpeg is mandatory for processing audio streams and extracting audio from YouTube videos.
Without FFmpeg the transcription pipeline will fail.
</p>

<ol>

<li>Download FFmpeg</li>

<pre>
https://ffmpeg.org/download.html
</pre>

<li>Extract the archive</li>

<li>Add <strong>bin</strong> folder to system PATH</li>

<li>Verify installation</li>

<pre>
ffmpeg -version
</pre>

</ol>

<p>
If FFmpeg is not installed correctly, audio extraction and transcription will not work.
</p>

</div>


<h2>⚙️ Installation</h2>

<pre>

git clone repository_url

cd repository

python -m venv env

</pre>

Activate Virtual Environment

Windows

<pre>

env\Scripts\activate

</pre>

Linux / macOS

<pre>

source env/bin/activate

</pre>


Install dependencies

<pre>

pip install -r requirements.txt

</pre>


<h2>🌱 Environment Variables</h2>

<pre>

DJANGO_SECRET_KEY=

GEMINI_API_KEY=

</pre>


Create .env

<pre>

cp .env.example .env

</pre>


<h2>🚀 Run Server</h2>

<pre>

python manage.py migrate

python manage.py runserver

</pre>


<h2>🔐 Authentication Endpoints</h2>


<div class="endpoint">

<span class="badge">POST</span>

<strong>/api/register/</strong>

<pre>

{
"username": "username",
"password": "password",
"confirmed_password": "password",
"email": "user@email.com"
}

</pre>

</div>


<div class="endpoint">

<span class="badge">POST</span>

<strong>/api/login/</strong>

</div>


<div class="endpoint">

<span class="badge">POST</span>

<strong>/api/logout/</strong>

</div>


<div class="endpoint">

<span class="badge">POST</span>

<strong>/api/token/refresh/</strong>

</div>



<h2>🎥 Quiz Endpoints</h2>


<div class="endpoint">

<span class="badge">POST</span>

<strong>/api/createQuiz/</strong>

<pre>

{
"url":"https://youtube.com/..."
}

</pre>

</div>


<div class="endpoint">

<span class="badge">GET</span>

<strong>/api/quizzes/</strong>

</div>


<div class="endpoint">

<span class="badge">GET</span>

<strong>/api/quizzes/{id}/</strong>

</div>


<div class="endpoint">

<span class="badge">PATCH</span>

<strong>/api/quizzes/{id}/</strong>

</div>


<div class="endpoint">

<span class="badge">DELETE</span>

<strong>/api/quizzes/{id}/</strong>

</div>


<h2>🧠 Processing Flow</h2>

<pre>

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

</pre>


<h2>📦 Key Technologies</h2>

<div class="card">

<ul>

<li>Django</li>

<li>Django REST Framework</li>

<li>SimpleJWT</li>

<li>yt-dlp</li>

<li>Whisper</li>

<li>Google Gemini API</li>

<li>FFmpeg</li>

</ul>

</div>


<h2>Error Codes</h2>

<pre>

200 Success

201 Created

204 Deleted

400 Bad Request

401 Unauthorized

403 Forbidden

404 Not Found

500 Server Error

</pre>



<div class="footer">

Quizly API Documentation

</div>


</div>

</body>

</html>