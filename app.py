from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")  # Securely load API key

def promptName(inPrompt):
    print(inPrompt, flush=True)
    description = openai.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "developer",
                "content": (
                    "You are an art curator writing exclusively in International Art English. "
                    "Create an invented artist name and a short bio line based on the user's "
                    "artwork prompt. Do not quote or name real artists, books, or literature. "
                    "Use exaggerated French-origin English words combined in a German style, "
                    "sometimes joining words together. Use 'space' ambiguously between physical "
                    "and non-physical meanings. Return exactly two lines: an invented artist "
                    "name, then a bio line with birth year and where the artist lives and works. "
                    "Do not include a field label."
                ),
            },
            {
                "role": "user",
                "content": f"Create an invented artist bio based on: {inPrompt}",
            },
            {
                "role": "assistant",
                "content": (
                    "Fartus Bunghole the Third\nb. 1997, lives and works between Verdun and the cloud"
                ),
            },
        ],
        temperature=1.6,
        max_output_tokens=50,
    )
    return description.output_text


def promptTitle(inPrompt):
    description = openai.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "developer",
                "content": (
                    "You are an art curator. Turn the user's artwork prompt into a concise "
                    "artwork title and append the year 2027. Return only the title and year, "
                    "with no field label, in this format: [title], 2027."
                    "You are an art curator writing exclusively in International Art English. "
                    "Create an invented artist name and a short bio line based on the user's "
                    "artwork prompt. Do not quote or name real artists, books, or literature. "
                    "Use exaggerated French-origin English words combined in a German style, "
                    "sometimes joining words together. Use 'space' ambiguously between physical "
                    "and non-physical meanings. "
                ),
            },
            {
                "role": "user",
                "content": f"Create a title and year based on: {inPrompt}",
            },
            {
                "role": "assistant",
                "content": f"{inPrompt}, 2027",
            },
        ],
        temperature=1.6,
        max_output_tokens=50,
    )
    return description.output_text


def promptMedium(inPrompt):
    description = openai.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "developer",
                "content": (
                    "You are an art curator writing in International Art English. Invent a "
                    "concise artwork medium that combines real materials with abstractions "
                    "or emotions. Do not name real artists or artworks. Return only the medium, "
                    "without a field label."
                    "You are an art curator writing exclusively in International Art English. "
                    "Create an invented artist name and a short bio line based on the user's "
                    "artwork prompt. Do not quote or name real artists, books, or literature. "
                    "Use exaggerated French-origin English words combined in a German style, "
                    "sometimes joining words together. Use 'space' ambiguously between physical "
                    "and non-physical meanings. "
                ),
            },
            {
                "role": "user",
                "content": f"Invent a medium for an artwork based on: {inPrompt}",
            },
            {
                "role": "assistant",
                "content": "Polyester, elastic, fatigue",
            },
        ],
        temperature=1.6,
        max_output_tokens=50,
    )
    return description.output_text


def promptDimensions(inPrompt):
    description = openai.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "developer",
                "content": (
                    "You are an art curator. Invent plausible dimensions for an imagined "
                    "artwork suggested by the user's prompt. Include units and use a concise "
                    "format such as '42 × 31 × 18 cm' or 'Dimensions variable'. Return only "
                    "the dimensions without a field label."
                    "You are an art curator writing exclusively in International Art English. "
                    "Create an invented artist name and a short bio line based on the user's "
                    "artwork prompt. Do not quote or name real artists, books, or literature. "
                    "Use exaggerated French-origin English words combined in a German style, "
                    "sometimes joining words together. Use 'space' ambiguously between physical "
                    "and non-physical meanings. "
                ),
            },
            {
                "role": "user",
                "content": f"Invent dimensions for this artwork: {inPrompt}",
            },
            {
                "role": "assistant",
                "content": "42 × 31 × 18 cm",
            },
        ],
        temperature=1.6,
        max_output_tokens=50,
    )
    return description.output_text


def promptProvenance(inPrompt):
    description = openai.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "developer",
                "content": (
                    "You are an art curator. Invent a brief, surreal ownership history for "
                    "the imagined artwork suggested by the user's prompt. Use a few dated "
                    "stages, ending with its acquisition by a museum. Return only the "
                    "ownership history without a field label."
                    "You are an art curator writing exclusively in International Art English. "
                    "Create an invented artist name and a short bio line based on the user's "
                    "artwork prompt. Do not quote or name real artists, books, or literature. "
                    "Use exaggerated French-origin English words combined in a German style, "
                    "sometimes joining words together. Use 'space' ambiguously between physical "
                    "and non-physical meanings. "
                ),
            },
            {
                "role": "user",
                "content": f"Invent the provenance for this artwork: {inPrompt}",
            },
            {
                "role": "assistant",
                "content": (
                    "Found beneath a radiator, 2026; private collection of a "
                    "dépanneur; acquired by the museum after a tense negotiation."
                ),
            },
        ],
        temperature=1.6,
        max_output_tokens=100,
    )
    return description.output_text


def promptCreditLine(inPrompt):
    description = openai.responses.create(
        model="gpt-4.1",
        input=[

            {
                "role": "developer",
                "content": (
                    "You are an art curator. Invent a short, amusing museum credit line for "
                    "the imagined artwork suggested by the user's prompt. Return only the "
                    "credit line without a field label."
                    "You are an art curator writing exclusively in International Art English. "
                    "Create an invented artist name and a short bio line based on the user's "
                    "artwork prompt. Do not quote or name real artists, books, or literature. "
                    "Use exaggerated French-origin English words combined in a German style, "
                    "sometimes joining words together. Use 'space' ambiguously between physical "
                    "and non-physical meanings. "
                ),
            },

            {
                "role": "user",
                "content": f"Invent a credit line for this artwork: {inPrompt}",
            },

            {
                "role": "assistant",
                "content": "Courtesy of the household, subject to the cat's continuing disinterest",
            },

        ],
        temperature=1.6,
        max_output_tokens=50,
    )
    return description.output_text


def promptInsurance(inPrompt):
    description = openai.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "developer",
                "content": (
                    
                    "You are an art curator. Invent a plausible but amusing insurance line "
                    "for the imagined artwork based on the user's prompt. Include a value in "
                    "CAD and an absurd exclusion. Return only the line, without a field label, "
                    "in this format: Insured for CAD [amount], excluding [exclusion]."
                    "You are an art curator writing exclusively in International Art English. "
                    "Create an invented artist name and a short bio line based on the user's "
                    "artwork prompt. Do not quote or name real artists, books, or literature. "
                    "Use exaggerated French-origin English words combined in a German style, "
                    "sometimes joining words together. Use 'space' ambiguously between physical "
                    "and non-physical meanings."
                ),
            },
            {
                "role": "user",
                "content": f"Invent an insurance line for this artwork: {inPrompt}",
            },
            {
                "role": "assistant",
                "content": "Insured for CAD 3,000,000, excluding acts of indifference",
            },
        ],
        temperature=1.6,
        max_output_tokens=60,
    )
    return description.output_text


def promptExtendedLabel(inPrompt):
    description = openai.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "developer",
                "content": (
                    "You are an art curator writing in International Art English. Write an "
                    "80–120 word extended museum label about an imagined artwork based on "
                    "the user's prompt. Cite exactly one invented theorist and their invented "
                    "book. Do not name real artists, theorists, books, or literature. Count "
                    "the words in the label itself, including the theorist and book citation, "
                    "and keep the count between 80 and 120. Return only the paragraph, without "
                    "a field label."
                ),
            },
            {
                "role": "user",
                "content": f"Write the extended label for this artwork: {inPrompt}",
            },
            {
                "role": "assistant",
                "content": (
                    "This imagined work gathers its materials into a provisional "
                    "architecture of feeling, where the visible object and its absent double "
                    "occupy one unsettled space. Its surface proposes a quiet exchange between "
                    "use and reverie: each mark appears at once accidental and ceremonially "
                    "placed. The work's invented maker treats ordinary matter as a carrier of "
                    "unstable memory, allowing the familiar to become newly strange. Theorist "
                    "Mirelle Vask describes this condition in her invented book "
                    "'The Elastic Elsewhere,' where objects are said to remember futures that "
                    "have not yet arrived. Here, that proposition becomes a tactile invitation "
                    "to look again."
                ),
            },
        ],
        temperature=1.6,
        max_output_tokens=220,
    )
    return description.output_text


def prompts(inPrompt):
    artist_lines = promptName(inPrompt).strip().splitlines()
    artist_name = artist_lines[0] if artist_lines else ""
    artist_bio = " ".join(artist_lines[1:])

    return {
        "artist_name": artist_name,
        "artist_bio": artist_bio,
        "title": promptTitle(inPrompt).strip(),
        "medium": promptMedium(inPrompt).strip(),
        "dimensions": promptDimensions(inPrompt).strip(),
        "provenance": promptProvenance(inPrompt).strip(),
        "insurance": promptInsurance(inPrompt).strip(),
        "credit_line": promptCreditLine(inPrompt).strip(),
        "extended_label": promptExtendedLabel(inPrompt).strip(),
    }


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



# Artist: an invented name and a bio line (e.g., “b. 1997, lives and works between Verdun and the cloud”)
# Title and year #  (e.g. {prompt}, 2027 )
# Medium: real materials and abstractions can mix (e.g., “Polyester, elastic, fatigue”)
# Dimensions
# Provenance: the object’s history of ownership (e.g., “Found under a radiator, 2026; private collection of a dépanneur; acquired by the museum after a tense negotiation”)
# Credit line (e.g., “Gift of the artist’s backpack”)
# The extended label is 80–120 words. It must cite one invented theorist and their invented book.

