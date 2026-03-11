## 🎓 Проект: Платформа онлайн-обучения

### 📋 Описание проекта
Django-проект образовательной платформы с REST API для управления курсами и уроками. Проект использует Django REST Framework для создания API и включает 
кастомную модель пользователя с авторизацией по email. Проект реализует полный CRUD для образовательного контента с расширенными возможностями фильтрации и отчетности.
1

### 🛠 Технологический стек
* Python 3.13+
* Django 5.x
* Django REST Framework (DRF)
* PostgreSQL/SQLite (на выбор)
* Postman для тестирования API
* JWT для аутентификации
* Coverage для анализа покрытия кода тестами
* Celery для фоновых задач
* Redis для кэширования и брокера сообщений
* Docker & Docker Compose
* GitHub Actions для CI/CD
* Stripe для платежей
* drf-yasg для документации API

## 🌐 Настройка удаленного сервера и деплой
### 📍 Требования к серверу
* Ubuntu 20.04+ / Debian 10+

* Минимум 2GB RAM

* 20GB свободного места на диске

* Публичный IP-адрес

* Открытые порты: 22 (SSH), 80/443 (HTTP/HTTPS), 8000 (приложение)

### 🚀 Быстрая настройка сервера

Создайте виртуальную машину, подключитесь к ней. В рамках учебного проекта сервер развернут на базе Яндекс.Cloud по адресу: http://158.160.94.12/

1. Подключение к серверу    
    ```ssh alexandra@158.160.94.12```

2. Установка необходимого ПО
    ```
   # Обновление системы
    sudo apt update && sudo apt upgrade -y
    
    # Установка Docker
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker $USER
    
    # Установка Docker Compose
    sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    
    # Установка дополнительных утилит
    sudo apt install -y git nginx python3-pip```


### 🚀 Быстрый старт
**Требования**
* Docker

* Docker Compose

* Git

### Запуск проекта
1. Клонируйте репозиторий:

```git clone https://github.com/Alexandra03091986/Django_REST_Framework_30-33/pull/7 cd Django_REST_Framework_30-33``` 

2. Создайте файл окружения:

```cp .env.example .env```

⚙️ Настройка окружения
Создайте (отредактируйте) файл .env на основе .env.example, указав свои настройки

3. Запустите проект:
``docker-compose up --build``

***Примечание:*** Для первого запуска может потребоваться время на сборку образов и применение миграций.

Проверьте статус сервисов:

```docker-compose ps```

4. Проект будет доступен по адресу:

- Django: http://localhost:8000

- API документация: http://localhost:8000/swagger/

- Админка: http://localhost:8000/admin/

### 🔧 Сервисы
Проект состоит из 5 сервисов:
1. Web (Django) - основной сервис, который запускает Django-приложение.
* Порт: 8000

* URL: http://localhost:8000

* Команда проверки: curl http://localhost:8000/

### Выполнить команду в контейнере web
```docker-compose exec web python manage.py [command]```

2. PostgreSQL (База данных)
* Порт: 5432

* Проверка: ```docker-compose exec postgres pg_isready -U postgres```

3. Redis (Кэш и брокер для Celery)
* Порт: 6379

* Проверка: ```docker-compose exec redis redis-cli ping```

Должен ответить: ПОНГ

4. Celery (Фоновые задачи)
Проверка: ```docker-compose exec celery celery -A config status```

5. Celery Beat (Планировщик задач)
Проверка: ```docker-compose logs celery-beat```

## 🛠 Команды управления

### Запуск и остановка

    # Запуск в фоновом режиме
    docker-compose up -d
    
    # Остановка
    docker-compose down
    
    # Пересборка и запуск
    docker-compose up --build -d
    
    # Перезапуск всех
    docker-compose restart
    
    # Просмотр логов
    docker-compose logs -f [service_name]

### 🔍 Мониторинг
#### Просмотр логов
#### Все логи
    docker-compose logs

#### Логи конкретного сервиса
    docker-compose logs web
    docker-compose logs postgres
    docker-compose logs celery

### Проверка сети

#### Проверить подключение между контейнерами
    docker-compose exec web ping postgres
    docker-compose exec web ping redis

### 🗑️ Очистка
#### Остановить и удалить контейнеры
    docker-compose down

##### Остановить и удалить контейнеры с volumes
    docker-compose down -v

### 📚 Документация API
**После запуска проекта доступна автоматическая документация:**

- Swagger UI: http://localhost:8000/swagger/

- ReDoc: http://localhost:8000/redoc/


## 📁 Структура проекта
### Приложения
1. **users** - управление пользователями
    - Модель Пользователь (User)
      - Кастомная модель пользователя с авторизацией по email
      - Дополнительные поля: телефон, город, аватар
      
    - Модель Платежи (Payments)
      - пользователь,
      - дата оплаты,
      - оплаченный курс или урок,
      - сумма оплаты,
      - способ оплаты: наличные, перевод на счет или онлайн-оплата.
      - Id сессии,
      - Ссылка на оплату
   

2. **materials (или lms)** - управление образовательным контентом

   - Модель Курса (Course)

   - Модель Урока (Lesson)

   - Связь "один ко многим" между курсом и уроками
   
   - Модель подписки на курс (Subscription)


### 3. Реализация API
### Для курсов (Course):
   * Использован ViewSet для полного CRUD
   * Реализованы операции:
     * Создание
     * Просмотр списка и сведений
     * Обновление
     * Удаление
   * Созданы сериализаторы:
     * CourseSerializer
     * CourseDetailSerializer,одновременно выводит: 
       * Количество уроков в курсе ```count_lessons```
       * Полную информацию по всем урокам курса ```lessons```

### Для уроков (Lesson):
  * Применены Generic-классы
  * Полный набор CRUD-операций
  * Собственный сериализатор

### Для платежей (Payments):
    * Настроена фильтрация для эндпоинта платежей с возможностями:
      * Сортировка по дате оплаты (asc/desc)      
      * Фильтрация по курсу       
      * Фильтрация по уроку
      * Фильтрация по способу оплаты
* **Подключена возможность оплаты курсов** через https://stripe.com/docs/api.



### Для пользователя (User):
* Расширен сериализатор профиля пользователя для вывода истории платежей

* Реализован CRUD для пользователей, в том числе регистрацию пользователей
* Настроено использование JWT-авторизации
* Закрыт каждый эндпоинт авторизацией (кроме авторизации и регистрации).

### **Особенности реализации**

* Заведена группа модераторов с правами работы с любыми уроками и курсами (без возможности удалять и создавать).

* Реализованы права доступа: пользователи могут видеть, редактировать и удалять только свои курсы и уроки.

* Валидатор для проверки ссылок на видео (интегрирован в сериализатор).

* Эндпоинт для управления подписками на курсы.

* Пагинация для вывода всех уроков и курсов.

* Тестирование с использованием метода ```setUp``` для заполнения базы данных тестовыми данными.

* Подключен и настроен вывод документации для проекта. Для работы с документацией проекта воспользовались библиотекой ```drf-yasg```.

* Настроена работа с Celery и celery-beat для периодических задач

* Асинхронная рассылка писем пользователям об обновлении материалов курса.

* Фоновая задача для блокировки неактивных пользователей (не заходили более месяца). по дате последнего входа по полю ```last_login``` и, если пользователь не заходил более месяца, блокирует его с помощью флага ```is_active```.

### 4. Тестирование
* Все эндпоинты проверены через Postman
* Протестированы все CRUD-операции
* Проверены связи между моделями

## Настройка проекта на удаленном сервере

#### 3. Настройка проекта на сервере
```
# Создание директории проекта
sudo mkdir -p /var/www/drf-online-platform
sudo chown -R $USER:$USER /var/www/drf-online-platform
cd /var/www/drf-online-platform

# Клонирование проекта
git clone https://github.com/Alexandra03091986/Django_REST_Framework_30-33.git .
# Или скопируйте файлы через scp/sftp

# Создание .env файла
cp .env.example .env
nano .env  # Отредактируйте настройки
```
#### 4. Настройка .env файла для продакшена

```
# .env файл для продакшена
DEBUG=False
SECRET_KEY=ваш-очень-сложный-секретный-ключ-здесь
ALLOWED_HOSTS=ваш-домен.ру,ваш-ip-адрес,localhost,127.0.0.1

# База данных
DATABASE_URL=postgresql://postgres:password@postgres:5432/drf_db

# Redis
REDIS_URL=redis://redis:6379/0

# Celery
CELERY_BROKER_URL=redis://redis:6379/1
CELERY_RESULT_BACKEND=redis://redis:6379/2

# Email (для рассылок)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=ваш-email@gmail.com
EMAIL_HOST_PASSWORD=ваш-пароль-приложения
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=ваш-email@gmail.com

# Stripe (для платежей)
STRIPE_SECRET_KEY=ваш-stripe-секретный-ключ
STRIPE_PUBLIC_KEY=ваш-stripe-публичный-ключ
```

## 🐳 Деплой с Docker Compose
#### 1. Сборка и запуск
```
cd /var/www/drf-online-platform

# Сборка образов
docker-compose build

# Запуск в фоновом режиме
docker-compose up -d

# Проверка статуса
docker-compose ps

# Просмотр логов
docker-compose logs -f web
```

#### 2. Выполнение миграций и создание суперпользователя
```
# Миграции
docker-compose exec web python manage.py migrate

# Создание суперпользователя
docker-compose exec web python manage.py createsuperuser

# Сборка статических файлов
docker-compose exec web python manage.py collectstatic --no-input
```
## 📦 Автоматический деплой с GitHub Actions
Ваш проект настроен для CI/CD. Для работы необходимо:

#### 1. Настройка секретов в GitHub
В настройках репозитория (Settings → Secrets and variables → Actions) добавьте:

* DOCKER_HUB_USERNAME - ваш логин на Docker Hub

* DOCKER_HUB_ACCESS_TOKEN - токен доступа к Docker Hub

* SERVER_IP - IP-адрес вашего сервера

* SSH_USER_SERVER - имя пользователя SSH (обычно ubuntu или debian)

* SSH_PRIVATE_KEY - приватный ключ SSH для доступа к серверу

* SECRET_KEY - секретный ключ Django

* DATABASE_URL - строка подключения к БД

* REDIS_URL - строка подключения к Redis

* STRIPE_SECRET_KEY - ключ Stripe

### 🚨 Устранение неполадок
#### 1. Порт уже занят

```
# Проверка занятых портов
sudo netstat -tulpn | grep :80
sudo netstat -tulpn | grep :8000

# Освобождение порта
sudo fuser -k 80/tcp
```

#### 2. Проблемы с Docker

```
# Перезапуск Docker
sudo systemctl restart docker

# Очистка неиспользуемых ресурсов
docker system prune -a
```

#### 3. Проблемы с базой данных
```
# Проверка подключения к БД
docker-compose exec postgres pg_isready -U postgres

# Сброс базы данных (осторожно!)
docker-compose down -v
docker-compose up -d
```

### 🔐 Рекомендации по безопасности
#### 1. Регулярно обновляйте систему
```
sudo apt update && sudo apt upgrade -y
Настройте фаервол
```
#### 2. Настройте фаервол
```
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 8000/tcp
sudo ufw enable
```
### 📞 Поддержка
При возникновении проблем:

1. Проверьте логи: ```docker-compose logs```

2. Проверьте статус контейнеров: ```docker-compose ps```

3. Убедитесь что порты открыты: ```sudo netstat -tulpn```

4. Проверьте переменные окружения в ```.env``` файле

### 📞 Контакты и поддержка
Проект разработан в рамках учебного курса. Для вопросов и предложений обращайтесь через Issues в репозитории.

**Автор:** Александра

**GitHub:** [Alexandra03091986](https://github.com/Alexandra03091986)

**Проект:** [Django REST Framework 30-33](https://github.com/Alexandra03091986/Django_REST_Framework_30-33)