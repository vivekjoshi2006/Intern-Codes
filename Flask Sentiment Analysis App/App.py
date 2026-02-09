from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    data = {"text": "", "sentiment": None, "polarity": None, "subjectivity": None, "color": "neutral"}

    if request.method == "POST":
        text = request.form["text"]
        s = TextBlob(text).sentiment

        data["text"] = text
        data["polarity"] = round(s.polarity, 3)
        data["subjectivity"] = round(s.subjectivity, 3)

        if s.polarity > 0:
            data["sentiment"] = "Positive 😊"
            data["color"] = "pos"
        elif s.polarity < 0:
            data["sentiment"] = "Negative 😡"
            data["color"] = "neg"
        else:
            data["sentiment"] = "Neutral 😐"
            data["color"] = "neutral"

    return render_template("index.html", **data)

if __name__ == "__main__":
    app.run(debug=True)