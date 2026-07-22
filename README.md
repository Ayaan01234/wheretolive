# 🏙️ WhereToLive

A **FastAPI + PostgreSQL** backend that helps users compare Indian cities based on **livability** factors such as **cost of living, air quality, safety, and healthcare**. The platform also provides **AI-generated summaries and personalized city recommendations** powered by **Google Gemini**.

---

## ✨ Features

* 📍 **City Data** – Browse Indian cities with year-wise livability metrics.
* 🔐 **Authentication** – Secure JWT-based signup, login, and protected routes.
* 🏆 **Rankings** – Overall and state-wise livability rankings using weighted scoring.
* ⚖️ **City Comparison** – Compare any two cities side-by-side.
* 🤖 **AI Summary** – Generate natural-language comparisons using Gemini AI.
* 💡 **AI Recommendation** – Get personalized city suggestions based on your preferences.
* 💾 **Saved Comparisons** – Save and revisit comparisons (authenticated users).

---

## 🛠 Tech Stack

| Layer          | Technology                               |
| -------------- | ---------------------------------------- |
| Backend        | FastAPI                                  |
| Database       | PostgreSQL + SQLModel                    |
| Authentication | JWT (`python-jose`) + `passlib` (bcrypt) |
| HTTP Client    | httpx (Async)                            |
| AI             | Google Gemini API                        |
| Deployment     | Render                                   |

---

## 📂 Project Structure

```text
wheretolive/
├── app/
│   ├── main.py                  # Application entry point
│   ├── database.py              # Database engine & session
│   │
│   ├── models/                  # SQLModel database models
│   ├── schemas/                 # Request/Response schemas
│   ├── routers/                 # API routes
│   ├── services/                # Business logic
│   ├── middlewares/             # Custom middlewares
│   │
│   └── seed/
│       ├── cities_seed.csv
│       └── seed_runner.py
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 🚀 Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/wheretolive.git
cd wheretolive
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 2. Configure Environment Variables

Create a `.env` file from `.env.example` and configure it:

```env
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_PORT=5432
DB_NAME=wheretolive_db

JWT_SECRET=your-secret-key

GEMINI_API_KEY=your-gemini-api-key
```

---

## 3. Create the Database

```sql
CREATE DATABASE wheretolive_db;
```

---

## 4. Run the Application

```bash
uvicorn app.main:app --reload
```

The application will be available at:

```
http://127.0.0.1:8000
```

Interactive Swagger API documentation:

```
http://127.0.0.1:8000/docs
```

---

## 5. Seed Sample Data

```bash
python -m app.seed.seed_runner
```

---

# 📖 API Endpoints

| Method | Endpoint                  | Description                      |
| ------ | ------------------------- | -------------------------------- |
| POST   | `/auth/signup`            | Register a new user              |
| POST   | `/auth/login`             | Login and receive JWT token      |
| GET    | `/auth/profile`           | Get current user profile         |
| GET    | `/cities`                 | List all cities                  |
| GET    | `/cities/{id}`            | Get city details                 |
| GET    | `/cities/{id}/history`    | Get historical city metrics      |
| GET    | `/rankings`               | Overall livability rankings      |
| GET    | `/rankings/state/{state}` | State-wise rankings              |
| GET    | `/rankings/compare`       | Compare two cities               |
| POST   | `/ai/summary`             | AI-generated comparison summary  |
| POST   | `/ai/recommend`           | AI-generated city recommendation |
| POST   | `/comparisons`            | Save comparison                  |
| GET    | `/comparisons/mine`       | View saved comparisons           |

---

# 🤖 AI Features

### AI Summary

Generate an easy-to-read comparison between two cities using Google Gemini.

### AI Recommendation

Describe your preferences (budget, climate, safety, healthcare, etc.) and receive an AI-powered city recommendation.

---

# 🚀 Deployment

The project is deployment-ready for **Render**.

Configure:

* PostgreSQL Database
* Environment Variables
* Build Command
* Start Command

Refer to **DEPLOYMENT.md** for detailed deployment instructions.

---

# 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Ayaan Qureshi**

If you found this project helpful, consider giving it a ⭐ on GitHub.
