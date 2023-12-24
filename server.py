# We create a server to serve as a backup trigger for the assistant in noisy environments where the trigger is unreliable. We can create a mobile app that sends a request to this server to trigger the assistant.


from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/trigger", methods=["GET", "POST"])
def trigger_assistant():
    # TODO: Implement trigger logic here
    return jsonify({"status": "success"})


if __name__ == "__main__":
    app.run(debug=True)
