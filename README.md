# Coding Challenge
November 2025

A Django boilerplate for technical interviews - clone, code, and showcase your skills

## Prerequisites

- Python 3.10 or higher
- Git
- pip and virtualenv (or your preferred virtual environment tool)

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/SyzLab/coding_challenge.git
cd coding_challenge
```

### 2. Create a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Install fixtures

```bash
python manage.py loaddata fixtures/users.json
```

### 6. Start the Development Server

```bash
python manage.py runserver
# Visit http://127.0.0.1:8000/ to see the app running!
```

### 7. Log in

You can use any user from the fixtures e.g. `syzlab`. Their passwords are all `djangoforlife`.
