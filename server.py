# Name: Jeremy Pogue
# Link to GitHub Repo: https://github.com/USC-EE-250L-Spring-2023/lab-10-jeremy-lab10

from flask import Flask, request, jsonify

from main import process1, process2


app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Welcome'})

# TODO: Create a flask app with two routes, one for each function.
# The route should get the data from the request, call the function, and return the result.
@app.route('/process1', methods=['POST'])
def get_process1():
    data = request.get_json()
    processed = process1(data["data"])
    return jsonify(processed)

@app.route('/process2', methods=['POST'])
def get_process2():
    data = request.get_json()
    processed = process2(data["data"])
    return jsonify(processed)

if __name__ == "__main__":
    app.run(host='localhost', port=5001)