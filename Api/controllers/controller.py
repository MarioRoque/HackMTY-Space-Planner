from flask import request, make_response, jsonify


def generate_space():
	info = request.get_json()

	if info["version"] == "V2":
		capacity = info["capacity"]
		threshold = info["threshold"]
		room_polygon = info["room"]

	#Logic of points generation

	return make_response("Job started"), 200