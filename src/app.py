from flask import Flask, jsonify,request,json
app = Flask(__name__)
# import json from flask.json

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = todos
    return jsonify(json_text)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data   
    decoded_object = json.loads(request.data)
    todos.append(decoded_object)         
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    newArr = []
    print("Incoming request to delete position", position)
    for x,y in enumerate(todos):
        if x == position:
            todos.remove(todos[x])
    return jsonify(todos)

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)