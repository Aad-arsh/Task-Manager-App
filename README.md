# Task Manager App (Flask + SQLite)

A resume-ready full-stack **Task Manager** application with:
- User Registration & Login (Flask-Login + hashed passwords)
- CRUD for Tasks and Categories
- Task fields: title, description, priority, due date, status, category
- Filter & search on tasks
- REST API for tasks (JWT-less, cookie session protected for simplicity)
- Bootstrap-based UI

---

## Tech Stack
- Python 3.9+
- Flask, SQLAlchemy, Flask-Login, Flask-WTF, Flask-Bcrypt
- SQLite (development)
- HTML + Bootstrap

---

## Project Structure
```
task_manager_app/
├─ task_manager/
│  ├─ __init__.py
│  ├─ extensions.py
│  ├─ models.py
│  ├─ auth.py
│  ├─ tasks.py
│  ├─ api.py
│  ├─ templates/
│  │  ├─ base.html
│  │  ├─ index.html
│  │  ├─ login.html
│  │  ├─ register.html
│  │  ├─ tasks.html
│  │  └─ task_form.html
│  └─ static/
│     └─ css/style.css
├─ scripts/
│  └─ seed.py
├─ tests/
│  └─ test_basic.py
├─ .env.example
├─ requirements.txt
└─ run.py
```

---

## Quickstart (Dev)

1) Create & activate a virtualenv
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

2) Install deps
```bash
pip install -r requirements.txt
```

3) Configure env (optional)
- Copy `.env.example` to `.env` and adjust if needed.
- Defaults will work out of the box with SQLite.

4) Run
```bash
python run.py
```
- App will start at http://127.0.0.1:5000

5) Seed some sample data (optional)
```bash
python scripts/seed.py
```

---

## Features

### Authentication
- Register, Login, Logout
- Passwords hashed with bcrypt

### Tasks
- Create, Read, Update, Delete
- Priority: Low, Medium, High
- Status: Pending, In Progress, Done
- Due Date (optional)
- Category (optional)
- Search by title/description, filter by status/priority/category

### REST API (cookie session auth)
- `GET /api/tasks` — list current user's tasks (+ filters via query params)
- `POST /api/tasks` — create task (JSON body)
- `GET /api/tasks/<id>` — get one
- `PUT /api/tasks/<id>` — update
- `DELETE /api/tasks/<id>` — delete

Send/receive JSON. Must be logged-in via browser session cookies.

---

## Testing
```bash
pytest -q
```

---

## Deploy Notes (Heroku-like or Render)
- Set `FLASK_SECRET_KEY` to a strong random string.
- For production, use Postgres and configure database URI via `DATABASE_URL` env var.
- Serve with gunicorn or uwsgi behind a reverse proxy.
