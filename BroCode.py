from flask import Flask, request, jsonify

app = Flask(__name__)

# Bro Code Password
BRO_PASSWORD = "A BRO IS NO BRO WITHOUT A BRO"

CHARSET_SIZE = 95  # Printable ASCII characters (32 to 126)

# Function to encode text
def encode(text, key):
    result = ""
    for char in text:
        if 32 <= ord(char) <= 126:
            result += chr(32 + (ord(char) - 32 + key) % CHARSET_SIZE)
        else:
            result += char
    return result

# Function to decode text
def decode(text, key):
    result = ""
    for char in text:
        if 32 <= ord(char) <= 126:
            result += chr(32 + (ord(char) - 32 - key + CHARSET_SIZE) % CHARSET_SIZE)
        else:
            result += char
    return result

@app.route('/')
def home():
    return "Welcome to the Bro Zone API!"

@app.route('/bro', methods=['POST'])
def bro_code():
    data = request.get_json()
    
    # Password check
    password = data.get("password", "")
    if password != BRO_PASSWORD:
        return jsonify({"message": "Access Denied. Wrong Password!"}), 403
    
    # Operation choice
    operation = data.get("operation", "")
    text = data.get("text", "")
    key = data.get("key", 0)
    
    if operation == "encode":
        result = encode(text, int(key))
        return jsonify({"message": "Success", "operation": "encode", "result": result})
    elif operation == "decode":
        result = decode(text, int(key))
        return jsonify({"message": "Success", "operation": "decode", "result": result})
    else:
        return jsonify({"message": "Invalid operation!"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
