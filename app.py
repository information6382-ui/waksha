from flask import Flask, request
from groq import Groq
import os

app = Flask(__name__)

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

@app.route("/")
def home():
    return "Waksha AI is running!"

@app.route("/roast")
def roast():

    user_text = request.args.get("text")

    if not user_text:
        return {"error": "No text provided"}

    chat = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Roast this in funny Sinhala style: {user_text}"
            }
        ],
        model="llama3-8b-8192"
    )

    reply = chat.choices[0].message.content

    return {
        "reply": reply
    }