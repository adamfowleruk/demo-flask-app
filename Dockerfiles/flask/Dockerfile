# WARNING - Do not use. Use demo-base-images/flaskbase then flaskonbase from this repo instead

# Args
ARG BASE_IMAGE=python:3.7-slim
# OR myorg/myapp:latest if overriding via ARGs in Docker build

# Phase 1 - Build
FROM python:3.7-slim AS compile-image
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential gcc && \
    apt-get clean

RUN python -m venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt

#COPY setup.py .
COPY flask-time-api .
#RUN pip -v install .

# Phase 2 - Run
FROM $BASE_IMAGE as run-image
COPY --from=compile-image /opt/venv /opt/venv
COPY --from=compile-image /usr/src/app /usr/src/app
WORKDIR /usr/src/app
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"
CMD ["python3","app.py"]