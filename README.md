# GR€€NV€STM€NT$

A personal development fork of the Budget Busters hackathon project, exploring a future green-investment direction.

**Python · Django**

[Getting started](#getting-started) · [Data model](#entity-relationship-diagram) · [Repository guide](#repository-guide) · [Checks](#checks-and-review) · [Credits](#credits-and-reuse)

## What you can explore

- The inherited Budget Busters account and budgeting application.
- Django forms, categories and financial-record models.
- The original hackathon design and testing record.

> **Project notes:** The green-investment concept describes the intended direction of this fork. The committed application is the inherited budgeting project; it does not establish a completed investment service.

## Entity relationship diagram

The budgeting screens keep a total budget and a map of expenses in the Django session. Each expense entry is a running total keyed by the submitted category display name. The form gets its category options from the database. The name is a text key in session data, so the association has no foreign-key constraint. The Django `Budget` model also defines a JSON `expenses` field. [Category and budget models](accounts/models.py) · [Budget form](templates/accounts/profile.html) · [Budget views](accounts/views.py) · [Calculated totals](accounts/contexts.py)

```mermaid
erDiagram
    accTitle: Budget session, expense totals and category options
    accDescr: Each budget session stores an expense total per submitted category name. The category table supplies the form options.
    "Budget Session" ||--o{ "Expense Total" : stores
    Category }o..o{ "Expense Total" : "shares label"

    "Budget Session" {
        int total_budget
        map expenses
    }
    "Expense Total" {
        string category_name
        int amount
    }
    Category {
        string name
        string friendly_name
    }
```

## Getting started

Requires Git, Python, pip and a virtual environment. Dependency pins in older projects may need a compatible Python environment; this README does not upgrade them.

```bash
git clone https://github.com/SamOBrienOlinger/GR-NV-STM-NT-.git
cd GR-NV-STM-NT-
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, activate the environment with `.venv\Scripts\Activate.ps1` instead.

After resolving the project notes and configuring the local environment, use:

```bash
python manage.py check
python manage.py migrate
python manage.py runserver
```

Open [localhost:8000](http://localhost:8000). Stop the server with **Ctrl+C**. Use `python manage.py createsuperuser` in the same project directory if you need access to Django admin.

## Configuration

Settings are defined in [BudgetBusters/settings.py](BudgetBusters/settings.py). Set the values used by your chosen local configuration before running Django. A `.env` file is only read when the project explicitly loads it; most of these projects read the process environment or an optional `env.py`.

| Variable | Purpose |
| --- | --- |
| `DATABASE_URL` | Connection URL for your own development database. Required where settings parse it without a fallback. |
| `DEV` | Development-mode switch. Inspect whether the settings test its presence or its value. |
| `SECRET_KEY` | Django signing key. Use a locally generated value and keep it out of Git. |

Use a disposable development database for migrations and tests. Keep service credentials and local configuration out of commits.

## Repository guide

| Path | Purpose |
| --- | --- |
| [requirements.txt](requirements.txt) | Python dependency versions |
| [manage.py](manage.py) | Django management commands |
| [BudgetBusters/settings.py](BudgetBusters/settings.py) | Django configuration |
| [templates/](templates/) | Server-rendered page templates |
| [docs/](docs/) | Supporting project documentation |

## Checks and review

From the directory containing `manage.py`, run `python manage.py check` and `python manage.py test` after configuring an isolated development database. Inspect the test modules: scaffold `tests.py` files may contain no actual tests.

Generate fresh results from the revision you are working on; historical test reports describe earlier runs.

## Deployment

Hosting entry points are recorded in [Procfile](Procfile). Configure the runtime, database, allowed origins and static/media handling for the chosen host. Historical deployment records may describe services that are no longer available.

## Credits and reuse

Forked from [rstan-dev/jan24-hackathon](https://github.com/rstan-dev/jan24-hackathon). Original authorship and contributor credits remain with that project.

Design decisions, original feature notes, historical testing evidence and detailed acknowledgements remain available in the preserved project record:

- [README.md · original project record](https://github.com/SamOBrienOlinger/GR-NV-STM-NT-/blob/15028381e422106c411249475758219800394abc/README.md)

Learning resources and starter material: [Code Institute](https://codeinstitute.net/).

No repository-level licence file is present in this snapshot. This README does not grant additional reuse permissions. Check with the relevant rights holders before reusing code, written content or assets.

## Support

Repository maintained in [Sam O’Brien-Olinger’s GitHub account](https://github.com/SamOBrienOlinger). Use the [repository’s pull requests](https://github.com/SamOBrienOlinger/GR-NV-STM-NT-/pulls) to propose a documented change, or follow the upstream project’s contribution process.

[Back to top](#grnvstmnt)
