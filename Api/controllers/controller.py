from flask import request, make_response, jsonify
from .PathPlanning import Spacer

def generate_space():
	info = request.get_json()
	return Spacer.main(info)