from flask import Flask, render_template
from flask_socketio import SocketIO
import subprocess, os

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on("command")
def handle_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        output = e.output
    socketio.emit("output", output)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render tự cấp port
    socketio.run(app, host="0.0.0.0", port=port)
