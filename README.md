# Django Metar App

This Django app provides endpoints for retrieving Metar information.

## API Endpoints

### Pong

Check if the server is running.

- **URL:** `/metar/ping`
- **Method:** GET
- **Handler:** `pong`
- **Description:** Returns a 'pong' response.

### Get Weather Report

Fetch weather report information.

- **URL:** `/metar/info/`
- **Method:** GET
- **Handler:** `get_weather_report`
- **Description:** Retrieves weather report data.

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/django-metar-app.git
```

```bash
pip install -r requirements.txt
```

```bash
python manage.py runserver
```


