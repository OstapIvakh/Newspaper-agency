# Newspaper-agency
 
Django project for online journal.

## Installation

```shell
git clone https://github.com/OstapIvakh/Newspaper-agency.git
cd newspaper-agency
python3 -m venv venv
source venv/bin/activate
pip install requirements.txt
python manage.py migrate
python manage.py manage.py loaddata db.json
python manage.py runserver
```

### Test User

```
username: admin
password: admin
```

## DB structure