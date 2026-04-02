# 🚀 AI Resume Analyzer

An intelligent web application built using **Flask** that analyzes resumes (PDF format), extracts skills, and provides a score with visual representation.

---

## 📌 Features

- 📄 Upload Resume (PDF)
- 🧠 Extracts text from resume
- 🔍 Identifies key skills
- 📊 Calculates resume score
- 🥧 Displays results using Pie Chart
- 💻 Simple and clean UI

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS
- **Backend:** Python (Flask)
- **Libraries Used:**
  - Flask
  - PyPDF2
  - OS module

---

## 📁 Project Structure

```
ai-resume-analyzer/
│
├── app.py
├── templates/
│   └── index.html
├── utils/
│   ├── analyzer.py
│   └── parser.py
```

---

## ⚙️ How It Works

1. User uploads a resume (PDF)
2. Flask backend receives the file
3. Text is extracted from PDF
4. Skills are identified from text
5. Score is calculated based on skills
6. Results are displayed with chart

---

## ▶️ How to Run Locally

### Step 1: Clone Repository
```
git clone https://github.com/YOUR-USERNAME/ai-resume-analyzer.git
cd ai-resume-analyzer
```

### Step 2: Install Dependencies
```
pip install flask PyPDF2
```

### Step 3: Run Application
```
python app.py
```

### Step 4: Open Browser
```
http://127.0.0.1:5000/
```

---

## 📸 Output Screenshot
Run locally:
http://127.0.0.1:5000/
![AI Resume Analyzer](https://raw.githubusercontent.com/srushthis21/ai-resume-analyzer/main/Screenshot 2026-04-02-20201328.png)
---

## 💡 Future Improvements

- Add job-role based analysis
- Improve UI/UX
- Add AI-based recommendations
- Deploy online

## ⭐ If you like this project, give it a star!
