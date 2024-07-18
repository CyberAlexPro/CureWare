from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

#Clé API
openai.api_key = 'clé api'

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')

    response = openai.Completion.create(
        model="CureWare",
        prompt=question,
        max_tokens=150
    )

    return jsonify(response.choices[0].text.strip())

if __name__ == '__main__':
    app.run(debug=True)
