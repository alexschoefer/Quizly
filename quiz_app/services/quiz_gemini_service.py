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

def clean_llm_output(text):
    """Removes unwanted code block delimiters and prepares the text for JSON processing."""
    text = re.sub(r"```json|```", "", text).strip()
    return json.loads(text)