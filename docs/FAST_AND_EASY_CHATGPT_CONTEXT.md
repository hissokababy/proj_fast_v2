# Fast and Easy --- Project Context for ChatGPT

> **Purpose:** This file is the handoff document for new ChatGPT
> conversations about the Fast and Easy project. Read it before
> proposing changes or writing code.
>
> **Last updated:** 2026-11-10\
> **Repository:** `hissokababy/proj_fast_v2`\
> **Working branch:** `anzor`

------------------------------------------------------------------------

## 1. Project overview

**Fast and Easy** is a language-learning centre in Chirchiq, Uzbekistan.
The current task is to stabilise and complete the Django backend and its
public API. The frontend is planned for a later phase.

The project should be developed pragmatically, prioritising
implementation speed while retaining basic security, correctness, and
maintainability.

### Current product direction

-   Public website languages: **Uzbek and Russian**.
-   Default public language: **Uzbek**.
-   Users switch language using a visible language-switch button.
-   Django Admin interface: **Russian only**.
-   Course/tariff information should be displayed without prices.
-   Public application form: name and phone number.
-   On submission: save the application in the database, then notify one
    Telegram group.

------------------------------------------------------------------------

## 2. Confirmed decisions from the owner

These are confirmed requirements. Do not silently change them.

  -----------------------------------------------------------------------
  Area                                Decision
  ----------------------------------- -----------------------------------
  Public site languages               Uzbek + Russian

  Default language                    Uzbek

  Language switching                  User switches using a button

  Admin language                      Russian only

  Courses/tariffs                     Show tariffs/plans without prices

  Admin users                         Option B from the earlier
                                      questionnaire --- see note below

  Admin-managed content               All previously listed content
                                      except social networks, SEO
                                      settings, and texts for every site
                                      section

  Hide individual items               No; the owner selected "No" for a
                                      separate hide/show feature

  Application fields                  Name and phone

  Application handling                Save to database and send Telegram
                                      notification

  Telegram recipient                  One Telegram group

  Application list in admin           Creation date, name, phone,
                                      application source

  File storage                        MinIO locally; S3-compatible
                                      storage in production

  Upload validation                   All four validation measures from
                                      the earlier questionnaire

  Main stack                          Confirmed; see Technical stack

  Docker                              Entire backend via Docker Compose

  Deployment                          Not decided yet

  Spam protection                     Keep it simple; choose a
                                      lightweight approach

  Tests                               Basic API tests only

  GitHub Actions                      Not for now

  Git workflow                        Work on `anzor`; after checks,
                                      merge into `main`

  Collaboration workflow              Assistant gives a task and
                                      code/instructions; owner makes
                                      changes locally; assistant says
                                      when to commit; assistant then
                                      checks the changes from Git

  Implementation priority             Speed of implementation
  -----------------------------------------------------------------------

### Clarifications still needed

The owner's answers to some numbered questionnaire items were blank or
depended on option labels that are not repeated here. Do not invent the
missing selections.

1.  **Homepage sections:** the selection for questionnaire item 4 was
    blank. The broader project context lists Hero, About, Courses,
    Teachers, Certificates/results, Achievements, Application form,
    Interior gallery, Events, Contacts/map, FAQ, Reviews, and Blog as
    possible sections. Confirm which ones are required for the current
    version.
2.  **Admin-managed content:** questionnaire item 8 says "everything
    except social networks, SEO settings, and texts of all site
    sections." Confirm the exact remaining content types if needed.
3.  **Admin users:** answer "B" was selected for item 7, but the option
    labels are not preserved in the answer. Confirm the intended
    admin-user arrangement before implementing permissions or roles.
4.  **Upload validation:** "all four points" was selected. The original
    four options were file format, file size, image resolution, and
    genuine-image validation. Confirm exact limits and accepted formats
    before implementing strict validation.
5.  **Simple spam protection:** choose a low-complexity solution. A
    reasonable starting point is DRF throttling plus a honeypot field;
    add a minimum form-completion time only if it remains simple. Do not
    add CAPTCHA without approval.
6.  **Tariffs:** the owner said to place tariffs/plans on the site
    without prices. Clarify the tariff fields and whether these are
    separate from the course list before designing models.

------------------------------------------------------------------------

## 3. Technical stack

Confirmed or documented stack:

### Backend

-   Python
-   Django
-   Django REST Framework
-   Django Jazzmin for the admin interface
-   `drf-spectacular` for OpenAPI schema and API documentation
-   SQLite for local development unless the owner confirms a different
    local setup
-   PostgreSQL intended for production
-   `django-storages` with MinIO locally and an S3-compatible service in
    production
-   `pyTelegramBotAPI` for Telegram notifications

### Frontend (later phase)

-   Next.js
-   TypeScript
-   Tailwind CSS

Do not start frontend implementation until the backend/API phase is
stable and the owner asks to proceed.

### Docker

The owner selected Docker Compose for the entire backend. The existing
Compose file only covered MinIO at the time of the audit, so the Compose
setup will need to be expanded to cover the agreed backend services.
Final production deployment details are not decided.

------------------------------------------------------------------------

## 4. Repository structure known from the audit

Repository: `hissokababy/proj_fast_v2`\
Branch: `anzor`

Known structure (simplified):

``` text
proj_fast_v2/
├── .gitignore
├── docs/
│   ├── PROJECT_CONTEXT.md
│   ├── PROJECT_STATUS.md
│   └── ТЗ проекта.doc
└── backend/
    ├── config/
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    ├── website/
    │   ├── migrations/
    │   ├── views/
    │   ├── services/
    │   ├── models.py
    │   ├── serializers.py
    │   ├── admin.py
    │   ├── urls.py
    │   └── tests.py
    ├── requirements.txt
    ├── manage.py
    └── docker-compose.yml
```

This is a simplified structure based on the repository inspection, not a
guarantee that no other files exist. Check the current Git tree before
relying on exact paths.

------------------------------------------------------------------------

## 5. Current data models

At the time of the audit, the `website` app contained:

-   `Teacher`
-   `Certificate`
-   `Event`
-   `InteriorPhoto`
-   `Application`
-   `OtherPhoto`

`Application` currently had only:

-   `full_name`
-   `phone`
-   `created_at`

The owner wants the admin application list to also show the application
source. The implementation must decide how to capture and store this
source; do not fabricate a source value when it is unavailable.

The owner wants courses/tariffs displayed without prices. The precise
model structure for courses and tariffs still needs confirmation.

------------------------------------------------------------------------

## 6. API endpoints found in the project specification

The project specification lists these endpoints:

  Method   Endpoint                      Purpose
  -------- ----------------------------- -----------------------------------
  GET      `/api/teachers/`              Public teacher list
  GET      `/api/certificates/`          Public certificate list
  GET      `/api/events/`                Public event list
  GET      `/api/interiors/`             Public interior-photo list
  GET      `/api/other-photos/<key>/`    Retrieve an image/resource by key
  POST     `/api/applications/create/`   Submit an application
  GET      `/api/schema/`                OpenAPI schema
  GET      `/api/docs/`                  Swagger documentation
  GET      `/api/redoc/`                 ReDoc documentation

Check the current URL configuration before changing or documenting
endpoint behaviour.

------------------------------------------------------------------------

## 7. Audit findings from the previous repository review

These findings were observed during a code review. They may have changed
since then; re-check the current branch before fixing anything.

### High-priority items

1.  **Telegram application notifications were not implemented.**\
    The application endpoint saved through the serializer, but there was
    no complete Telegram notification workflow.

2.  **Application spam protection was missing.**\
    The owner prefers a simple solution rather than a complex CAPTCHA
    setup.

3.  **Automated tests were almost empty.**\
    The owner selected basic API tests, not a comprehensive test suite.

4.  **`OtherPhoto.image` used `FileField`.**\
    Earlier migration history showed it had been an `ImageField`; the
    owner now requires all four upload-validation measures. Reconcile
    model and migrations carefully.

5.  **Production database configuration was incomplete.**\
    SQLite was configured directly. PostgreSQL is intended for
    production.

### Other code/configuration findings

-   `certificate_service.py` had an incorrect queryset return type
    annotation: it returned certificates but was annotated as teachers.
-   `event_service.py` had the same kind of incorrect return type
    annotation.
-   `.gitignore` ignored `.env` and `.env.*`, which also risks ignoring
    `.env.example` unless explicitly unignored.
-   `.vscode/settings.json` appeared in the Git tree even though
    `.vscode/` was listed in `.gitignore`.
-   The existing `docker-compose.yml` ran MinIO only, not the full
    backend stack.
-   Production-oriented settings such as secure cookies, trusted CSRF
    origins, and static/media configuration needed review.
-   The dependency file was a large frozen requirements list; review
    only as needed and avoid unnecessary dependency churn.
-   Migration history included an abandoned tariff model (`0006_tariff`,
    followed by `0007_delete_tariff`).

### Security note

During the previous review, `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, and
MinIO credentials were found to be read from environment variables. Do
not claim they were hardcoded unless a fresh inspection proves that.
Never print or expose secret values.

------------------------------------------------------------------------

## 8. Application form and Telegram workflow

Expected flow:

1.  A visitor submits their name and phone number.
2.  Backend validates the submitted data.
3.  Backend saves the application in the database.
4.  Backend sends a notification to the configured Telegram group.
5.  If Telegram is unavailable, the saved application must remain in the
    database.

The Telegram failure must not cause the application record to be lost.
The notification process should log failures safely and allow a
practical retry mechanism if needed.

The admin application list should show:

-   Creation date
-   Name
-   Phone
-   Application source

Do not log full phone numbers or other unnecessary personal data.

------------------------------------------------------------------------

## 9. File and image handling

Storage direction:

-   Local development: MinIO.
-   Production: S3-compatible storage.
-   Backend is expected to use `django-storages`.

The owner selected all four validation categories:

1.  Allowed file formats
2.  Maximum file size
3.  Image dimensions/resolution
4.  Validation that the upload is a genuine/valid image

Exact allowed formats, size limits, and resolution limits have not yet
been confirmed. Use conservative, clearly documented defaults only after
explaining them to the owner.

------------------------------------------------------------------------

## 10. Development and Git workflow

Follow this workflow strictly:

1.  Inspect the current repository and branch before proposing code
    changes.
2.  Give the owner a small, clear task with exact file paths and
    code/instructions.
3.  The owner applies the changes locally.
4.  Review the changes from GitHub/Git once the owner says they are
    ready.
5.  Run or request the relevant checks.
6.  Tell the owner explicitly when the changes are ready to commit.
7.  Work on branch `anzor`.
8.  Merge into `main` only after the owner has reviewed and approved the
    checked changes.

The owner prefers to make the local edits personally. Do not assume
permission to push, merge, or change repository files directly.

If GitHub integration cannot write to the repository, state that clearly
and continue with local instructions. Never claim a change was committed
or pushed unless the tool confirms it.

------------------------------------------------------------------------

## 11. Working principles for ChatGPT

When a new conversation starts:

1.  Read this file first.
2.  Inspect the current Git branch and latest repository contents before
    relying on old audit findings.
3.  Treat the owner's confirmed decisions in Section 2 as requirements.
4.  Treat items in "Clarifications still needed" as unresolved, not as
    permission to make assumptions.
5.  Keep tasks small and implementation-focused.
6.  Prioritise speed, but do not sacrifice data integrity or basic
    security.
7.  Avoid unnecessary architecture, dependencies, abstractions, or
    features.
8.  Do not start the frontend until the backend/API is stable and the
    owner approves that phase.
9.  Do not add prices to tariffs.
10. Keep Django Admin in Russian; the public website is Uzbek by default
    with a Russian language option.
11. Do not expose secrets, credentials, tokens, or personal data.
12. After each task, explain what changed, how to test it, and whether
    it is ready to commit.

------------------------------------------------------------------------

## 12. Immediate next steps

Recommended order, subject to the owner confirming the remaining
details:

1.  Re-check the latest `anzor` branch and repository tree.
2.  Resolve the outstanding questions about sections, admin users,
    courses/tariffs, and upload limits.
3.  Agree on the minimal data model for courses/tariffs and application
    source.
4.  Fix the small service typing errors and `.gitignore` example-file
    rule.
5.  Implement the application workflow and Telegram group notification.
6.  Add simple spam protection.
7.  Correct image field/validation and storage configuration.
8.  Expand Docker Compose to run the agreed backend services.
9.  Add basic API tests and update setup documentation.
10. Verify the backend before beginning frontend work.

**Important:** This document is a project handoff, not proof that the
repository currently matches every item. Always verify the live branch
before editing.
