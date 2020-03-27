FROM python:3.8-alpine
MAINTAINER Benning

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev libffi-dev \
    cairo-dev pango-dev gdk-pixbuf-dev fontconfig font-noto-thai
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev python3-dev fontconfig font-noto-thai
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY . .

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser -D user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web

USER user