FROM ghcr.io/astral-sh/uv:python3.12-bookworm

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync

COPY . .

EXPOSE 8000

CMD ["./bin/start.sh"]


