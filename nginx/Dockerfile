FROM nginx:latest

# Создаем папку для статики Django
RUN mkdir -p /app/staticfiles

# Копируем наш конфиг Nginx
COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80