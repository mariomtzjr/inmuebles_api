FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /code

WORKDIR /code

COPY . /code/

RUN apk update \
    && apk add build-base

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiamos el proyecto
COPY . /code/

EXPOSE 9001

CMD ["python", "code/app.py"]
