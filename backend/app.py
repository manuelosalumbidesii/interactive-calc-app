from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculate")
def calculate():
    num1 = request.args.get("num1", type=int)
    num2 = request.args.get("num2", type=int)
    result = num1 + num2
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
