# Python 
FROM python:3.13-slim

# venv
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /API


RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /API/
RUN pip install --no-cache-dir -r requirements.txt


COPY . /API/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
