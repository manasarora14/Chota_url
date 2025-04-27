from flask import Flask, request, jsonify, redirect
import random
import string

app = Flask(__name__)

# Dictionary to store mapping of short codes to long URLs
url_mapping = {}

def generate_short_code(length=5):
    # Generates a random string of letters and digits
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choices(characters, k=length))
    return short_code

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    long_url = data.get('long_url')

    # Generate a unique short code
    short_code = generate_short_code()

    # Save the mapping
    url_mapping[short_code] = long_url

    short_url = f"http://localhost:5000/{short_code}"
    return jsonify({'short_url': short_url})

@app.route('/<short_code>')
def redirect_to_long_url(short_code):
    long_url = url_mapping.get(short_code)
    if long_url:
        return redirect(long_url)
    else:
        return "Invalid short URL", 404

if __name__ == "__main__":
    app.run(debug=True)
