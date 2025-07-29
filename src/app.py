from flask import Flask, request, jsonify

app = Flask(__name__)
tasks = []
task_id = 1

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id
    data = request.get_json()
    task = {"id": task_id, "title": data['title'], "status": data.get("status", "A Fazer")}
    tasks.append(task)
    task_id += 1
    return jsonify(task), 201

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()
    for task in tasks:
        if task['id'] == id:
            task.update(data)
            return jsonify(task)
    return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    global tasks
    tasks = [task for task in tasks if task['id'] != id]
    return jsonify({'message': 'Deleted'}), 204

if __name__ == '__main__':
    app.run(debug=True)