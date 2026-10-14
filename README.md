TaskFlow Backend

A project management API (mini Jira/Trello) built with FastAPI and SQLAlchemy.

## Features
- Users, Projects, Tasks with relationships
- Input validation with Pydantic
- Organized routers

## Run locally
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

API docs: http://localhost:8000/docs
