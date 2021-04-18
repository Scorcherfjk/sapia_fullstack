FROM python:3.6.8-alpine3.9

LABEL MAINTAINER="Javier De Freitas <franjavikale@gmail.com>"

ENV GROUP_ID=1000 \
    USER_ID=1000 
    # MONGODB_DATABASE=sapia \
    # MONGODB_USERNAME=flaskuser \
    # MONGODB_PASSWORD=your_mongodb_password \
    # MONGODB_HOSTNAME=mongodb

RUN apk add --no-cache --virtual .pynacl_deps build-base libffi-dev

WORKDIR /var/www/

ADD ./requirements.txt /var/www/requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

ADD . /var/www/


RUN addgroup -g $GROUP_ID www
RUN adduser -D -u $USER_ID -G www www -s /bin/sh

USER www

EXPOSE 5000

CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi:app"]