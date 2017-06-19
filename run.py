from flask import Flask, jsonify, request,redirect
app = Flask(__name__)

@app.route("/home", methods=["POST"])
def home():

    #pega body da requisão com application/json
    print(request.json)

    response = request.json

    #return jsonify(results=response)

    return redirect("/estorno")

@app.route("/estorno", methods=["GET","POST"])
def estorno():

    response = {
        "teste": {
            "teste": 123
        }
    }

    return jsonify(results=response)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8580, debug=False)
