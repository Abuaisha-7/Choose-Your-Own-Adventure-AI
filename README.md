# Choose-Your-Own-Adventure-AI ✅

A small full-stack project that generates interactive choose-your-own-adventure stories using a FastAPI backend and a React (Vite) frontend. This repository includes a simple job-based API to generate stories, persist them in a database, and fetch the completed story tree for playback in the frontend.

---

## Quickstart 🚀

Prerequisites:

- Python 3.13+ (backend) and Node.js 18+ / npm (frontend)
- An OpenAI API key (optional but required for story generation using OpenAI)

Backend (development):

1. Create a virtual environment and activate it:

   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate  # Windows
   source .venv/bin/activate   # macOS / Linux
   ```

2. Install dependencies:

   ```bash
   pip install -r backend/requirements.txt
   ```

3. Copy `backend/example.env` to `.env` and set your secrets (e.g. `OPENAI_API_KEY`, `GROQ_API_KEY`):

   ```bash
   cp backend/example.env backend/.env
   ```

4. Run the API server:

   ```bash
   cd backend
   uvicorn main:app --reload --port 8000
   ```

Frontend (development):

1. Install dependencies and run dev server:

   ```bash
   cd frontend
   npm install
   npm run dev
   ```

2. Open the app in your browser (defaults to http://localhost:5173).

---

## API Summary 🔧

Base URL: `http://localhost:8000` (when running locally)

- POST /api/stories/create

  - Create a story generation job. Set cookie `session_id` so multiple requests can be tied to the same session.
  - Request body: `{ "theme": "your story theme" }`
  - Returns: job metadata with `job_id` and status (`pending`/`processing`/`completed`/`failed`).

- GET /api/jobs/{job_id}

  - Check status of a job by `job_id`.

- GET /api/stories/{story_id}/complete
  - Retrieve the full story tree (nodes and options) for playback in the frontend.

Documentation: FastAPI interactive docs are available at `/docs` (Swagger) and `/redoc`.

---

## Project Structure 📂

- `backend/` - FastAPI application and database models.

  - `main.py` - application entry point.
  - `core/` - configuration, prompts, and generator logic.
  - `routers/` - API routes for jobs and stories.
  - `db/` - database init and helper utilities.

- `frontend/` - React (Vite) SPA that communicates with the backend.
  - `src/components` - UI components for generating and playing stories.

---

## Environment Variables & Keys 🔐

- `OPENAI_API_KEY` - required if using OpenAI for story generation.
- `GROQ_API_KEY` - used when Groq provider is configured.
- `DATABASE_URL` - default is SQLite (see `backend/example.env`).
- `API_PREFIX` - route prefix for API (default `/api`).

Always keep API keys private and do not commit them to source control.

---

## Development Notes & Tips 💡

- The backend is configured to create database tables on startup (`create_tables()`), pointing at the `DATABASE_URL`.
- Story generation runs as a background task and is persisted using SQLAlchemy models.
- If you change models, drop or migrate the DB as needed during development.

---

## Contributing & License 🤝

Contributions are welcome. Feel free to open issues or submit pull requests. Add tests and update documentation when adding features.

_This project does not include a license file by default — add a `LICENSE` (for example MIT) if you intend to open-source it._


