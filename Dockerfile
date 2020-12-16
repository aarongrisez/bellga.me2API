FROM python:3.8.1
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
RUN apt-get update && apt-get install -y git-all libsndfile1
WORKDIR /src
COPY ./pyproject.toml .
COPY ./poetry.lock .
ENV PATH="/root/.poetry/bin:${PATH}"
RUN poetry install
EXPOSE 80
CMD ["poetry", "run", "uvicorn", "api.main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]