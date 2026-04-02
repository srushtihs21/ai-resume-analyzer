from flask import Flask, render_template, request
import os
from utils.analyzer import extract_skills
from utils.parser import extract_text

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    return render_template("index.html", skills=[], score=0)


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('resume')

    if file:
        os.makedirs("uploads", exist_ok=True)

        path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(path)

        text = extract_text(path)
        skills = extract_skills(text)

        # score logic
        score = len(skills) * 10
        if score > 100:
            score = 100

        return render_template("index.html", skills=skills, score=score)

    return render_template("index.html", skills=[], score=0)


if __name__ == "__main__":
    app.run(debug=True)