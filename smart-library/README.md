📚 Flask Library Management System

A simple Library Management Web App built using Flask, SQLite, Docker, and the Open Library API.

Users can:

- Search books online
- Save books to local database
- View saved books
- Delete saved books

---

🚀 Features

- 🔍 Search books using Open Library API
- 💾 Save books into SQLite database
- 📖 View saved books
- ❌ Delete saved books
- 🐳 Docker support
- ⚙️ GitHub Actions CI/CD workflow

---

🛠 Tech Stack

- Python
- Flask
- SQLite
- HTML / CSS / JavaScript
- Docker
- GitHub Actions

---

📂 Project Structure

project/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── library.db
│
├── templates/
│   ├── index.html
│   └── saved.html
│
├── static/
│
└── .github/
    └── workflows/
        └── docker-build.yml

---

⚡ Installation

1. Clone Repository

git clone https://github.com/your-username/library-management.git
cd library-management

---

2. Create Virtual Environment

python -m venv venv

Activate environment:

Windows

venv\Scripts\activate

Linux / Mac

source venv/bin/activate

---

3. Install Dependencies

pip install -r requirements.txt

---

▶️ Run Application

python app.py

Server runs on:

http://127.0.0.1:5000

---

🐳 Docker Setup

Build Docker Image

docker build -t flask-library .

Run Container

docker run -p 5000:5000 flask-library

---

⚙️ GitHub Actions

This project includes CI/CD workflow:

.github/workflows/docker-build.yml

Whenever code is pushed to "main" branch:

- Docker image is automatically built
- Image is pushed to GitHub Container Registry

---

📡 API Routes

Method| Route| Description
GET| "/"| Home Page
GET| "/search?q=book"| Search Books
POST| "/save"| Save Book
GET| "/saved"| View Saved Books
DELETE| "/delete/<id>"| Delete Book

---

📚 Open Library API

This project uses:

https://openlibrary.org/developers/api

For fetching book data and covers.

---

🔮 Future Improvements

- User authentication
- Book categories
- Pagination
- Redis caching
- PostgreSQL migration
- REST API versioning
- Async requests
- Rate limiting
- Admin dashboard

---

🧠 Learning Goals

This project helps understand:

- Flask routing
- REST APIs
- Database CRUD operations
- Docker containerization
- CI/CD pipelines
- Backend architecture basics

---

📜 License

MIT License