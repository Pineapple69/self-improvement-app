FROM python:3.12-slim

RUN apt-get -q -y update
RUN apt-get install -y gcc

WORKDIR /app

COPY pyproject.toml ./
COPY poetry.lock ./

RUN pip3 install --upgrade pip && pip3 install poetry==1.8.3 && poetry config virtualenvs.create false  && poetry install --no-root

COPY . ./

EXPOSE 5005
CMD ["flask", "--debug", "run", "-h", "0.0.0.0",  "-p", "8000"]