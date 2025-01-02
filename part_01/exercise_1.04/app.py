from flask import Flask, request, jsonify

app = Flask(__name__)

todos = [
    {"id": 1, "task": "Clean the house", "done": False},
    {"id": 2, "task": "Buy groceries", "done": False}
]

@app.route('/')
def home():
    return "Server started on port 5000"

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

@app.route('/todos/<int:id>', methods=['GET'])
def get_todo_by_id(id):
    todo = next((todo for todo in todos if todo["id"] == id), None)
    if todo:
        return jsonify(todo), 200
    return jsonify({"message": "Todo not found"}), 404

@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    if 'task' not in data:
        return jsonify({"message": "Task is required"}), 400
    new_todo = {
        "id": len(todos) + 1,
        "task": data["task"],
        "done": False
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201

@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    todo = next((todo for todo in todos if todo["id"] == id), None)
    if not todo:
        return jsonify({"message": "Todo not found"}), 404

    data = request.get_json()
    if "task" in data:
        todo["task"] = data["task"]
    if "done" in data:
        todo["done"] = data["done"]

    return jsonify(todo), 200

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    global todos
    todos = [todo for todo in todos if todo["id"] != id]
    return jsonify({"message": "Todo deleted"}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)