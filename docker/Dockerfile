FROM python:3.9-slim-buster

# Установка зависимостей
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Копирование файлов
COPY . .

# Запуск
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
