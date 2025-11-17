# Interview Quest
November of 2025

A Django boilerplate for technical interviews - clone, code, and showcase your skills

## Prerequisites

- Python 3.10 or higher
- Git
- pip and virtualenv (or your preferred virtual environment tool)

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/SyzLab/interview-quest.git
cd interview-quest
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

### 4. Set Up Environment Variables

```bash
# Copy the example environment file
cp .env.example .env
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Start the Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to see the app running!
