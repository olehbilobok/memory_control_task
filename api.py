import datetime
from flask import request, jsonify
from models import Memory
from config import app


@app.route("/api/memory/<string:machine_id>", methods=['GET'])
def get(machine_id):

    memory = Memory.objects(id=machine_id).first()

    if not memory:
        return jsonify({'error': 'data not found'}), 404
    else:
        return jsonify(memory.to_json()), 200


@app.route("/api/memory", methods=['POST'])
def post():

    request_data = request.get_json()

    memory = Memory(
        id=request_data['id'],
        consumption=float(request_data['consumption'])
    )
    memory.save()

    return jsonify(memory.to_json()), 201


@app.route("/api/memory/<string:machine_id>", methods=['PUT'])
def put(machine_id):

    memory = Memory.objects(id=machine_id).first()

    if memory:
        request_data = request.get_json()
        memory.update(
            consumption=float(request_data['consumption']),
            updated_at=datetime.datetime.now()
        )
        return jsonify(memory.to_json()), 200

    return jsonify({'error': 'data not found'}), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
