from flask import Flask, render_template, request


app = Flask(__name__)


def get_length(text):
    btext = text.encode()
    num_new_lines = btext.count(b"\n")
    text_len = len(btext) + num_new_lines
    return (str(text_len), f"{text_len:x}")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/calc-length", methods=["POST"])
def calc_length():
    data = request.json
    cl, te = get_length(data["content"])
    return {"content-length": cl, "transfer-encoding": te}
