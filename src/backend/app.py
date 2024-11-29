from flask import Flask, request, jsonify
from flask_cors import CORS
from model import interpret_dream

app = Flask(__name__)
CORS(app)

@app.route('/interpret-dream', methods=['POST'])
def interpret_dream_route():
    data = request.get_json()
    dream_description = data.get('dream_description', '')
    
    if not dream_description:
        return jsonify({'error': 'Dream description is required!'}), 400
    
    interpretation, details = interpret_dream(dream_description)
    
    return jsonify({
        'interpretation': interpretation,
        'details': details
    })

if __name__ == '__main__':
    app.run(debug=True)