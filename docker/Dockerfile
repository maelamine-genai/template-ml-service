FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml .
COPY src ./src
RUN python -m pip install -U pip && \
    pip install --no-cache-dir .
CMD ["uvicorn", "src.<pkg_name>.app:app", "--host", "0.0.0.0", "--port", "8080"]
