<h1>📘 Quizly API</h1>

<p>
Quizly is an AI-powered backend that converts YouTube videos into interactive quizzes.
The system downloads videos, extracts audio, transcribes speech, and generates
structured quiz questions using AI.
</p>

<hr>

<h2>🚀 Features</h2>

<ul>
<li>🎥 YouTube Video Processing</li>
<li>🎙 Speech-to-Text Transcription</li>
<li>🤖 AI Question Generation</li>
<li>🔐 Authentication System</li>
<li>📊 Quiz CRUD API</li>
<li>⚡ Modular Django Architecture</li>
</ul>

<hr>

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

<hr>

<h2>⚙️ Requirements</h2>

<ul>
<li>Python 3.10+</li>
<li>pip</li>
<li>virtualenv</li>
<li>FFmpeg (Required)</li>
</ul>

<hr>

<h2>⚠️ Important: Install FFmpeg</h2>

<p>
FFmpeg is required for extracting audio from YouTube videos and running transcription.
Without FFmpeg, quiz generation will fail.
</p>

<h3>Install FFmpeg</h3>

<p>Download FFmpeg:</p>

<pre>
https://ffmpeg.org/download.html
</pre>

<p>Verify installation:</p>

<pre>
ffmpeg -version
</pre>

<p>
If installed correctly, version information will be displayed.
</p>

<hr>

<h2>⚙️ Installation</h2>

<h3>Clone Repository</h3>

<pre>
git clone repository_url
cd Quizly
</pre>

<h3>Create Virtual Environment</h3>

<p>Windows:</p>

<pre>
python -m venv env
env\Scripts\activate
</pre>

<p>Linux / macOS:</p>

<pre>
python3 -m venv env
source env/bin/activate
</pre>

<h3>Install Dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

<hr>

<h2>🌱 Environment Variables</h2>

<p>Create a <code>.env</code> file:</p>

<pre>
cp .env.example .env
</pre>

<p>Example:</p>

<pre>
DJANGO_SECRET_KEY=
GEMINI_API_KEY=
</pre>

<hr>

<h2>🚀 Run Server</h2>

<pre>
python manage.py migrate
python manage.py runserver
</pre>

<hr>

<h2>🔐 Authentication Endpoints</h2>

<h3>Register</h3>

<p><code>POST /api/register/</code></p>

<pre>
{
"username": "username",
"password": "password",
"confirmed_password": "password",
"email": "email@example.com"
}
</pre>

<h3>Login</h3>

<p><code>POST /api/login/</code></p>

<h3>Logout</h3>

<p><code>POST /api/logout/</code></p>

<h3>Refresh Token</h3>

<p><code>POST /api/token/refresh/</code></p>

<hr>

<h2>🎥 Quiz Endpoints</h2>

<h3>Create Quiz</h3>

<p><code>POST /api/createQuiz/</code></p>

<pre>
{
"url": "https://youtube.com/..."
}
</pre>

<h3>Get All Quizzes</h3>

<p><code>GET /api/quizzes/</code></p>

<h3>Get Quiz</h3>

<p><code>GET /api/quizzes/{id}/</code></p>

<h3>Update Quiz</h3>

<p><code>PATCH /api/quizzes/{id}/</code></p>

<h3>Delete Quiz</h3>

<p><code>DELETE /api/quizzes/{id}/</code></p>

<hr>

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
Quiz Storage
</pre>

<hr>

<h2>📦 Key Technologies</h2>

<ul>
<li>Django</li>
<li>Django REST Framework</li>
<li>SimpleJWT</li>
<li>yt-dlp</li>
<li>Whisper</li>
<li>Google Gemini</li>
<li>FFmpeg</li>
</ul>

<hr>

<h2>Error Codes</h2>

<table>
<tr>
<th>Code</th>
<th>Description</th>
</tr>

<tr>
<td>200</td>
<td>Success</td>
</tr>

<tr>
<td>201</td>
<td>Created</td>
</tr>

<tr>
<td>204</td>
<td>Deleted</td>
</tr>

<tr>
<td>400</td>
<td>Bad Request</td>
</tr>

<tr>
<td>401</td>
<td>Unauthorized</td>
</tr>

<tr>
<td>403</td>
<td>Forbidden</td>
</tr>

<tr>
<td>404</td>
<td>Not Found</td>
</tr>

<tr>
<td>500</td>
<td>Server Error</td>
</tr>

</table>

<hr>

<h2>🤝 Contributing</h2>

<p>
Contributions are welcome.  
Please open an issue or submit a pull request.
</p>

<hr>

<h2>📄 License</h2>

<p>MIT License © alexschoefer</p>