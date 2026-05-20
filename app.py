from flask import Flask, render_template, request, jsonify
from groq import Groq
import os

app = Flask(__name__)

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/roast", methods=["POST"])
def roast():

    data = request.get_json()

    name = data.get("name")

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are a funny Sri Lankan roast AI."
            },
            {
                "role": "user",
                "content": f"Roast this person in Sinhala funny style: {name}"
            }
        ]
    )

    reply = completion.choices[0].message.content

    return jsonify({
        "reply": reply
    })

application = app