FROM python:3.9

WORKDIR  /django_admin

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

#WORKDIR /django_admin/test_project

#CMD gunicorn test_project.wsgi:application --bind 0.0.0.0:$PORT
#CMD python3 manage.py runserver