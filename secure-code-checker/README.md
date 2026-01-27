# Secure Code Checker

An AI-powered secure code analysis tool that detects vulnerabilities
and rewrites insecure code using secure coding practices.

## Features
- Detects SQL Injection, XSS, Command Injection, RCE, etc.
- Secure code rewriting using Gemini API
- Strict input validation: only code is accepted
- FastAPI backend with HTML/CSS/JS frontend

## Tech Stack
- Backend: FastAPI (Python)
- Frontend: HTML, CSS, JavaScript
- AI Model: Google Gemini
- Server: Uvicorn

## Installation
1. Clone the repo
```bash
git clone https://github.com/cyber-abhi01/Project.git
cd Project/secure-code-checker
Install dependencies

pip install -r requirements.txt
Copy .env.example to .env and add your API key

cp .env.example .env
Run server

python -m uvicorn app:app --reload
Open browser at http://127.0.0.1:8000