FROM python:3.9-alpine
WORKDIR /api/app

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
RUN apk add --no-cache git build-base bash curl openssl sudo openblas-dev ffmpeg sox libffi-dev libsndfile-dev postgresql-dev 
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./app /api/app

EXPOSE 9002

CMD ["flask","run","--host","0.0.0.0","--port","9002"]
