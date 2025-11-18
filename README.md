# Coding Challenge
November 2025

A Django boilerplate for technical interviews - clone, code, and showcase your skills

## Prerequisites

- Python 3.10 or higher
- Git
- pip and virtualenv (or your preferred virtual environment tool)

## Quick Start

### 1. Make a Fork of the Repository

Go to `https://github.com/SyzLab/coding_challenge` and select the Fork option.

### 2. Clone the Repository

```bash
git clone https://github.com/<your-username>/coding_challenge.git
cd coding_challenge
```

### 3. Create a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Install fixtures

```bash
python manage.py loaddata fixtures/users.json
```

### 7. Start the Development Server

```bash
python manage.py runserver
# Visit http://127.0.0.1:8000/ to see the app running!
```

### 8. Log in

You can use any user from the fixtures e.g. `syzlab`. Their passwords are all `djangoforlife`.
