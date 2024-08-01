from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# Hardcoded API key
api_key = "AIzaSyBXvzVj1yjAiBeQS1VXqLfM1diYWU2b1-w"
print("API key:", api_key)

# Configure Generative AI
genai.configure(api_key=api_key)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate_text():
    prompt = request.json.get('prompt')
    try:
        response = genai.generate_text(prompt=prompt)
        print(response)
        generated_text = response.result if hasattr(response, 'result') else "No text generated"
        return jsonify({'response': generated_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
