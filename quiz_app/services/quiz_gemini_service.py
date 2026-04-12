from google import genai
import json
from django.conf import settings
import re

QUIZ_GEMINI_PROMPT = """
    Basierend auf dem folgenden Transkript erstelle ein Quiz im gültigen JSON-Format.

    Das Quiz muss exakt folgende Struktur haben:

    {
    "title": "Erstelle einen kurzen, prägnanten Titel basierend auf dem Thema des Transkripts.",
    "description": "Fasse das Transkript in maximal 150 Zeichen zusammen. Enthält keine Fragen oder Antworten.",
    "questions": [
        {
        "question_title": "Die Frage steht hier.",
        "question_options": ["Option A", "Option B", "Option C", "Option D"],
        "answer": "Die korrekte Antwort aus den oben genannten Optionen"
        }
    ]
    }

    Anforderungen:

    - Genau 10 Fragen müssen enthalten sein.
    - Jede Frage muss genau 4 unterschiedliche Antwortmöglichkeiten haben.
    - Es darf nur eine korrekte Antwort pro Frage geben.
    - Die korrekte Antwort muss exakt einem der Einträge in "question_options" entsprechen.
    - Alle Texte (Titel, Beschreibung, Fragen, Antworten) müssen auf Deutsch sein.
    - Die Ausgabe muss valides JSON sein und direkt mit json.loads() verarbeitet werden können.
    - Gib ausschließlich JSON zurück – keine Erklärungen, kein zusätzlicher Text, keine Codeblöcke.

    """

def _create_prompt(transcript):
    """
    Combines the predefined quiz generation prompt with the provided transcript to create the final prompt for the Gemini API.
    The transcript is appended to the quiz generation prompt, separated by two newlines for clarity.
    """
    return QUIZ_GEMINI_PROMPT + "\n\n" + transcript

def clean_llm_output(text):
    """Removes unwanted code block delimiters and prepares the text for JSON processing."""
    text = re.sub(r"```json|```", "", text).strip()
    return json.loads(text)

def generate_quiz_from_transcript(transcript):
    """
    Generates a quiz based on the provided transcript using the Gemini API.
    """
    if not settings.GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY is not set")

    client = genai.Client(api_key=settings.GEMINI_API_KEY)

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=_create_prompt(transcript)
    )

    return clean_llm_output(response.text)

def validate_quiz_data(data):
    """
    Validates the structure and content of the quiz data to ensure it meets the specified requirements.
    """
    if len(data.get("questions", [])) != 10:
        raise ValueError("Invalid number of questions")

    for q in data["questions"]:
        if len(q["question_options"]) != 4:
            raise ValueError("Invalid number of options")
        if q["answer"] not in q["question_options"]:
            raise ValueError("Answer not in options")