from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- Home Route (show HTML) ---
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Form values read karenge
        access_token = request.form.get("accessToken")
        thread_id = request.form.get("threadId")
        hater_name = request.form.get("kidx")
        time = request.form.get("time")
        msg_file = request.files.get("msgFile")

        # File ka content read karna (agar diya gaya ho)
        messages = None
        if msg_file:
            messages = msg_file.read().decode("utf-8").splitlines()

        # Filhaal simple response bhej dete hain
        return f"""
        <h2>✅ Form Submitted</h2>
        <p><b>Token:</b> {access_token}</p>
        <p><b>Thread ID:</b> {thread_id}</p>
        <p><b>Hater Name:</b> {hater_name}</p>
        <p><b>Speed:</b> {time} seconds</p>
        <p><b>Messages File Lines:</b> {len(messages) if messages else 0}</p>
        <a href="/">🔙 Go Back</a>
        """

    return render_template("index.html")


# --- Stop Route ---
@app.route("/stop")
def stop():
    return "<h2>🚫 Bot STOPPED!</h2><a href='/'>🔙 Go Back</a>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)