from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")  # Securely load API key

def prompts(inPrompt):
    print(inPrompt, flush=True)
    description = openai.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "developer",
                "content": (
                    "You are an art curator writing exclusively in International Art English. "
                    "Invent the artist and all references; do not quote or name real artists, "
                    "books, or literature. Use exaggerated French-origin English words combined "
                    "in a German style, sometimes joining words together. Use words such as "
                    "'space' ambiguously between physical and non-physical meanings."
                ),
            },
            {"role": "user", "content": f"Create an invented artist bio based on: {inPrompt}"},
            {
                "role": "assistant",
                "content": (
                    "Fartus Bunghole the Third, b. 1997, lives and works between Verdun and the cloud. "
                    "Grolu, an immortal being focused on the transient nature of the human condition."
                ),
            },
        ],
        temperature=1.6,
        max_output_tokens=50,
    )
    return description.output_text


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        prompt = request.form["prompt"]
        try:
            response = openai.responses.create(
                model="gpt-4.1",  
                input=[{"role": "developer", "content": "You are a psychedelic AI that speaks in Oulipian constraints. Your responses are short, surreal, and witty. Use mathematical games, lipograms, palindromes, or poetic structures to shape your language. Avoid predictable phrasing. Let logic slip through the cracks like liquid geometry."}, 
                          {"role": "user", "content": prompt}],
                          temperature=1.6,
                          max_output_tokens=50
            )
            result = response.output_text
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template("index.html", result=result)

@app.route("/museum", methods=["GET", "POST"])
def museum():
    result = None
    if request.method == "POST":
        try:
            prompt = request.form["prompt"]
            result = prompts(prompt)
        except Exception as e:
            result = f"Error: {str(e)}"


    return render_template("museum.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)  # Run locally for testing

#  (e.g., )
# Title and year
# Medium: real materials and abstractions can mix (e.g., “Polyester, elastic, fatigue”)
# Dimensions
# Provenance: the object’s history of ownership (e.g., “Found under a radiator, 2026; private collection of a dépanneur; acquired by the museum after a tense negotiation”)
# Credit line (e.g., “Gift of the artist’s backpack”)
# The extended label is 80–120 words. It must cite one invented theorist and their invented book.

