from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/moveo/joke", methods=["POST"])
def moveo_joke():
    try:
        r = requests.get(
            "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
        )
        joke = r.json()

        if joke["type"] == "single":
            message_text = joke["joke"]
        else:
            message_text = f"{joke['setup']}\n\n{joke['delivery']}"

        # Moveo-compatible response with text
        return jsonify({
            "responses": [
                {
                    "type": "text",
                    "text": message_text
                }
            ],
            "context": {}
        })

    except Exception as e:
        return jsonify({
            "responses": [
                {
                    "type": "text",
                    "text": "😅 Something went wrong while getting the joke."
                }
            ],
            "context": {}
        })

if __name__ == "__main__":
    app.run(port=3000)
