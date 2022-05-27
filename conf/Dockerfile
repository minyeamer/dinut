FROM python:3.8.8

WORKDIR /home/

RUN echo "refresh"

RUN git clone https://github.com/minyeamer/dinut.git

WORKDIR /home/dinut/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c",
    "python manage.py collectstatic --noinput --settings=dinut.settings.deploy &&
    python manage.py migrate --settings=dinut.settings.deploy &&
    python script.py &&
    gunicorn dinut.wsgi --env DJANGO_SETTINGS_MODULE=dinut.settings.deploy --bind 0.0.0.0:8000"]
