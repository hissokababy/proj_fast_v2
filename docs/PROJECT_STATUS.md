# Fast and Easy — Project Status

**Last updated:** 2026-11-09  
**Branch:** `anzor`  
**Repository:** `hissokababy/proj_fast_v2`

## 1. Current stage

Backend development — cleanup, configuration review and security preparation.

## 2. Completed

- Django project configured.
- Django REST Framework configured.
- Django Jazzmin installed.
- `website` application created.
- Models, serializers, admin, views, URLs and services implemented.
- Initial migrations created and applied.
- Migrations `0001–0007` applied.
- `makemigrations --check --dry-run` completed without changes.
- API documentation configured through drf-spectacular.
- MinIO configuration added.
- Root `.gitignore` created.
- Python cache files excluded from Git tracking.
- `backend/.env` removed from Git tracking.
- `backend/db.sqlite3` removed from Git tracking.
- Local `.env` and SQLite database files preserved.

## 3. Git status

- Branch: `anzor`.
- Latest local commit: `fda2e65`.
- Commit message: `chore: remove local files from tracking and update gitignore`.
- Working tree was clean after the commit.
- Push status must be verified separately.

## 4. Current backend structure

```text
backend/
├── config/
├── website/
│   ├── migrations/
│   ├── services/
│   ├── views/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   └── urls.py
├── manage.py
├── requirements.txt
└── docker-compose.yml
```

## 5. Next tasks

1. Verify GitHub synchronization.
2. Rotate all credentials previously exposed through `.env`.
3. Review Django settings and move secrets into environment variables.
4. Review DEBUG, ALLOWED_HOSTS, CORS and security configuration.
5. Review requirements.txt and fix dependency issues.
6. Review existing models and API.
7. Add backend tests.
8. Implement application notification through Telegram.
9. Add application statuses and UTM attribution.
10. Prepare PostgreSQL and production storage configuration.
11. Begin frontend development with Next.js and TypeScript.

## 6. Important development rules

- Work in small steps.
- Maximum 1–2 tasks per instruction.
- Do not run migrations or change models without checking current state.
- Preserve local environment and database files.
- Do not commit `.env`, databases, virtual environments or Python cache.
- Update `project_context.md` and this file after significant changes.
- Follow the approved project requirements.
