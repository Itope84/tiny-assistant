# We create a server to serve as a backup trigger for the assistant in noisy environments where the trigger is unreliable. We can create a mobile app that sends a request to this server to trigger the assistant.


from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/trigger", methods=["POST"])
def trigger_assistant():
    # TODO: Implement trigger logic here
    # TODO: require authentication for this endpoint as it is a security risk if an attacker were to gain access to the home network
    return jsonify({"status": "success"})


if __name__ == "__main__":
    # Listen on all public IPs on the network
    app.run(host="0.0.0.0", port=5000, debug=True)
