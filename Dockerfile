FROM python:3.7.3

COPY ./ ./opt/djangoNews
WORKDIR /opt/djangoNews

RUN pip install -r requirements.txt
