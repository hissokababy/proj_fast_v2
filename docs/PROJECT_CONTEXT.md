# Fast and Easy — Project Context

**Version:** 1.0  
**Project:** Fast and Easy  
**Location:** Chirchiq, Tashkent Region, Uzbekistan  
**Repository:** https://github.com/hissokababy/proj_fast_v2  
**Working branch:** anzor  
**Status:** Preliminary backend audit completed; implementation not yet modified.

---

# 1. Project Overview

Fast and Easy is a bilingual website for an English language learning center located in Chirchiq, Tashkent Region, Uzbekistan.

The website must:
- Present the learning center and its educational programs.
- Display teachers, certificates, student results, and interior photos.
- Allow visitors to submit applications.
- Send application notifications to Telegram.
- Save all applications in the database.
- Support Uzbek and Russian languages.
- Provide an administrator-friendly content management system.
- Be optimized for Google, Yandex, and ChatGPT Search discovery.

The website should be maintainable and scalable.

# 2. Technology Stack

## Backend
- Python
- Django
- Django REST Framework
- Django Jazzmin
- PostgreSQL (production)
- SQLite (local development, temporarily)
- drf-spectacular
- django-storages
- MinIO / S3-compatible storage
- Telegram Bot API

## Frontend
- Next.js
- TypeScript
- Tailwind CSS

## Additional services
- Yandex Maps
- Google Analytics 4
- Google Search Console
- Yandex Metrica
- Telegram notifications

# 3. Languages

The website supports:
- Uzbek — default language.
- Russian — additional language.

Recommended URL structure:

- `/uz/`
- `/ru/`

The root URL `/` should redirect to `/uz/`.

All editable content and SEO metadata must support both languages.

The header must include a language switcher.

# 4. Website Structure

The homepage consists of the following sections:

1. Hero section.
2. About the learning center.
3. Courses and educational programs.
4. Teachers.
5. Certificates and student results.
6. Achievements of the learning center.
7. Application form.
8. Interior gallery.
9. Contacts and Yandex Map.

The following sections are explicitly excluded:
- FAQ.
- Reviews/testimonials.
- Blog.

## Courses

Initial courses:

- General English
- English for Kids
- English for Adults
- IELTS
- Pre-IELTS
- Speaking Club

Administrators must be able to add new courses.

Courses are displayed as cards on the homepage.

There must be no separate page for each course.

Administrators choose which courses are displayed.

Course prices must not be displayed publicly. Prices are communicated after an application.

## Achievements

The administrator must be able to edit achievement values and descriptions.

Examples:
- Number of students.
- Number of teachers.
- Years of experience.
- Other measurable achievements.

# 5. Backend Database Models

Existing models must be reviewed before changing or deleting anything.

The target data model includes:

## Teacher

Suggested fields:
- name_uz
- name_ru
- description_uz
- description_ru
- photo
- order
- is_active

## Certificate

Suggested fields:
- title_uz
- title_ru
- description_uz
- description_ru
- image
- order
- is_active

## InteriorPhoto

Suggested fields:
- title_uz
- title_ru
- image
- order
- is_active

## Course

Suggested fields:
- title_uz
- title_ru
- description_uz
- description_ru
- image
- order
- is_active
- show_on_home

## Achievement

Suggested fields:
- title_uz
- title_ru
- value
- suffix_uz
- suffix_ru
- order
- is_active

The value should support text such as `10+`, `500+`, and similar formats.

## SiteSettings

Suggested fields:
- site_name
- logo
- favicon
- phone
- email
- address_uz
- address_ru
- latitude
- longitude
- working_hours
- social_links
- Yandex Maps settings

This model should ideally have one configuration record.

## SEOSettings

Suggested fields:
- meta_title_uz
- meta_title_ru
- meta_description_uz
- meta_description_ru
- h1_uz
- h1_ru

SEO settings should be editable through Django Admin.

## Application

Suggested fields:
- full_name
- phone
- status
- utm_source
- utm_medium
- utm_campaign
- utm_content
- utm_term
- landing_page
- referrer
- language
- telegram_notified_at
- created_at
- updated_at

Possible statuses:
- new
- in_progress
- contacted
- completed
- cancelled

## Event

The existing Event model may be retained if it has a real purpose.

It must not be removed without checking its usage.

## OtherPhoto

The existing OtherPhoto model must be reviewed before deciding whether to retain or replace it.

# 6. Application Form

The public application form contains only:

- Name.
- Phone number.

When a visitor submits the form:

1. Validate the submitted data.
2. Save the application to the database.
3. Trigger a Telegram notification.
4. Record notification status.
5. Allow failed Telegram notifications to be retried.

Important:

**An application must remain saved even if Telegram is unavailable.**

The following attribution fields must be collected when available:

- utm_source
- utm_medium
- utm_campaign
- utm_content
- utm_term
- landing_page
- referrer

The application API must include anti-spam protection and request throttling.

# 7. API Structure

Existing endpoints:

- GET `/api/teachers/`
- GET `/api/certificates/`
- GET `/api/events/`
- GET `/api/interiors/`
- POST `/api/applications/create/`
- GET `/api/other-photos/<slug:key>/`

Planned endpoints:

- GET `/api/courses/`
- GET `/api/achievements/`
- GET `/api/settings/`

SEO settings may be included in the settings endpoint.

Public content endpoints must be read-only.

Content management must happen through Django Admin.

# 8. Django Admin

Django Jazzmin is used as the administration interface.

Administrators should be able to manage:

- Teachers.
- Certificates.
- Courses.
- Achievements.
- Interior photos.
- Site settings.
- SEO settings.
- Applications.

Application management should include:

- Status changes.
- Search by name and phone.
- Filtering by date and status.
- Application creation date.
- Telegram notification status.

The admin interface should be practical and easy to use.

# 9. SEO and Search Visibility

The website should be optimized for:

- Google Search.
- Yandex Search.
- ChatGPT Search.

SEO requirements:

- Unique title and description for each language.
- Correct H1 structure.
- Canonical URLs.
- hreflang for Uzbek and Russian.
- Open Graph metadata.
- Sitemap.xml.
- robots.txt.
- Schema.org structured data.
- EducationalOrganization or an appropriate LocalBusiness schema.
- Descriptive image alt attributes.
- Server-side rendering or static generation with Next.js.
- Fast page loading.
- Responsive design.
- HTTPS.
- WebP/AVIF image optimization.

## Local SEO

The physical learning center is located in Chirchiq.

The website should target:
- Chirchiq.
- Tashkent Region.
- Uzbekistan.

Do not create fake physical locations or misleading city-specific branches.

Maintain consistent business information across Google Business Profile and Yandex Business.

## ChatGPT Search

The website should allow OAI-SearchBot to crawl public pages.

Example robots.txt configuration:

    User-agent: OAI-SearchBot
    Allow: /

    User-agent: GPTBot
    Disallow: /

    User-agent: *
    Allow: /

    Sitemap: https://YOUR-DOMAIN/sitemap.xml

Search inclusion and ranking cannot be guaranteed.

# 10. Security Requirements

The preliminary audit identified the following issues:

- A `.env` file is committed to a public repository.
- Django SECRET_KEY is hardcoded in settings.
- DEBUG is enabled.
- ALLOWED_HOSTS is empty.
- Application endpoint permits anonymous requests without identified throttling.
- Upload validation needs review.
- CORS configuration needs review.
- Tests are currently insufficient.

Required actions:

1. Rotate all exposed Cloudinary credentials.
2. Revoke and regenerate the Telegram bot token.
3. Rotate MinIO credentials.
4. Replace the Django SECRET_KEY.
5. Remove `.env` from Git tracking.
6. Add `.env` to `.gitignore`.
7. Remove SQLite database files and Python cache files from Git tracking where appropriate.
8. Review Git history for exposed credentials.
9. Configure production DEBUG=False.
10. Configure ALLOWED_HOSTS.
11. Review CORS, CSRF, HTTPS, cookies, and security headers.
12. Add upload type and size validation.
13. Add API throttling and application anti-spam protection.

Never store actual credentials or secret values in this document.

# 11. Current Backend Structure

Preliminary structure:

    backend/
      config/
        settings.py
        urls.py
        asgi.py
        wsgi.py
      website/
        migrations/
        services/
        views/
        admin.py
        models.py
        serializers.py
        urls.py
        tests.py
      manage.py
      requirements.txt
      docker-compose.yml
      .env
      db.sqlite3

This structure must be verified against the current repository before implementation.

# 12. Preliminary Audit Findings

The following issues were identified:

- Incorrect type hints in certificate and event services.
- Empty placeholder test file.
- Possible malformed dependency entry in requirements.txt.
- OtherPhoto uses FileField although it appears to store images.
- Telegram notification workflow has not been identified.
- Application model lacks the planned UTM and status fields.
- Additional security configuration is required.

These findings are preliminary and must be verified against current files.

# 13. Development Rules

1. Continue working in the existing repository.
2. Do not create a new repository.
3. Use the `anzor` branch unless explicitly instructed otherwise.
4. Do not delete existing models or data without reviewing dependencies.
5. Use Django migrations for database changes.
6. Avoid destructive migrations.
7. Keep backend API contracts consistent with frontend requirements.
8. Add tests for new functionality.
9. Keep secrets out of Git.
10. Update this document after every significant development stage.

# 14. Current Development Status

Completed:
- Initial requirements gathering.
- Initial architecture selection.
- Preliminary backend structure review.
- Preliminary security review.
- Initial target database model planning.
- Initial API planning.

Not completed:
- Full migration audit.
- Full dependency audit.
- Database schema review.
- Telegram notification implementation review.
- Security remediation.
- Database model updates.
- API updates.
- Automated tests.
- Frontend implementation.
- Production deployment.

No code or database changes have been made as part of the preliminary audit.

GitHub integration previously returned HTTP 403 when attempting to create a file. Therefore, this document must currently be added manually.

# 15. Next Development Steps

## Stage 1 — Repository Audit

Obtain and review:

- Complete repository tree.
- requirements.txt
- docker-compose.yml
- settings.py
- models.py
- admin.py
- serializers.py
- urls.py
- views
- services
- migrations

Also check `.gitignore` and Git tracking of sensitive files without printing secret values.

## Stage 2 — Database Design

Compare the current schema with the target models.

Prepare safe Django migrations.

Do not delete existing data.

## Stage 3 — Backend Implementation

Implement:

- Multilingual content models.
- Course API.
- Achievement API.
- Site settings API.
- Application status and attribution.
- Telegram notification workflow.
- Notification retry mechanism.
- Admin improvements.

## Stage 4 — Tests and Security

Implement tests and resolve security findings.

## Stage 5 — Frontend

Build the bilingual Next.js website.

## Stage 6 — SEO and Analytics

Implement SEO, analytics, indexing, and structured data.

## Stage 7 — Deployment

Prepare production infrastructure and deployment.

---

# 16. Change History

## Version 1.0

- Created initial project context.
- Documented approved website requirements.
- Documented target architecture.
- Recorded preliminary backend audit findings.
- Recorded security risks.
- Defined implementation stages.