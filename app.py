from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")  # Securely load API key

# vars,
globalTemp = 0.5
ART_STYLE_RULES = (
    " Always follow these three rules: (1) Write entirely in English and keep the user's "
    "mundane object, ordinary form, and relevant materials precise; let humor come from "
    "the contrast with inflated art language, never from making the object vague. (2) Use "
    "the IAE features named in the earlier prompts: exaggerated French-origin English "
    "word choices, occasional German-style compounds, and 'space' used for both physical "
    "and abstract meanings. Keep all vocabulary English and preserve each field's format. "
    "(3) Invent every artist, critic, curator, theorist, book, and reputation; never name or "
    "quote a real person or attribute work or ideas to them. In the extended label, cite "
    "exactly one invented theorist and invented book. Keep all field lengths and structures."
)

def promptName(inPrompt):
    print(inPrompt, flush=True)
    description = openai.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "developer",
                "content": (
                    "You are an art curator. Write entirely in English, even if the user's "
                    "prompt is in another language. Invent an artist name and a concise bio "
                    "based on the user's artwork prompt. Do not use real artists, critics, "
                    "curators, books, or literature. Return exactly two lines: an invented "
                    "artist name, then one "
                    "short bio line with birth year and where the artist lives and works. "
                    "Do not include field labels."
                ) + ART_STYLE_RULES,
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
        temperature=globalTemp,
        max_output_tokens=35,
    )
    return description.output_text


def promptTitle(inPrompt):
    description = openai.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "developer",
                "content": (
                    "You are an art curator. Write entirely in English, even if the user's "
                    "prompt is in another language. Create a concise title based on the "
                    "artwork prompt and append the year 2027. Return only the title and year, "
                    "without a field label, in this format: [title], 2027. Do not name real "
                    "artists, critics, curators, books, or literature."
                ) + ART_STYLE_RULES,
            },
            {
                "role": "user",
                "content": f"Create a title and year based on: {inPrompt}",
            },
            {
                "role": "assistant",
                "content": "An Ordinary Spoon Waiting for Applause, 2027",
            },
        ],
        temperature=globalTemp,
        max_output_tokens=24,
    )
    return description.output_text


def promptMedium(inPrompt):
    description = openai.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "developer",
                "content": (
                    "You are an art curator. Write entirely in English, even if the user's "
                    "prompt is in another language. Invent a very concise artwork medium from "
                    "the prompt, combining real materials with one abstraction or emotion. "
                    "Return only the medium, without a field label, in a short list like "
                    "'Polyester, elastic, fatigue'. Do not name real artists or artworks."
                ) + ART_STYLE_RULES,
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
        temperature=globalTemp,
        max_output_tokens=16,
    )
    return description.output_text


def promptDimensions(inPrompt):
    description = openai.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "developer",
                "content": (
                    "You are an art curator. Write any words in English, even if the user's "
                    "prompt is in another language. Invent plausible artwork dimensions from "
                    "the prompt, include units, and return only a concise value such as "
                    "'42 × 31 × 18 cm' or 'Dimensions variable'. Do not add a field label."
                ) + ART_STYLE_RULES,
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
        temperature=globalTemp,
        max_output_tokens=16,
    )
    return description.output_text


def promptProvenance(inPrompt):
    description = openai.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "developer",
                "content": (
                    "You are an art curator. Write entirely in English, even if the user's "
                    "prompt is in another language. Invent a concise, surreal ownership "
                    "history based on the prompt, using a few dated stages separated by "
                    "semicolons and ending with museum acquisition. Keep it to one short line. "
                    "Return only the ownership history, without a field label."
                ) + ART_STYLE_RULES,
            },
            {
                "role": "user",
                "content": f"Invent the provenance for this artwork: {inPrompt}",
            },
            {
                "role": "assistant",
                "content": (
                    "Found beneath a radiator, 2026; private collection of a corner shop; "
                    "acquired by the museum after a tense negotiation."
                ),
            },
        ],
        temperature=globalTemp,
        max_output_tokens=35,
    )
    return description.output_text


def promptCreditLine(inPrompt):
    description = openai.responses.create(
        model="gpt-4.1",
        input=[

            {
                "role": "developer",
                "content": (
                    "You are an art curator. Write entirely in English, even if the user's "
                    "prompt is in another language. Invent a brief, amusing museum credit "
                    "line based on the prompt. Keep it to one short phrase, such as 'Gift of "
                    "the artist's backpack'. Return only the credit line, without a field label."
                ) + ART_STYLE_RULES,
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
        temperature=globalTemp,
        max_output_tokens=20,
    )
    return description.output_text


def promptInsurance(inPrompt):
    description = openai.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "developer",
                "content": (
                    "You are an art curator. Write entirely in English, even if the user's "
                    "prompt is in another language. Invent one concise, amusing insurance "
                    "line based on the prompt, with a value in CAD and one absurd exclusion. "
                    "Return only the line, without a field label, in this format: Insured for "
                    "CAD [amount], excluding [exclusion]."
                ) + ART_STYLE_RULES,
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
        temperature=globalTemp,
        max_output_tokens=20,
    )
    return description.output_text


def promptExtendedLabel(inPrompt, prior_prompts):
    prior_context = "\n".join(
        f"{field.replace('_', ' ').title()}: {value}"
        for field, value in prior_prompts.items()
    )
    description = openai.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "developer",
                "content": (
                    "You are an art curator. Write entirely in English. Write an "
                    "80–120 word extended museum label about an imagined artwork based on "
                    "the user's prompt. Cite exactly one invented theorist and their invented "
                    "book in this parenthetical format: (Invented Name, Invented Book, 2026). "
                    "Do not name, quote, or attribute work or ideas to real artists, critics, "
                    "curators, theorists, books, or literature. Count "
                    "the words in the label itself, including the theorist and book citation, "
                    "and keep the count between 80 and 120. Build on the supplied artwork "
                    "details and keep the label consistent with them. Return only the "
                    "paragraph, without a field label."
                ) + ART_STYLE_RULES,
            },
            {
                "role": "user",
                "content": (
                    f"Original artwork prompt: {inPrompt}\n\n"
                    f"Previously generated artwork details:\n{prior_context}\n\n"
                    "Write the extended label using all of these details."
                ),
            },
            {
                "role": "assistant",
                "content": (
                    "This imagined work gathers its materials into a provisional "
                    "architecture of feeling, where the visible object and its absent double "
                    "occupy one unsettled space. Its surface proposes a quiet exchange between "
                    "use and reverie: each mark appears at once accidental and ceremonially "
                    "placed. The work's invented maker treats ordinary matter as a carrier of "
                    "unstable memory, allowing the familiar to become newly strange. This "
                    "condition is described as the object's future-bearing space in the "
                    "invented study of Mirelle Vask (Mirelle Vask, The Elastic Elsewhere, 2026). "
                    "Here, that proposition becomes a tactile invitation to look again."
                ),
            },
        ],
        temperature=globalTemp,
        max_output_tokens=220,
    )
    return description.output_text


def prompts(inPrompt):
    artist_lines = promptName(inPrompt).strip().splitlines()
    artist_name = artist_lines[0] if artist_lines else ""
    artist_bio = " ".join(artist_lines[1:])

    result = {
        "artist_name": artist_name,
        "artist_bio": artist_bio,
        "title": promptTitle(inPrompt).strip(),
        "medium": promptMedium(inPrompt).strip(),
        "dimensions": promptDimensions(inPrompt).strip(),
        "provenance": promptProvenance(inPrompt).strip(),
        "insurance": promptInsurance(inPrompt).strip(),
        "credit_line": promptCreditLine(inPrompt).strip(),
    }
    result["extended_label"] = promptExtendedLabel(inPrompt, result).strip()
    return result


def generateArtworkImage(inPrompt, generated_result):
    image_prompt = (
        f"Artwork name (use this as the main image prompt): {generated_result['title']}\n"
        f"Generated museum label: {generated_result['extended_label']}\n"
        f"Original object description: {inPrompt}\n"
        f"Generated medium: {generated_result['medium']}\n\n"
        "Use the artwork name as the main subject cue, and use the label and original "
        "description to decide exactly what the object is. Create a realistic interior "
        "photograph of one genuinely mundane readymade: a "
        "recognizable, ordinary, mass-produced or found object with a clear everyday use, "
        "such as a cup, stool, bag, tool, bottle, or household appliance. If the user names "
        "a concrete object, depict that exact object; do not substitute another. If the prompt "
        "is abstract, choose one ordinary item most strongly implied by the generated title, "
        "description, and concrete materials in the medium. Do not turn abstract medium terms "
        "into physical effects. Keep its normal "
        "function, familiar shape, materials, believable scale, and natural colors. Show it "
        "unchanged or with only minimal alteration. It must look like an actual everyday "
        "object, not a sculpture, art installation, prototype, or fantasy object.\n\n"
        "Place the item inside a tall, sterile white room with a high ceiling, matte white "
        "painted wood walls, subtle vertical wood-panel seams, and a plain pale floor. Make "
        "the room feel clean, quiet, and minimally furnished. Show the whole item clearly at "
        "a believable scale, as the main subject, with the room's height visible around it. "
        "Use straightforward natural interior photography. Do not add other objects, people, "
        "writing, labels, visible words from the artwork name, picture frames, surreal "
        "effects, or changes to the item's colors."
    )

    image_response = openai.images.generate(
        model="gpt-image-2.5-flare",
        prompt=image_prompt,
        n=1,
        size="1536x1024",
        quality="medium",
        output_format="png",
    )
    image_base64 = image_response.data[0].b64_json
    return f"data:image/png;base64,{image_base64}"


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        prompt = request.form["prompt"]
        try:
            response = openai.responses.create(
                model="gpt-4.1",  
                input=[{"role": "developer", "content": "Respond only in English. You are a psychedelic AI that speaks in Oulipian constraints. Your responses are short, surreal, and witty. Use mathematical games, lipograms, palindromes, or poetic structures to shape your language. Avoid predictable phrasing. Let logic slip through the cracks like liquid geometry."}, 
                      {"role": "user", "content": prompt}],
                      temperature=globalTemp,
                      max_output_tokens=50
            )
            result = response.output_text
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template("index.html", result=result)

@app.route("/museum", methods=["GET", "POST"])
def museum():
    result = None
    dev_preview = False
    if request.method == "POST":
        try:
            prompt = request.form["prompt"]
            result = prompts(prompt)
            result["artwork_data_uri"] = generateArtworkImage(prompt, result)
        except Exception as e:
            result = f"Error: {str(e)}"
    elif request.args.get("preview") == "1":
        dev_preview = True
        result = {
            "artist_name": "Mireille Vask",
            "artist_bio": "b. 1984, lives and works between Montréal and the soft edge of a teaspoon",
            "title": "A Door Practising Being a Window (2026)",
            "medium": "Wood, borrowed light, administrative hesitation",
            "dimensions": "61 × 94 × 8 cm",
            "provenance": "Found leaning toward an unopened room; acquired after a brief exchange of weather.",
            "insurance": "Insured for CAD 18,400, excluding sudden certainty.",
            "credit_line": "Courtesy of the artist and the corridor that kept it ajar.",
            "extended_label": (
                "This imagined work holds its threshold in a state of courteous uncertainty. "
                "Neither entry nor view is fully granted; instead, the object rehearses the "
                "small negotiations by which space becomes available. Its borrowed light "
                "gathers along the grain, suggesting that passage may be less a movement "
                "through architecture than a temporary agreement with it. Mireille Vask "
                "describes this condition in The Elastic Elsewhere, where the ordinary "
                "object is understood as a site of unfinished arrival."
            ),
        }
    return render_template("museum.html", result=result, dev_preview=dev_preview)

if __name__ == "__main__":
    app.run(debug=True)  # Run locally for testing



# Artist: an invented name and a bio line (e.g., “b. 1997, lives and works between Verdun and the cloud”)
# Title and year #  (e.g. {prompt}, 2027 )
# Medium: real materials and abstractions can mix (e.g., “Polyester, elastic, fatigue”)
# Dimensions
# Provenance: the object’s history of ownership (e.g., “Found under a radiator, 2026; private collection of a dépanneur; acquired by the museum after a tense negotiation”)
# Credit line (e.g., “Gift of the artist’s backpack”)
# The extended label is 80–120 words. It must cite one invented theorist and their invented book.

