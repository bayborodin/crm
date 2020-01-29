# Django CRM
CRM built with Django 2.0

## Тесты
```bash
coverage erase  # Remove any coverage data from previous runs
coverage run manage.py test  # Run the full test suite
coverage run manage.py test offerings -v 2
coverage report --include=./*py
coverage html --include=./*py

## Акт обнаружения брака
/defections/6fe2ca63-128c-4f14-bd95-229eb3c9bc2b
