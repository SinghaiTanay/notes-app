# Notes App

Notes App is a FastAPI service for managing notes, backed by PostgreSQL. It includes a health route and a database connectivity check.

## Tech Stack

- Python 3.14+
- FastAPI
- Uvicorn
- SQLAlchemy
- Psycopg
- Pydantic Settings
- PostgreSQL
- Alembic
- uv

## Project Structure

```text
app/
  main.py          # FastAPI application and route registration
  api/             # API routers
  core/            # Application configuration
  db/              # Database engine and session management
  models/          # SQLAlchemy models
  schemas/         # Pydantic schemas
  services/        # Application service logic
```

## Prerequisites

- Python 3.14 or newer
- [uv](https://docs.astral.sh/uv/)
- A running PostgreSQL database

## Installation

1. Clone the repository and enter the project directory:

   ```powershell
   git clone https://github.com/SinghaiTanay/notes-app.git
   cd notes-app
   ```

2. Install the dependencies:

   ```powershell
   uv sync
   ```

3. Create a local environment file:

   ```powershell
   Copy-Item .env.example .env
   ```

4. Update `DATABASE_URL` in `.env` with your PostgreSQL credentials:

   ```dotenv
   DATABASE_URL=postgresql+psycopg://postgres:your_password@localhost:5432/your_database
   ```

The URL format is:

```text
postgresql+psycopg://<username>:<password>@<host>:<port>/<database>
```

## Running the Application

Start the development server with automatic reload:

```powershell
uv run uvicorn app.main:app --reload
```

The API will be available at:

- API: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | Confirms that the API is running |
| `GET` | `/health/db` | Checks the PostgreSQL database connection |

Example:

```powershell
Invoke-RestMethod http://127.0.0.1:8000/
Invoke-RestMethod http://127.0.0.1:8000/health/db
```

A healthy database response has the following shape:

```json
{
  "status": "OK",
  "database": "Connected successfully"
}
```