from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")  # Securely load API key

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

    if request.method == "POST":
        try:
            print("hi1")
        except Exception as e:
            print("hi2")
            result = f"Error: {str(e)}"






    print("hi1")
    return render_template("museum.html")

if __name__ == "__main__":
    app.run(debug=True)  # Run locally for testing