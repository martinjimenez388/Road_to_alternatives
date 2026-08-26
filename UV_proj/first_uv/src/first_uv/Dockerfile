FROM agrigorev/zoomcamp-model:2025

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --locked --no-dev --no-install-project

COPY src/first_uv/load_model_fastapi.py src/first_uv/pipeline_v1.bin ./

EXPOSE 9696

ENTRYPOINT ["uv", "run", "--no-project", "uvicorn", "load_model_fastapi:app", "--host", "0.0.0.0", "--port", "9696"]