FROM python:3.12-alpine

WORKDIR /star-burger

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt backend/requirements.txt

RUN pip3 install --upgrade pip
RUN pip install -r backend/requirements.txt

COPY . .
