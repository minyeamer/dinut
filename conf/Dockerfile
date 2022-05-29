FROM python:3.8.8

WORKDIR /home/

RUN echo "refresh"

ADD https://api.github.com/repos/minyeamer/dinut/git/refs/heads/main version.json
RUN git clone https://github.com/minyeamer/dinut.git

WORKDIR /home/dinut/

RUN apt-get update && pip install --upgrade pip

RUN apt-get update && pip install --no-cache-dir -r requirements.txt

RUN apt-get update && pip install --no-cache-dir gunicorn

RUN apt-get update && pip install --no-cache-dir mysqlclient

RUN apt-get update && apt install -y libgl1-mesa-glx

EXPOSE 8000

CMD ["bash", "-c", \
    "python manage.py collectstatic --noinput --settings=dinut.settings.deploy && \
    python manage.py migrate --settings=dinut.settings.deploy && \
    python script.py --settings=dinut.settings.deploy && \
    gunicorn dinut.wsgi --env DJANGO_SETTINGS_MODULE=dinut.settings.deploy --bind 0.0.0.0:8000"]
