from flask import jsonify, Blueprint, request
from app.problemmanager import ProblemManager
import random
import json

api = Blueprint("api", __name__, url_prefix="/api")

pmanager = ProblemManager()


def problem_dict(problem_id, probelm):
    return {
        "problem_id": problem_id,
        "locations": probelm.locations,
        "distance_matrix": probelm.distance_matrix,
        "solution": probelm.solution
    }


@api.route("/create_problems", methods=["POST"])
def create_random_problems():
    request_data = json.loads(request.data)
    if request_data.get("location_list"):
        location_list = request_data.get("location_list")
    else:
        location_list = []

    if not location_list:
        for _ in range(random.randint(2, 10)):
            location_list.append((random.randint(1, 400), random.randint(1, 400)))

    problem_id, probelm = pmanager.create_problem(location_list)

    return jsonify(problem_dict(problem_id, probelm)), 200


@api.route("/subscribe", methods=["GET"])
def subscribe():
    problem_id, probelm = pmanager.subscribe()
    if problem_id == 0:
        return jsonify({"error": probelm}), 200
    return jsonify(problem_dict(problem_id, probelm)), 200


@api.route("/publish", methods=["POST"])
def publish():
    request_data = json.loads(request.data)
    if request_data.get("problem_id"):
        problem_id, probelm = pmanager.publish(request_data.get('problem_id'), request_data.get('num_vehicles', 1))
        if problem_id == 0:
            return jsonify({"error": probelm}), 400
        return jsonify(problem_dict(problem_id, probelm)), 200
    else:
        return jsonify({"message": "error"}), 200
