FROM python:3.8-buster as prod-image

RUN pip install -U pip pipenv

WORKDIR /opt/toy_robot

COPY Pipfile* ./

RUN pipenv install --deploy --system

COPY . .

ENV APP_HOME='/opt/toy_robot'
ENV APP_BIN="${APP_HOME}/toy_robot/bin"
ENV PATH="${APP_HOME}:${APP_BIN}:${PATH}"

ENTRYPOINT ["toy-robot"]


FROM prod-image as test

RUN pipenv install -d --system

ENTRYPOINT ["pytest"]
