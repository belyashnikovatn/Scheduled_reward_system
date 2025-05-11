# Scheduled Reward System

Система управления отложенными наградами для пользователей с использованием Django, Celery и Redis. Позволяет планировать начисление монет пользователям на будущее время и обеспечивает автоматическое выполнение этих задач.

## 📌 Функциональность

- **Аутентификация**: JWT-аутентификация с использованием `rest_framework_simplejwt`.
- **Профиль пользователя**: Получение информации о текущем пользователе.
- **Планирование наград**: Создание отложенных наград с указанием суммы и времени исполнения.
- **Очередь задач**: Автоматическое начисление монет в указанное время с использованием Celery и Redis.
- **Логирование**: Ведение истории начислений в модели `RewardLog`.
- **Документация API**: Доступна через Swagger и ReDoc.

## 🛠️ Стек технологий

- **Backend**: Django 4.2, Django REST Framework
- **Аутентификация**: JWT (`rest_framework_simplejwt`)
- **Очереди**: Celery 5.x
- **Брокер сообщений**: Redis
- **База данных**: PostgreSQL
- **Документация API**: drf-yasg (Swagger/OpenAPI)
- **Контейнеризация**: Docker, Docker Compose

## 🚀 Запуск проекта через Docker

1. **Клонируйте репозиторий**:

   ```bash
   git clone https://github.com/belyashnikovatn/Scheduled_reward_system.git
   cd Scheduled_reward_system
   ```

2. **Создайте и запустите контейнеры**:

   ```bash
   docker-compose up --build
   ```

   Это запустит следующие сервисы:

   - `web`: Django-приложение
   - `db`: PostgreSQL
   - `redis`: Брокер сообщений для Celery
   - `worker`: Celery worker для обработки задач

3. **Применение миграций и создание пользователей через `entrypoint.sh`**:

Сценарий запуска:

- Ожидание готовности базы данных и Redis
- Применение миграций
- Запуск Celery
- Запуск Django-сервера

4. **Доступ к приложению**:

   - API: [http://localhost:8000/api/](http://localhost:8000/api/)
   - Swagger: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
   - ReDoc: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)
   - Админка: [http://localhost:8000/admin/](http://localhost:8000/admin/)

## 🧩 Описание компонентов

### Celery и Redis

- **Celery**: Обрабатывает отложенные задачи по начислению наград.
- **Redis**: Используется как брокер сообщений для Celery.

### Планирование наград

Пользователь может создать отложенную награду, указав сумму и время исполнения. Celery Beat периодически проверяет запланированные награды и, при наступлении времени исполнения, Celery worker начисляет монеты пользователю и записывает событие в `RewardLog`.

## 📄 API Endpoints

- `POST /api/token/`: Получение JWT токена
- `POST /api/token/refresh/`: Обновление токена
- `POST /api/token/verify/`: Проверка токена
- `GET /api/profile/`: Информация о текущем пользователе
- `POST /api/rewards/request/`: Создание отложенной награды
- `GET /api/rewards/`: Список всех выданных наград пользователю


## 📬 Контакты

Разработчик: [belyashnikovatn](mailto:belyashnikova.tn@gmail.com)
Задание: [ссылка](https://docs.google.com/document/d/190LiIppiBbY3L2ntdYHeH7nLOeX7suR5-v0ktHMe3rs/edit?tab=t.0)