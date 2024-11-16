FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Создаем пользователя
RUN adduser --disabled-password app

# Копируем содержимое проекта в контейнер
COPY . /app

# Устанавливаем права для папки data (если она существует)
RUN chmod -R 777 /app/data

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Задаем пользователя и окружение
USER app
ENV FLASK_ENV=production

# Открываем порт
EXPOSE 5000

# Запуск приложения
CMD ["python", "application.py", "runserver", "--host", "0.0.0.0"]
