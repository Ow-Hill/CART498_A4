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
    " Always follow these three rules: (1) Write in English; describe the mundane object "
    "accurately and let humor come from its contrast with mock-serious art language. (2) "
    "Use the earlier IAE cues: French-influenced English, occasional German-style compounds, "
    "and physical/abstract uses of 'space'; keep a dryly amused tone. (3) Never use real "
    "artists, critics, curators, theorists, or books; cite one invented theorist and book in "
    "the extended label. Preserve each "
    "field's required length and format."
    "AVOID THE WORD ENNUI"
)


def catalogDeveloperPrompt(task, output_structure):
    return (
        "Role: Art curator writing fictional museum catalogue copy.\n"
        "Language: English.\n"
        f"Shared rules: {ART_STYLE_RULES}\n"
        f"Task: {task}\n"
        f"Output structure: {output_structure}\n"
        "Return only the requested field, without a field label."
    )


def catalogUserPrompt(inPrompt, field, prior_context=None):
    message = f"Original object prompt: {inPrompt}\n\nRequested field: {field}"
    if prior_context:
        message += f"\n\nPreviously generated catalogue details:\n{prior_context}"
    return message

def promptName(inPrompt):
    print(inPrompt, flush=True)
    description = openai.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "developer",
                "content": catalogDeveloperPrompt(
                    "Invent an artist name and concise bio for the object.",
                    "Exactly two lines: an invented artist name, then one short bio line "
                    "with birth year and where the artist lives and works.",
                ),
            },
            {
                "role": "user",
                "content": catalogUserPrompt(inPrompt, "Artist name and bio"),
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
    return inPrompt.strip()


def promptMedium(inPrompt):
    description = openai.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "developer",
                "content": catalogDeveloperPrompt(
                    "Invent a very concise medium for the object, combining real materials "
                    "RULE:THIS MUST MY A REAL MATERIAL",
                    "One short comma-separated list, such as 'Polyester, elastic, fatigue'.",
                ),
            },
            {
                "role": "user",
                "content": catalogUserPrompt(inPrompt, "Medium"),
            },
            {
                "role": "assistant",
                "content": "Polyester, elastic, Porcelyn",
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
                "content": catalogDeveloperPrompt(
                    "Invent plausible dimensions for the object and include units.",
                    "One concise value, such as '42 × 31 × 18 cm' or whatever dimensions make sense for the artwork.",
                ),
            },
            {
                "role": "user",
                "content": catalogUserPrompt(inPrompt, "Dimensions"),
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
                "content": catalogDeveloperPrompt(
                    "Invent a concise, dryly amusing ownership history for the object.",
                    "One short line with a few dated stages separated by semicolons, ending "
                    "with museum acquisition.",
                ),
            },
            {
                "role": "user",
                "content": catalogUserPrompt(inPrompt, "Provenance"),
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
                "content": catalogDeveloperPrompt(
                    "Invent a brief, dryly amusing museum credit line for the object.",
                    "One short phrase, such as 'Gift of the artist's backpack'.",
                ),
            },

            {
                "role": "user",
                "content": catalogUserPrompt(inPrompt, "Credit line"),
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
                "content": catalogDeveloperPrompt(
                    "Invent one concise, dryly amusing insurance line with a CAD value and "
                    "one leagalise sounding exclusion.",
                    "Insured for CAD [amount], excluding [exclusion].",
                ),
            },
            {
                "role": "user",
                "content": catalogUserPrompt(inPrompt, "Insurance"),
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
                "content": catalogDeveloperPrompt(
                    "Write an extended museum label for the object, consistent with the "
                    "earlier catalogue details.",
                    "One paragraph of 80–120 words, including exactly one citation to an "
                    "invented theorist and book in this format: (Invented Name, Invented "
                    "Book, 2026)." + ART_STYLE_RULES,
                ),
            },
            {
                "role": "user",
                "content": catalogUserPrompt(inPrompt, "Extended label", prior_context),
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
        "year": "2027",
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
        "Use the artwork name as the main cue and the label and original description to "
        "define the object. Depict a real, ordinary found or mass-produced item as a readymade, "
        "keeping its familiar form and everyday materials. It may have simple physical additions "
        "or be joined to another found object when the description calls for it; keep these "
        "changes plausible, visible, and secondary to the mundane object. Avoid a polished "
        "sculpture or fantasy design. If abstract, choose the everyday base object implied by "
        "the title and label. Preserve natural colors.\n\n"
        "Show the whole object at believable scale in a tall, sterile white room with a high "
        "ceiling, matte white painted wood walls with vertical seams, and a pale floor. Use "
        "quiet, matter-of-fact catalog photography. No people, text, labels, frames, or "
        "unrelated objects."
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
            "title": "A Door Practising Being a Window",
            "year": "2026",
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

