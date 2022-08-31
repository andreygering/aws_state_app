ARG PYTHON_VERSION=3.10
FROM python:${PYTHON_VERSION} as builder 
ENV PYTHONUNBUFFERED=1 
WORKDIR /usr/src/app/
COPY * /usr/src/app/
COPY requirements.txt /wheels/
WORKDIR /wheels
RUN pip install pip --upgrade && pip wheel -r requirements.txt && ls 



# Runs Pylint Tests
FROM eeacms/pylint:latest as linting
WORKDIR /code
COPY --from=builder /usr/src/app/aws_instances_status.py  /code/aws_instances_status.py
RUN ["pylint",  "--disable=all","./aws_instances_status.py"]


# Runs Unit Tests
# Phase IV
FROM python:${PYTHON_VERSION} as unit-tests
WORKDIR /usr/src/app
# Copy all packages instead of rerunning pip install
COPY --from=builder /wheels /wheels
RUN     pip install -r /wheels/requirements.txt \
                      -f /wheels \
       && rm -rf /wheels \
       && rm -rf /root/.cache/pip/* 

COPY --from=builder /usr/src/app/ ./
RUN ["python", "unittest_aws_instances_status.py"]

# Starts and Serves Web Page
# Phase VI
FROM python:${PYTHON_VERSION}-slim as serve
WORKDIR /usr/src/app
# Copy all packages instead of rerunning pip install
COPY --from=builder /wheels /wheels
RUN     pip install -r /wheels/requirements.txt \
                      -f /wheels \
       && rm -rf /wheels \
       && rm -rf /root/.cache/pip/* 

COPY --from=builder /usr/src/app/*.py ./
ENTRYPOINT ["python", "-u", "aws_instances_status.py"]
CMD ["python", "-u", "aws_instances_status.py"]