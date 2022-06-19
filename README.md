# Demo Flask App

Sample flask app exposing two endpoints to show server time and downstream database time for an upstream caller.

### Prerequisites

* Python 3
* docker
* postgresql

## Usage

### Building the app locally 

    python3 -m venv .venv3
    source .venv3/bin/activate
    pip3 install -r requirements.txt

### Running the app locally

    PGHOST='localhost' PGUSER=test PGDATABASE=test PGPASSWORD=test FLASK_APP=app.py python -m flask run --host=0.0.0.0 --port=5000

### Buildpacks to build the OCI image

Use following commands to build the image.

    pack build demo-flask-app --builder paketobuildpacks/builder:base

_NOTE: Assuming [buildpacks](https://buildpacks.io/) is installed locally_

### Running the built container image

    docker run -e PGHOST='localhost' -e PGUSER=test -e PGDATABASE=test -e PGPASSWORD=test -e PORT=5000 -p5000:5000 demo-flask-app:latest

_NOTE: Assuming [docker](https://www.docker.com/) is installed and PostgreSQL is accessible with passed in 
environment variables_