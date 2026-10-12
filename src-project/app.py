import socket

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hostname():
    return f"Hostname: {socket.gethostname()}\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
