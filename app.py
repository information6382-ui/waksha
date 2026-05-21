from flask import Flask, request, jsonify, render_template
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

    data = request.json
    user_text = data.get("text")

    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "system",
                "content": "You are a savage Sinhala AI roaster called Waksha AI."
            },
            {
                "role": "user",
                "content": user_text
            }
        ]
    )

    reply = completion.choices[0].message.content

    return jsonify({
        "reply": reply
    })

app = app