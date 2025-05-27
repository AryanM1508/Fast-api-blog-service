# 📝 FastAPI Blog API

A simple and secure RESTful API built with **FastAPI** that allows users to register, log in, and perform CRUD operations on blog posts.

---

## 🚀 Features

- ✅ User Registration  
- ✅ User Login with JWT Authentication  
- ✅ Create, Read, Update, Delete Posts  
- ✅ Only post owners can edit or delete their posts  
- ✅ Search and pagination support for posts  
- ✅ Passwords are hashed before saving  
- ✅ PostgreSQL database  
- ✅ Alembic for database migrations  

---

## 📁 Folder Structure

```
project-root/
│
├── app/                # Core logic (models, DB, auth, schemas)
│   ├── main.py         # Starts the FastAPI app
│   ├── config.py       # Loads environment variables
│   ├── database.py     # Sets up database connection
│   ├── models.py       # SQLAlchemy ORM models
│   ├── oauth2.py       # JWT creation/verification
│   ├── schemas.py      # Pydantic data models
│   ├── utils.py        # Password hashing and verification
│
├── routers/            # API route handlers
│   ├── auth.py         # Handles login
│   ├── user.py         # User registration and fetching
│   ├── post.py         # CRUD operations for posts
│
├── alembic/            # Database migration tool
│   ├── env.py          # Alembic DB setup
│   └── versions/       # Migration history (auto-generated)
│
├── .env.example        # Sample environment variable setup
├── requirements.txt    # Python dependencies
├── README.md           # Project description
```

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **FastAPI**
- **SQLAlchemy**
- **PostgreSQL**
- **Alembic**
- **Pydantic**
- **passlib[bcrypt]**
- **python-jose**

---

## 🧪 Example Endpoints

| Method | Endpoint      | Description               |
|--------|---------------|---------------------------|
| POST   | `/users`      | Register a new user       |
| POST   | `/login`      | Log in and get JWT token  |
| GET    | `/posts`      | View all posts            |
| POST   | `/posts`      | Create a new post         |
| GET    | `/posts/{id}` | View a single post by ID  |
| PUT    | `/posts/{id}` | Update post (owner only)  |
| DELETE | `/posts/{id}` | Delete post (owner only)  |

---

## 🔒 Authentication

This project uses **JWT tokens** to secure protected endpoints.

After logging in, use the returned token in the `Authorization` header like this:

```
Authorization: Bearer <your_token_here>
```

---

## 🧑‍💻 How to Run Locally

> You can skip this if you're only uploading to GitHub, but here’s how to run it on your own machine:

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Set up a `.env` file:
    ```env
    DATABASE_HOSTNAME=localhost
    DATABASE_PORT=5432
    DATABASE_PASSWORD=yourpassword
    DATABASE_NAME=yourdbname
    DATABASE_USERNAME=yourdbuser
    SECRET_KEY=randomstring
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```

3. Run the app:
    ```bash
    uvicorn app.main:app --reload
    ```

---

## 📌 How to Upload to GitHub (Without Git Commands)

1. Go to [GitHub](https://github.com)  
2. Click **New Repository**  
3. Name it something like `fastapi-blog-api`  
4. **Do NOT check “Add README”**  
5. After creating it, click **“Uploading an existing file”**  
6. Drag and drop:
   - `app/`
   - `routers/`
   - `alembic/`
   - `.env.example`
   - `requirements.txt`
   - `README.md`
7. Click **Commit changes**

✅ Your project is now live on GitHub!

---

## 📬 Contact

If you have any questions or want to contribute, feel free to fork the project or open an issue.

---
