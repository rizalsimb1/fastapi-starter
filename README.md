# fastapi-starter

![Node](https://img.shields.io/badge/node-20+-green.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Stars](https://img.shields.io/github/stars/rizalsimb1/fastapi-starter?style=social)

> A modern REST API built with FastAPI, SQLAlchemy 2.0, and PostgreSQL. Includes JWT authentication, rate limiting, background tasks, and Docker deployment.

## ✨ Features

- ✅ JWT authentication with refresh tokens
- ✅ SQLAlchemy 2.0 async ORM with PostgreSQL
- ✅ Pydantic v2 request/response validation
- ✅ Redis-based rate limiting and caching
- ✅ Background task queue with Celery
- ✅ Auto-generated OpenAPI/Swagger documentation
- ✅ Docker + docker-compose for one-command setup
- ✅ Comprehensive test suite with pytest-asyncio

## 🛠️ Tech Stack

`Python 3.11+` • `FastAPI` • `SQLAlchemy 2.0` • `PostgreSQL` • `Redis` • `Docker` • `Pydantic v2`

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/rizalsimb1/fastapi-starter.git
cd fastapi-starter

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Quick Start

```python
# Start the API
docker-compose up -d

# Or run locally
uvicorn app.main:app --reload --port 8000

# API docs at http://localhost:8000/docs

```

## 📁 Project Structure

```
fastapi-starter/
├── src/
│   └── main files
├── tests/
│   └── test files
├── requirements.txt
├── README.md
└── LICENSE
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'feat: add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<p align="center">Made with ❤️ by <a href="https://github.com/rizalsimb1">rizalsimb1</a></p>

