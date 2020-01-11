# Django CRM
CRM built with Django 2.0

## Тесты
```bash
coverage erase  # Remove any coverage data from previous runs
coverage run manage.py test  # Run the full test suite
coverage run manage.py test offerings -v 2
coverage report --include=./*py
coverage html --include=./*py
