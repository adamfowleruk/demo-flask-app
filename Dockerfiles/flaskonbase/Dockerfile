ARG BASE_IMAGE=harbor.shared.12factor.xyz/adamf/python-flask-base-image:v1
ARG APP_FOLDER=flask-time-api

FROM $BASE_IMAGE
WORKDIR /usr/src/app
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

# Copy actual app over
COPY flask-time-api/* .

# This will be done in the execution image Dockerfile only:-
CMD ["flask","run","--no-debugger"]