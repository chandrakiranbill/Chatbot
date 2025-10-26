# Chatbot — Django + ChatterBot (Python 3.13.9, Windows)


---

## Prerequisites

- **Windows 10/11**
- **Python 3.13.9** installed and added to PATH 
- **VS Code** with the Python extension

---



## Quick Start (VS Code, PowerShell)

> Open **VS Code** → **File → Open Folder…** → Chatbot.

1) **Creating and activating virtual environment**
```powershell
cd "C:\path\to\chatbot"
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
```
> If there is any script policy error, run  this once to bypass the error:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

2) **Installing dependencies**
```powershell
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

3) **Installing spaCy English model which will be required by ChatterBot**
```powershell
python -m pip install spacy
python -m spacy download en_core_web_sm
```

4) **Installing the  YAML support for the corpus**
```powershell
pip install pyyaml
```

5) **Initializing Django DB and train the bot this is for the first time only**
```powershell
python manage.py migrate
python manage.py chatbot_tty --reset
```

6) **Steps by step Commands to Execute the chatbot**
```bat
cd C:\path\to\termbot
py -3.13 -m venv .venv
.\.venv\Scripts\activate

python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
python -m pip install spacy
python -m spacy download en_core_web_sm
pip install pyyaml

python manage.py migrate
python manage.py chatbot_tty --reset
```

---

