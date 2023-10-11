# Newspaper-agency
 
Django project for managing online journal.

## Check it out!
[Newspaper agency project deployed to Render](https://newspaper-agency-geiu.onrender.com/)

## Installation

Python3 must be already installed

For Windows:
```shell
git clone https://github.com/OstapIvakh/Newspaper-agency.git
cd newspaper_agency
python venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata db.json
python manage.py runserver
```

For Mac (and Linux):
```shell
git clone https://github.com/OstapIvakh/Newspaper-agency.git
cd newspaper_agency
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata db.json
python manage.py runserver
```

### Test User

```
username: admin
password: admin
```

## Features

- Managing redactors and topics and 
- Authentication for created Redactors
- Create, read, edit, delete newspapers
- Create, edit, delete redactors
- Create, edit, delete topics

## DB structure
![image](https://github.com/OstapIvakh/Newspaper-agency/assets/137914345/66935575-5dae-4693-8bde-05d8b0e65032)

## Home page
![image](https://github.com/OstapIvakh/Newspaper-agency/assets/137914345/124875e8-997e-414d-953f-65438b527842)

## Redactors list
![image](https://github.com/OstapIvakh/Newspaper-agency/assets/137914345/e147721f-0481-4d0b-9bb2-c10cbc4fa090)

## Topics list
![image](https://github.com/OstapIvakh/Newspaper-agency/assets/137914345/ca7bc2e5-0dde-4123-8535-7efb40e6a850)

## Newspapers list
![image](https://github.com/OstapIvakh/Newspaper-agency/assets/137914345/b4a8c0e6-fcbd-4f8e-8046-7ebddc6b961e)
