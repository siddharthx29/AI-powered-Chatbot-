from flask import Flask, render_template, request
from pc_ai_lib.ai_helpers import get_ai_response   # FIXED IMPORT

app = Flask(__name__)
messages = []


@app.route("/", methods=["GET", "POST"])
def home():
    global messages

    if request.method == "POST":
        user_text = request.form.get("user_input")
        if not user_text:
            return "Bad Request", 400

        messages.append({"role": "user", "content": user_text})

        ai_reply = get_ai_response(user_text)
        messages.append({"role": "assistant", "content": ai_reply})

    return render_template("index.html", messages=messages)


@app.route("/new-chat")
def new_chat():
    global messages
    messages = []
    return render_template("index.html", messages=messages)


@app.route("/pc-build-chat")
def pc_build_chat():
    return render_template("pc_build_chat.html")


@app.route("/ai-troubleshooting")
def ai_troubleshooting():
    return render_template("troubleshooting.html")   # MATCHES FILE NAME


@app.route("/gpu-advisor")
def gpu_advisor():
    return render_template("gpu.html")  # MATCHES FILE NAME


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
