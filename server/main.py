from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
from io import BytesIO
import base64
import pytesseract
from llm import chat_completion
from json import loads
import db as dbs
from config import HOST

app = Flask(__name__)
cors = CORS(app)
db = dbs.DB()
db.create_db()

@app.route('/registration', methods=['POST'])
def registration():
    data = request.form.get('data')
    data = data if data else loads(request.data)['data']
    resp = ''
    if data:
        name = data['name']
        password = data['password']
        contraindications = data['contraindications']
        if all([name, password, contraindications]):
            resp = db.create_user(name, password, contraindications)
    if resp==True:
        return jsonify({'status': 'success', 'message': f'User created'})
    if resp:
        return jsonify({'status': 'errore', 'message': resp})


@app.route('/edit', methods=['POST'])
def edit_contraindications():
    data = request.form.get('data')
    data = data if data else loads(request.data)['data']
    resp = ''
    if data:
        name = data['name']
        password = data['password']
        contraindications = data['contraindications']
        if all([name, password, contraindications]):
            resp = db.edit_contraindications(name, password, contraindications)
    if resp==True:
        return jsonify({'status': 'success', 'message': resp})
    else:
        return jsonify({'status': 'errore', 'message': resp})

@app.route('/get', methods=['POST'])
def get_contraindications():
    data = request.form.get('data')
    data = data if data else loads(request.data)['data']
    resp = False
    if data:
        name = data['name']
        password = data['password']
        if all([name, password]):
            resp = db.get_contraindications(name, password)
    if resp:
        return jsonify({'status': 'success', 'message': resp})
    else:
        return jsonify({'status': 'errore', 'message': resp})


@app.route('/upload', methods=['POST'])
def upload_photo():
    data = request.form.get('data')
    data = data if data else loads(request.data)['data']
    if data:
        image_data = data['image']
        name = data['name']
        password = data['password']
        if all([name, password]):
            contraindications = db.get_contraindications(name, password)
            if contraindications:
                try:
                    image_bytes = base64.b64decode(image_data)
                    image = Image.open(BytesIO(image_bytes))
                    text = pytesseract.image_to_string(image, lang='rus')
                    text = chat_completion(contraindications, text)
                    return jsonify({'status': 'success', 'message': text})
                except Exception as e:
                    return jsonify({'status': 'error', 'message': str(e)})
    else:
        return jsonify({'status': 'error', 'message': 'No image data provided'})


if __name__ == '__main__':
    app.run(host=HOST, debug=False)
