FROM python:3.10.9 AS base

COPY requirements.txt ./
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

# ---- App ----
FROM base as app
WORKDIR /app

COPY . ./rest_api

WORKDIR /app/rest_api

CMD export FLASK_APP=app
EXPOSE 5000

