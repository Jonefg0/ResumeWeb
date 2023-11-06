# Show your resume as a web page

This website was created with django

# How to deploy this website locally

### Here are the requirements for implementation:

| Name | Version |
|------|----------|
|Python| 3.11 |
|pipenv| * |
|Django| 4.2 |

### First, we need to create a python environment with:

`pipenv install django django-ckeditor Pillow pylint pylint-django`

Access to pipenv environment with:
`pipenv shell`

### Now it is necesary to create superuser to access the admin panel and make database migrations:
Open your terminal, navigate to the project root folder, and then run the following commands: 
* Create super user:
  `python manage.py createsuperuser`
* Make migrations:
  `python manage.py makemigrations`
  `python manage.py migrate`
This will create a sqlite3 file in your folder

### Run Server
To deploy your application, execute the following command
`python manage.py runserver`
Access from your browser at http://127.0.0.1:8000/







  








