# Fast and Easy — Project Status

**Last updated:** 2026-11-16
**Branch:** `anzor`
**Repository:** `hissokababy/proj_fast_v2`

---

# 1. Current Stage

Backend development — завершение аудита, исправление конфигурации и подготовка к локальной проверке API.

Основная backend-логика реализована. Сейчас проверяются инфраструктура, безопасность и корректность работы API.

# 2. Completed

## Django

- Django 6.1.2 configured.
- Django REST Framework configured.
- Django Jazzmin configured.
- drf-spectacular configured.
- Applications `website` and `tg_bot` created.
- Database models implemented.
- Serializers implemented.
- Public API views implemented.
- API URLs configured.
- Django Admin configured in Russian.
- Singleton protection for SiteSettings and SEOSettings implemented.

## Database

Реализованы модели:

- Teacher
- Certificate
- Event
- InteriorPhoto
- Course
- Application
- OtherPhoto
- SiteSettings
- SEOSettings

## Migrations

Миграции приложения `website`:

- 0001_initial
- 0002_alter_certificate_title_alter_event_title_and_more
- 0003_otherphoto
- 0004_alter_otherphoto_key_alter_otherphoto_title
- 0005_alter_otherphoto_image
- 0006_tariff
- 0007_delete_tariff
- 0008_course_seosettings_sitesettings_and_more

Все восемь миграций применены.

Проверки:

- `makemigrations --check --dry-run` — новых миграций не обнаружено.
- `migrate --check` — неприменённых миграций нет.

## API

Реализованы:

- Teachers API.
- Certificates API.
- Events API.
- Interiors API.
- Courses API.
- Site Settings API.
- SEO API.
- Other Photos API.
- Applications API.

Поддерживается переключение языков через `?lang=uz` и `?lang=ru`.

API documentation:

- Swagger.
- ReDoc.
- OpenAPI schema.

## Applications

- Создание заявок.
- Валидация имени и телефона.
- UTM attribution.
- Сохранение landing page и referrer.
- Сохранение языка сайта.
- Honeypot anti-spam.
- DRF throttling: 5 заявок в час.
- Сохранение заявки до отправки Telegram-уведомления.

## Telegram

- pyTelegramBotAPI installed.
- Bot initialization implemented.
- `/start` and `/help` handlers implemented.
- Management command `runbot` implemented.
- Telegram notification service implemented.
- Notification timestamp `telegram_notified_at` implemented.

Принятая логика:

1. Сохранить заявку в БД.
2. Отправить уведомление в Telegram.
3. Завершить обработку.

Повторные отправки не используются.

## Docker

Docker Compose включает:

- Django.
- PostgreSQL 17.
- MinIO.

Добавлены:

- Dockerfile.
- docker-compose.yml.
- `.env.example`.

Переменные окружения используются для конфигурации Django, PostgreSQL, MinIO и Telegram.

## Git

- Рабочая ветка: `anzor`.
- `.gitignore` настроен.
- `.env` исключён из Git tracking.
- SQLite database исключена из Git tracking.
- Python cache исключён из Git tracking.
- `.env.example` хранится в репозитории.

# 3. Current Backend Structure

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
│   ├── tests.py
│   └── urls.py
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

# 4. Completed Audit

Проверены:

- Основные Django models.
- Django Admin.
- API serializers.
- API URLs.
- Основные API views.
- Content services.
- Application workflow.
- Telegram notification workflow.
- Django settings.
- Миграции.

Выявленные моменты:

1. Необходимо проверить публичную доступность файлов MinIO.
2. Нужно разделить внутренний и внешний адрес MinIO.
3. Необходимо проверить production-настройки Django.
4. Нужно проверить допустимые значения поля `language` в заявках.
5. Необходимо провести локальную HTTP-проверку API.
6. Нужно проверить загрузку изображений через MinIO.

# 5. Remaining Backend Tasks

## Infrastructure

- [ ] Проверить MinIO public endpoint.
- [ ] Проверить доступность изображений из браузера.
- [ ] Проверить bucket configuration.
- [ ] Проверить Docker networking.
- [ ] Проверить production WSGI server.

## Security

- [ ] Проверить обязательность `DJANGO_SECRET_KEY`.
- [ ] Проверить `DEBUG=False` для production.
- [ ] Проверить `ALLOWED_HOSTS`.
- [ ] Настроить production CORS origins.
- [ ] Проверить CSRF и security headers.
- [ ] Проверить ограничения загрузки файлов.
- [ ] Проверить секреты и их ротацию.

## API

- [ ] Проверить все endpoints локально.
- [ ] Проверить JSON responses.
- [ ] Проверить переключение языков.
- [ ] Проверить fallback переводов.
- [ ] Проверить создание заявок.
- [ ] Проверить отправку Telegram.
- [ ] Проверить поведение API при отсутствии настроек.
- [ ] Проверить загрузку изображений.

## Tests

Автоматические тесты пока не реализуются. Сначала завершается основная проверка и исправление backend.

После этого:

- [ ] Model tests.
- [ ] Serializer tests.
- [ ] API tests.
- [ ] Application workflow tests.
- [ ] Telegram service tests.

# 6. Frontend

Frontend пока не реализован.

Планируемый стек:

- Next.js.
- TypeScript.
- Tailwind CSS.

Frontend должен использовать существующий backend API.

Требования:

- Узбекский и русский языки.
- Перевод UI на frontend.
- Адаптивная верстка.
- Яндекс Карты.
- SEO.
- Интеграция формы заявки.
- Отображение контента из Django API.

# 7. Important Decisions

- Основной язык сайта — узбекский.
- Русский — дополнительный.
- Админка только на русском.
- Переводы контента хранятся на backend.
- Переводы UI выполняются на frontend.
- Achievement не используется.
- SiteSettings и SEOSettings — singleton.
- Публичный API контента read-only.
- Заявка сохраняется до Telegram-уведомления.
- Повторная отправка Telegram не нужна.
- Celery и Redis не используются.
- PostgreSQL используется в Docker.
- MinIO используется для хранения файлов.

# 8. Next Development Steps

1. Завершить настройку MinIO.
2. Проверить Django production settings.
3. Проверить API локально.
4. Исправить обнаруженные проблемы.
5. Проверить загрузку файлов.
6. Завершить backend security review.
7. Перейти к автоматическим тестам.
8. Начать frontend-разработку.
9. Настроить SEO и аналитику.
10. Подготовить production deployment.

# 9. Development Rules

1. Работать в ветке `anzor`.
2. Давать не более 1–2 задач за раз.
3. Не создавать миграции без предварительной проверки.
4. Не удалять существующие данные без согласования.
5. Не добавлять лишние зависимости.
6. Не использовать Celery и Redis для заявок.
7. Не реализовывать повторную отправку Telegram.
8. Не коммитить `.env`, SQLite, venv и Python cache.
9. Обновлять документацию после значимых этапов.
10. Сообщать, когда логический этап готов к коммиту.

---

# 10. Change History

## Version 2.0 — 2026-11-16

- Обновлён статус backend.
- Добавлены актуальные модели и API.
- Обновлено состояние миграций.
- Добавлена реализация Telegram.
- Добавлено текущее состояние Docker.
- Удалены устаревшие задачи.
- Зафиксированы оставшиеся задачи аудита.
- Обновлён план дальнейшей разработки.
