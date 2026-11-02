from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


# Encrypts letters by shifting them while leaving other characters unchanged.
def encrypt(message, key):
    encrypted_message = ""

    for character in message:
        if "A" <= character <= "Z":
            # ord() turns letters into numbers, chr() turns them back, and % 26 wraps within 26 letters.
            shifted_character = chr((ord(character) - ord("A") + key) % 26 + ord("A"))
            encrypted_message = encrypted_message + shifted_character
        elif "a" <= character <= "z":
            shifted_character = chr((ord(character) - ord("a") + key) % 26 + ord("a"))
            encrypted_message = encrypted_message + shifted_character
        else:
            encrypted_message = encrypted_message + character

    return encrypted_message


# Decrypts a message by reversing its shift with encrypt().
def decrypt(message, key):
    return encrypt(message, -key)


# Displays the page with the cipher form.
@app.route("/")1
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "Send a JSON object with a message and key."}), 400

    message = data.get("message")
    key = data.get("key")

    if not isinstance(message, str) or message.strip() == "":
        return jsonify({"error": "Message cannot be empty."}), 400
    if not isinstance(key, int) or isinstance(key, bool) or key < 1 or key > 25:
        return jsonify({"error": "Key must be a whole number from 1 to 25."}), 400

    return jsonify({"result": encrypt(message, key)})


# Validates the submitted message and key, then returns the decrypted text.
@app.route("/decrypt", methods=["POST"])
def decrypt_route():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "Send a JSON object with a message and key."}), 400

    message = data.get("message")
    key = data.get("key")

    if not isinstance(message, str) or message.strip() == "":
        return jsonify({"error": "Message cannot be empty."}), 400
    if not isinstance(key, int) or isinstance(key, bool) or key < 1 or key > 25:
        return jsonify({"error": "Key must be a whole number from 1 to 25."}), 400

    return jsonify({"result": decrypt(message, key)})


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
