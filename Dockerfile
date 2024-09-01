FROM python:3.12-slim

RUN pip install poetry

RUN mkdir -p /app

COPY ./main.py /app/
COPY MlopsArchi/ /app/MlopsArchi/
COPY test/ /app/test/
COPY pyproject.toml poetry.lock* /app/

WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"

RUN poetry install

CMD ["poetry", "run", "python", "main.py"]