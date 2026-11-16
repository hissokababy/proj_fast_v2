# Fast and Easy — Project Context

**Version:** 2.0  
**Project:** Fast and Easy  
**Location:** Chirchiq, Tashkent Region, Uzbekistan  
**Repository:** https://github.com/hissokababy/proj_fast_v2  
**Working branch:** `anzor`  
**Last updated:** 2026-11-16

---

# 1. Project Overview

Fast and Easy — сайт языкового центра в Чирчике, Узбекистан.

Основные задачи:
- Представление языкового центра.
- Информация о курсах и преподавателях.
- Галерея сертификатов, мероприятий и интерьера.
- Приём заявок от посетителей.
- Отправка уведомлений о заявках в Telegram.
- Поддержка узбекского и русского языков.
- Управление контентом через Django Admin.
- SEO и локальное продвижение.

# 2. Technology Stack

## Backend
- Python
- Django 6.1.2
- Django REST Framework
- Django Jazzmin
- PostgreSQL 17
- SQLite для локальной разработки при необходимости
- drf-spectacular
- django-storages
- MinIO (S3-compatible storage)
- pyTelegramBotAPI

## Frontend
- Next.js
- TypeScript
- Tailwind CSS

## Infrastructure
- Docker
- Docker Compose
- PostgreSQL
- MinIO

## External services
- Yandex Maps
- Telegram Bot API
- Google Analytics 4
- Google Search Console
- Yandex Metrica

# 3. Languages

Сайт поддерживает два языка:

- Узбекский (`uz`) — основной.
- Русский (`ru`) — дополнительный.

Перевод контента выполняется на backend с использованием отдельных полей:
- `field_uz`
- `field_ru`

API принимает параметр `?lang=uz` или `?lang=ru`.

Правила:
- По умолчанию используется узбекский.
- При неподдерживаемом языке используется узбекский.
- Если перевод выбранного языка пустой, используется русский.

Интерфейс сайта (меню, кнопки, системные сообщения и другие UI-элементы) переводится на frontend.

Административная панель Django используется только на русском языке.

# 4. Website Structure

Основные секции сайта:

1. Hero.
2. О центре.
3. Курсы.
4. Преподаватели.
5. Сертификаты.
6. Мероприятия.
7. Форма заявки.
8. Интерьер.
9. Контакты.
10. Яндекс Карта.

Исключены:
- FAQ.
- Отзывы.
- Блог.
- Achievement как отдельная модель.

## Courses

Администратор управляет курсами.

Начальные направления:
- General English.
- English for Kids.
- English for Adults.
- IELTS.
- Pre-IELTS.
- Speaking Club.

Возможности:
- Создание и редактирование курсов.
- Два языка.
- Изображение.
- Порядок отображения.
- Активация и деактивация.
- Выбор курсов для главной страницы.

Цены публично не отображаются.

# 5. Database Models

Реализованные модели приложения `website`:

## Teacher
- name_uz
- name_ru
- description_uz
- description_ru
- photo
- order
- is_active

## Certificate
- title_uz
- title_ru
- description_uz
- description_ru
- image
- order
- is_active

## Event
- title_uz
- title_ru
- description_uz
- description_ru
- image
- order
- is_active

## InteriorPhoto
- title_uz
- title_ru
- image
- order
- is_active

## Course
- title_uz
- title_ru
- description_uz
- description_ru
- image
- order
- is_active
- show_on_home

## Application
- full_name
- phone
- status
- utm_source
- utm_medium
- utm_campaign
- utm_term
- utm_content
- landing_page
- referrer
- language
- telegram_notified_at
- created_at
- updated_at

Статусы:
- new
- in_progress
- completed
- rejected

## OtherPhoto
- title
- key
- image

Используется для дополнительных изображений, доступных по уникальному ключу.

## SiteSettings

- site_name
- logo
- favicon
- phone
- email
- address_uz
- address_ru
- latitude
- longitude
- working_hours_uz
- working_hours_ru
- instagram_url
- telegram_url
- facebook_url
- youtube_url
- yandex_maps_api_key
- yandex_maps_map_id

## SEOSettings

- meta_title_uz
- meta_title_ru
- meta_description_uz
- meta_description_ru
- h1_uz
- h1_ru

SiteSettings и SEOSettings — singleton-модели. Создание дополнительных записей ограничено через Django Admin.

Achievement не используется и не планируется.

# 6. Application Workflow

Форма заявки содержит:
- Имя.
- Телефон.

Дополнительные данные:
- UTM-параметры.
- Страница отправки.
- Referrer.
- Язык сайта.

Последовательность:

1. Frontend отправляет заявку.
2. Backend валидирует данные.
3. Заявка сохраняется в базе данных.
4. Backend отправляет уведомление в Telegram-группу.
5. При успешной отправке записывается `telegram_notified_at`.

**Важные правила:**

- Сохранение заявки не зависит от доступности Telegram.
- Если Telegram недоступен, заявка остаётся в базе.
- Повторных отправок нет.
- Celery, Redis, Beat и фоновые retry-механизмы не используются.
- Не создавать отдельный механизм повторной отправки.
- Telegram-уведомление отправляется один раз при создании заявки.

## Anti-spam

Используются:
- DRF ScopedRateThrottle.
- Ограничение 5 заявок в час.
- Honeypot-поле `website`.
- Валидация имени и телефона.

# 7. API

Все публичные endpoints доступны без авторизации.

## Content API

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/teachers/` | Преподаватели |
| GET | `/api/certificates/` | Сертификаты |
| GET | `/api/events/` | Мероприятия |
| GET | `/api/interiors/` | Интерьер |
| GET | `/api/courses/` | Все активные курсы |
| GET | `/api/courses/?home=true` | Курсы для главной |
| GET | `/api/site-settings/` | Настройки сайта |
| GET | `/api/seo/` | SEO |
| GET | `/api/other-photos/{key}/` | Дополнительное фото |
| POST | `/api/applications/create/` | Создание заявки |

## API Documentation

- Swagger: `/api/docs/`
- ReDoc: `/api/redoc/`
- OpenAPI schema: `/api/schema/`

Публичные endpoints контента доступны только для чтения.

Создание заявки — единственный публичный endpoint записи.

# 8. Django Admin

Используется Django Jazzmin.

Админка только на русском языке.

Управление:
- Преподавателями.
- Сертификатами.
- Мероприятиями.
- Интерьером.
- Курсами.
- Заявками.
- Дополнительными фотографиями.
- Настройками сайта.
- SEO.

Для контента доступны сортировка и активация.

Для заявок:
- Поиск по имени и телефону.
- Фильтрация по статусу.
- Фильтрация по языку.
- Фильтрация по дате.
- Отображение даты уведомления Telegram.

SiteSettings и SEOSettings ограничены одной записью через Django Admin.

# 9. Docker Infrastructure

Docker Compose используется для запуска:

- Django.
- PostgreSQL.
- MinIO.

Основные файлы:

```text
backend/
├── Dockerfile
├── docker-compose.yml
├── .env.example
└── config/
    └── settings.py
```

Конфиденциальные значения хранятся в `backend/.env`.

`.env`, база SQLite, виртуальное окружение и Python cache не должны попадать в Git.

`.env.example` хранится в репозитории без реальных секретов.

## PostgreSQL

Используется PostgreSQL 17.

В Docker Django подключается к базе через имя сервиса `db`.

## MinIO

Используется S3-совместимое хранилище для изображений и файлов.

Необходимо отдельно проверить:
- Внутренний адрес MinIO для Django.
- Публичный адрес для браузера.
- Формирование URL файлов.
- Доступность файлов с frontend.
- Настройки bucket и доступа.

Внутренний Docker hostname `minio` не должен использоваться браузером напрямую.

# 10. Security

Основные требования:

- `SECRET_KEY` только через environment variables.
- `DEBUG=False` в production.
- Корректный `ALLOWED_HOSTS`.
- CORS только для разрешённых origins.
- HTTPS в production.
- Секреты не хранятся в Git.
- Telegram token не публикуется.
- MinIO credentials не публикуются.
- API key Яндекс Карт не выдаётся публичным API.
- Валидация загружаемых файлов.
- Защита от спама.
- Ограничение запросов.

Дополнительно требуется проверить:
- Production deployment.
- Gunicorn или другой production WSGI server.
- CSRF и security headers.
- Проверку типов и размеров загружаемых файлов.
- Публичную доступность MinIO.
- Ротацию секретов при необходимости.

# 11. Current Backend Structure

```text
backend/
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── website/
│   ├── migrations/
│   ├── services/
│   ├── views/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── tests.py
├── tg_bot/
│   ├── handlers/
│   ├── management/
│   │   └── commands/
│   │       └── runbot.py
│   ├── services/
│   │   └── telegram.py
│   ├── bot.py
│   ├── admin.py
│   ├── models.py
│   └── tests.py
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── manage.py
└── requirements.txt
```

# 12. Telegram Bot

Используется библиотека pyTelegramBotAPI.

Структура:
- `bot.py` — создание бота.
- `handlers/start.py` — обработчики `/start` и `/help`.
- `management/commands/runbot.py` — запуск polling.
- `services/telegram.py` — отправка уведомлений о заявках.

Бот запускается отдельной management-командой.

Telegram-уведомления о заявках отправляются непосредственно из API после сохранения заявки.

Повторная отправка уведомлений не реализуется.

# 13. Development Rules

1. Работать в существующем репозитории.
2. Рабочая ветка — `anzor`.
3. Не менять архитектуру без согласования.
4. Не удалять модели и данные без проверки.
5. Миграции сначала анализировать, затем создавать и применять.
6. Не добавлять ненужные зависимости.
7. Не внедрять Celery и Redis для заявок.
8. Не добавлять Achievement.
9. Документацию обновлять после значимых изменений.
10. Работать небольшими этапами — 1–2 задачи за раз.
11. Сообщать, когда логический этап готов к коммиту.

# 14. Current Development Status

## Implemented

- Основные Django-модели.
- Django Admin.
- Singleton-защита настроек.
- Мультиязычные сериализаторы.
- Публичные API endpoints.
- Фильтрация активного контента.
- API документация.
- Создание заявок.
- Сохранение UTM-данных.
- Anti-spam и throttling.
- Telegram notification service.
- Telegram bot на pyTelegramBotAPI.
- Docker Compose для Django, PostgreSQL и MinIO.
- Переменные окружения.

## Verified

- Миграции `website` с 0001 по 0008 применены.
- `makemigrations --check --dry-run` не выявил новых миграций.
- `migrate --check` не выявил неприменённых миграций.
- Основные публичные views и services проверены по коду.
- API serializers и маршруты проверены.
- Telegram workflow проверен по коду.

## Remaining Backend Work

1. Проверить публичную доступность файлов MinIO.
2. Разделить внутренний и публичный адрес MinIO.
3. Проверить production-настройки Django.
4. Проверить API локально через HTTP.
5. Проверить валидацию заявок и поведение Telegram.
6. Проверить загрузку изображений.
7. Провести итоговый аудит безопасности.
8. Обновить и запустить автоматические тесты.

Автоматические тесты пока не являются приоритетом — сначала завершается аудит и исправление основной логики.

## Frontend

Frontend Next.js должен быть реализован отдельно после завершения backend.

# 15. Next Development Steps

1. Обновить `PROJECT_STATUS.md`.
2. Завершить настройку MinIO.
3. Проверить production settings.
4. Провести локальную проверку API.
5. Исправить обнаруженные проблемы.
6. Перейти к автоматическим тестам.
7. Начать frontend.
8. Настроить SEO и аналитику.
9. Подготовить production deployment.

---

# 16. Change History

## Version 2.0 — 2026-11-16

- Обновлена архитектура проекта.
- Документ приведён в соответствие с текущими Django-моделями.
- Обновлена структура API.
- Зафиксирована текущая реализация Telegram.
- Удалены устаревшие требования к Achievement.
- Удалены требования к повторной отправке Telegram.
- Обновлена Docker-инфраструктура.
- Зафиксировано текущее состояние миграций.
- Добавлены актуальные задачи backend-разработки.
