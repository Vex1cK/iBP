FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y ffmpeg \
&& rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./ai_models ./ai_models

COPY ./pyproject.toml ./pyproject.toml
COPY ./entrypoint.sh /app/entrypoint.sh
COPY ./.env ./.env
COPY ./tests ./tests
COPY ./src ./src

COPY ./checksums.txt ./checksums.txt

EXPOSE 8000

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
