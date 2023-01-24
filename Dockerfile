FROM python:3.11.1
ENV PYTHONUNBUFFERED 1
# App setup
ADD . /code
WORKDIR /code
# Requirements installation
RUN pip install -r requirements.txt
