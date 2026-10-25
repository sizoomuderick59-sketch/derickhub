# AgriTrack for Maize AI

AI-assisted maize crop advisory and plant-disease detection for farmers in Uganda, with an
administrator console for monitoring farmers, reports and communication.

## Quick start

```bash
python -m venv venv
venv\Scripts\activate            # Windows   (Linux/macOS: source venv/bin/activate)
pip install -r requirements.txt
python scripts/seed_database.py  # creates tables, the admin account and reference data
python run.py                    # http://127.0.0.1:5000
```

`run.py` (and therefore `gunicorn run:app` in Docker) creates any missing tables on start-up. It only
*adds* tables, it never alters or drops existing ones, so upgrading an existing database is safe.
Back up `instance/` before upgrading anyway.

## Who sees what

| Visitor | Lands on | Can open |
|---|---|---|
| Not logged in | Home / Login / Register | public pages only |
| **Farmer** | Farmer Portal | portal, AI Advisor, Diagnose Plant, My History, Tips, Notifications |
| **Admin** | Admin dashboard | everything above for preview **plus** all `/admin/...` pages |

Admin pages are protected on the server. A farmer who types an admin address is sent back to their
portal; someone not logged in is sent to the login page. An admin can look at the farmer home, login
and registration pages (a dark bar offers *Back to admin dashboard*) without being logged out.

## What the administrator can do

* **Dashboard**: platform totals, this month's engagement percentages, recent sign-ins, charts.
* **Monthly report** (`/admin/monthly-report`): % of farmers who logged in, ran a diagnosis, asked the
  AI advisor and were active overall; month-over-month change, 12-month trend, per-farmer table,
  filters, CSV export and print/PDF. Weekly report is still available.
* **Farmers** (`/admin/users`): search, view details and inquiries, **edit** account and farm details,
  activate/deactivate, **delete** (removes the farmer, their diagnoses, questions, photos, login
  history and notifications, after a confirmation).
* **Notifications** (`/admin/notifications`): send a message to one farmer or to all farmers, see how
  many have read it, delete it.
* Disease catalog, knowledge base, model registry and audit logs.

## What the farmer gets

* A portal showing their registered farm details (editable), scan buttons and a question box.
* **Bell icon** in the navigation bar with an unread count and the latest messages; a full
  Notifications page with mark-as-read.
* Diagnose Plant, AI Advisor and **My History**: every diagnosis and conversation is saved in the
  account so it can be reviewed later.

## Configuration (`.env`)

| Variable | Default | Meaning |
|---|---|---|
| `REPORT_UTC_OFFSET_HOURS` | `3` | Local time used to bucket days/months in reports (Uganda = UTC+3) |
| `UPLOAD_FOLDER` | `app/static/uploads/diagnoses` | Where diagnosis photos are stored |
| `PUBLIC_BASE_URL` | unset | Public app URL used in password recovery links |
| `MAIL_SERVER` / `MAIL_PORT` | unset / `587` | SMTP server settings for recovery email |
| `MAIL_USERNAME` / `MAIL_PASSWORD` | unset | Optional SMTP authentication credentials |
| `MAIL_DEFAULT_SENDER` | unset | Verified sender address required for recovery email |
| `PASSWORD_RESET_MAX_AGE` | `3600` | Reset-link lifetime in seconds |

Password recovery is available from the login page. Configure SMTP and `PUBLIC_BASE_URL` in `.env`
to deliver one-hour, single-use reset links to farmers.

## Tests

```bash
pytest
```

Covers authentication, login history, admin access control, the monthly report, farmer edit/delete,
notifications and the report calculations.

## Brand assets

`brand/` holds the logo (emblem, horizontal, stacked and reversed versions), app icons, the login
background and `brand-showcase.png`. The website uses the copies in `app/static/img/`.

## Interactive demo

`demo/agritrack-live-preview.html` is a self-contained front-end preview (sample data, runs in any
browser) of the login, admin dashboard, farmer portal, notifications and reports. It is for
demonstrations only and is not connected to the real database.
