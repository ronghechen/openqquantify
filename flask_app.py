#!/usr/bin/env python3
import os
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from openai import OpenAI

load_dotenv()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)  # bind db to app

class QuestionAnswer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    saved = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f"<QnA {self.id}>"

client = OpenAI()

@app.route("/")
def index():
    return render_template("index.html", response=None, question="")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("question", "").strip()
    save = request.form.get("save") == "on"  # opt-in checkbox

    try:
        completion = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert in international medical regulation "
                        "and data compliance (HIPAA, GDPR, MDR, etc.). "
                        "Answer clearly and cite sources where possible."
                    ),
                },
                {"role": "user", "content": question},
            ],
            temperature=0.3,
        )
        answer = completion.choices[0].message.content
    except Exception as e:
        answer = f"Error: {str(e)}"

    if save and question and not answer.startswith("Error:"):
        row = QuestionAnswer(question=question, answer=answer, saved=True)
        db.session.add(row)
        db.session.commit()

    return render_template("index.html", response=answer, question=question)

@app.route("/history")
def history():
    rows = (
        QuestionAnswer.query.filter_by(saved=True)
        .order_by(QuestionAnswer.created_at.desc())
        .limit(50)
        .all()
    )
    return render_template("history.html", rows=rows)

@app.route("/healthz")
def healthz():
    return {"status": "ok"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    debug = bool(int(os.getenv("DEBUG", "0")))
    app.run(host="0.0.0.0", port=port, debug=debug)
