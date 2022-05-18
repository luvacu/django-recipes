FROM python:3.9-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

ARG DEV_BUILD=false
COPY ./requirements*.txt .
RUN if [ "$DEV_BUILD" = "true" ]; then \
      pip install -r /app/requirements-dev.txt; \
    else \
      pip install -r /app/requirements.txt; \
    fi

COPY . .
