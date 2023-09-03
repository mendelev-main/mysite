FROM python:3.11

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN pip3 install poetry

COPY ./poetry.lock ./pyproject.toml ./
RUN poetry install

COPY ./api ./api
COPY ./blog ./blog
COPY ./mysite ./mysite
COPY ./overrides ./overrides
COPY ./polls ./polls
COPY ./static ./static
COPY ./templates ./templates
COPY manage.py ./

ENTRYPOINT ["poetry", "run"]


