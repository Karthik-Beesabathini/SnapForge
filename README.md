# SnapForge
> Forge moments from every snap

A photo booth web app that captures a sequence of photos from your webcam and stitches them into a collage — built with Flask and OpenCV.

> ⚠️ **Note:** This version runs **locally only**. It requires a connected webcam and a Python environment. See the [static web version](#static-web-version) below for a deployable alternative.

---

## Tech Stack

- **Python / Flask** — backend server and routing
- **OpenCV** — webcam access and image processing
- **HTML / CSS / JavaScript** — frontend UI and collage rendering

---

## Local Setup

### Prerequisites

- Python 3.8+
- A connected webcam

### 1. Clone the repository

```bash
git clone https://github.com/Karthik-Beesabathini/SnapForge.git
cd SnapForge
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
python app.py
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

---

## Generating `requirements.txt`

If you don't have a `requirements.txt` yet, run this in your project folder with your virtual environment active:

```bash
pip freeze > requirements.txt
```

This captures all installed packages and their versions. Commit this file to the repo so others can replicate your environment exactly.

---

## Static Web Version

A fully client-side version of SnapForge is available — built with HTML, CSS, and JavaScript only, using the browser's Web Camera API. No Python or server required.

🔗 **[Live demo →](#)** https://snapforge-js.vercel.app/

---

## Contributors

| Name | Contribution |
|------|-------------|
| **Karthik** | Python backend and Flask server |
| **DGK** | Flask–frontend integration and Python refactoring |
| **Aditya** | UI/UX design in Figma, frontend implementation, and static JS version |
