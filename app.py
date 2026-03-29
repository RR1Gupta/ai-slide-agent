from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Slide Generator Running!"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    topic = data.get("topic")

    text = f"Title: {topic}\nDescription: This slide explains {topic} in simple terms."
    image_url = "https://via.placeholder.com/400"

    return jsonify({
        "text": text,
        "image": image_url
    })

if __name__ == "__main__":
    app.run()