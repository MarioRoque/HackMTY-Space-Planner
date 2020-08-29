from .controllers import controller
from flask import Flask, request

app = Flask(__name__)

@app.route('/status')
def ping_status():
    print("OK")
    return "OK"

@app.route('/generate', methods=['POST'])
def legacy():
    response = controller.generate_space()
    return response
