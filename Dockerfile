FROM python:3.9

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы в рабочую директорию
COPY . /app

# Пробрасываем порт 8081
EXPOSE 8081

# Команда для запуска приложения
CMD ["python", "app.py"]
