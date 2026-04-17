<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Quizly Backend Documentation</title>

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

.footer {
text-align:center;
margin-top:60px;
opacity:0.6;
}

</style>

</head>

<body>

<div class="container">

<h1>🧠 Quizly Backend</h1>

<p>
Quizly is an AI-powered backend that generates quizzes from YouTube videos.
The system extracts transcripts, processes them using AI, and returns structured quiz questions.
</p>


<h2>🚀 Features</h2>

<div class="card">

<ul>
<li>🎥 YouTube Video Processing</li>
<li>🤖 AI Quiz Generation</li>
<li>🔐 Authentication</li>
<li>📊 Quiz API</li>
<li>⚡ Scalable Architecture</li>
<li>🔄 Redis Support</li>
</ul>

</div>


<h2>🏗️ Projektstruktur</h2>

<pre>

Quizly/
│
├── auth_app/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│
├── quiz_app/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── services/
│   │    ├── ai_service.py
│   │    ├── youtube_service.py
│   │
│   └── urls.py
│
├── core/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
└── .env

</pre>


<h2>🧰 Tech Stack</h2>

<div class="card">

<ul>
<li>Django</li>
<li>Django REST Framework</li>
<li>OpenAI API</li>
<li>YouTube API</li>
<li>Redis</li>
<li>PostgreSQL</li>
<li>Docker</li>
</ul>

</div>


<h2>⚙️ Installation</h2>

<pre>

git clone https://github.com/alexschoefer/Quizly.git

cd Quizly

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

</pre>


<h2>Environment Variables</h2>

<pre>

SECRET_KEY=

DEBUG=True

OPENAI_API_KEY=

YOUTUBE_API_KEY=

REDIS_URL=redis://localhost:6379

</pre>


<h2>🚀 Start Server</h2>

<pre>

python manage.py migrate

python manage.py runserver

</pre>


<h2>🔐 Authentication Endpoints</h2>

<div class="endpoint">

<span class="badge">POST</span>

<strong>/api/auth/register/</strong>

<pre>

{
"email": "user@test.com",
"password": "password"
}

</pre>

</div>


<div class="endpoint">

<span class="badge">POST</span>

<strong>/api/auth/login/</strong>

<pre>

{
"email": "user@test.com",
"password": "password"
}

</pre>

</div>


<div class="endpoint">

<span class="badge">GET</span>

<strong>/api/auth/profile/</strong>

</div>



<h2>🎥 Quiz Endpoints</h2>

<div class="endpoint">

<span class="badge">POST</span>

<strong>/api/quiz/generate/</strong>

<pre>

{
"youtube_url": "https://youtube.com/watch?v=..."

}

</pre>

</div>


<div class="endpoint">

<span class="badge">GET</span>

<strong>/api/quiz/{id}/</strong>

</div>


<div class="endpoint">

<span class="badge">POST</span>

<strong>/api/quiz/{id}/submit/</strong>

<pre>

{
"answers":[1,2,3]

}

</pre>

</div>



<div class="endpoint">

<span class="badge">GET</span>

<strong>/api/quiz/my/</strong>

</div>



<h2>🧠 Processing Flow</h2>

<pre>

YouTube Video

↓

Transcript Extraction

↓

AI Processing

↓

Quiz Generation

↓

Database Storage

↓

API Response

</pre>


<h2>📦 Requirements</h2>

<div class="card">

<ul>
<li>Python 3.10+</li>
<li>Redis</li>
<li>OpenAI API Key</li>
<li>YouTube API Key</li>
</ul>

</div>


<h2>🐳 Docker</h2>

<pre>

docker build -t quizly .

docker run -p 8000:8000 quizly

</pre>



<h2>🚀 Deployment</h2>

<div class="card">

<ul>
<li>AWS</li>
<li>Railway</li>
<li>Render</li>
<li>Docker VPS</li>
</ul>

</div>



<h2>📈 Future Features</h2>

<ul>

<li>Realtime Quiz</li>

<li>Multiplayer Quiz</li>

<li>Analytics Dashboard</li>

<li>Mobile API</li>

</ul>



<div class="footer">

Quizly Backend • AI Quiz Generator

</div>


</div>

</body>

</html>