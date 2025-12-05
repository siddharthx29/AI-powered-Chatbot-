from flask import Flask, render_template, request
from pc_ai_lib.ai_helpers import get_ai_response

app = Flask(__name__)

# ---------------- HOME (PC BUILD CHAT) ----------------
@app.route("/", methods=["GET", "POST"])
def home():
    answer = None
    query = None

    if request.method == "POST":
        query = request.form["query"]
        answer = get_ai_response(query)

    return render_template(
        "index.html",
        title="PC Build Assistant",
        header_title="💻 PC Build AI Assistant",
        header_sub="Ask anything about builds, compatibility, upgrades & more.",
        answer=answer,
        query=query
    )

# ---------------- NEW CHAT PAGE ----------------
@app.route("/new")
def new_chat():
    return render_template(
        "index.html",
        title="New Chat",
        header_title="💬 New Chat",
        header_sub="Start a fresh conversation.",
        answer=None,
        query=None
    )

# ---------------- TROUBLESHOOT PAGE ----------------
@app.route("/troubleshoot", methods=["GET", "POST"])
def troubleshoot():
    answer = None
    query = None

    if request.method == "POST":
        query = request.form["query"]
        answer = get_ai_response("Troubleshoot this issue: " + query)

    return render_template(
        "troubleshooting.html",
        title="Troubleshooting",
        header_title="🛠 Troubleshooting AI",
        header_sub="Fix crashes, lag, overheating, errors, BSOD & more.",
        answer=answer,
        query=query
    )

# ---------------- GPU PAGE ----------------
@app.route("/gpu", methods=["GET", "POST"])
def gpu():
    answer = None
    query = None

    if request.method == "POST":
        query = request.form["query"]
        answer = get_ai_response("GPU advice: " + query)

    return render_template(
        "gpu.html",
        title="GPU Advisor",
        header_title="🎮 GPU Advisor",
        header_sub="Ask about GPUs, bottlenecks, performance & gaming.",
        answer=answer,
        query=query
    )

# ---------------- ABOUT PAGE ----------------
@app.route("/about")
def about():
    return render_template(
        "about.html",
        title="About AI",
        header_title="ℹ️ About this AI Assistant",
        header_sub="Learn more about how this AI works."
    )

if __name__ == "__main__":
    app.run(debug=True)
