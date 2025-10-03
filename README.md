# 📦 Django + Docker Project

This is a Django project containerized with **Docker** and **PostgreSQL**.

---

## 🚀 Features
- Django backend
- PostgreSQL database
- Docker Compose for easy setup
- Hot reload in development (`runserver` + volume mounts)
- Persistent PostgreSQL data (via Docker volume)

---

## 🛠️ Setup

### 1. Clone repo & install Docker
Make sure you have **Docker** and **docker-compose** installed.

### 2. Build containers
```bash
docker-compose up --build

This will:

    Build the Django web container

    Start the PostgreSQL db container

3. Run migrations

Inside the running container:

docker-compose exec web python manage.py migrate

4. Create superuser (optional)

docker-compose exec web python manage.py createsuperuser

📂 Project Structure

.
├── API/                # Django project code
├── Dockerfile          # Docker build instructions
├── docker-compose.yml  # Docker Compose services
├── requirements.txt    # Python dependencies
├── manage.py
└── README.md

🔧 Useful Commands

    Rebuild containers

docker-compose up --build

Run migrations

docker-compose exec web python manage.py migrate

Create superuser

docker-compose exec web python manage.py createsuperuser

Open Django shell

docker-compose exec web python manage.py shell

Stop containers

    docker-compose down

🌍 Access

    Django: http://127.0.0.1:8000

Admin Panel: http://127.0.0.1:8000/admin
🗄️ Database

The PostgreSQL database runs inside Docker.
Default values (change in docker-compose.yml or .env):

    DB name: mydb

    User: myuser

    Password: mypassword

    Host: db (inside containers)


## 📊 API Endpoints

### 1. Employee Statistics (single employee)
**GET** `/statistics/employee/{id}/?month={month}&year={year}`  
Returns:
- Full name of employee
- Number of clients
- Number of products sold
- Total sales amount

---

### 2. Employee Statistics (all employees)
**GET** `/employee/statistics/?month={month}&year={year}`  
Returns a list of employees with:
- Employee ID
- Full name
- Number of clients
- Number of products sold
- Total sales amount

---

### 3. Client Statistics
**GET** `/statistics/client/{id}/?month={month}&year={year}`  
Returns:
- Client ID
- Full name
- Number of purchased products
- Total purchase amount
