FROM python:3.8-slim
ENV PYTHONUNBUFFERED=1
RUN mkdir /app
WORKDIR /app

RUN apt-get update -y && apt-get install -y g++

ADD poetry.lock /app/
ADD pyproject.toml /app/

RUN pip3 install --upgrade pip
RUN pip3 install poetry
RUN poetry config virtualenvs.create false --local
RUN poetry install --no-dev
ADD . /app/
ENV PYTHONPATH=/app

CMD ["python", "main.py"]
EXPOSE 9999