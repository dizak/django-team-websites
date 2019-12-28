# django team websites

Lab website builder created with [Django Project](https://docs.djangoproject.com/)

## Development

1. Install dependencies listed in the ```requirements.txt```:

```bash
pip install -r djago_team_websites/requirements.txt
```

1. Initialize database using fixtures:

    ```bash
    python manage.py makemigrations lab_website

    python manage.py migrate lab_website

    python manage.py loaddata lab_website/fixtures/lab_test_data.json
    ```

1. Go to djago_team_websites and run ```python manage runserver```

## Deployment

Docker files were copied from the flascholarly project, not functional yet
