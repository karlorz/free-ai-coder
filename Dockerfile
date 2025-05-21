FROM python:3.11-slim

WORKDIR /app

# Copy all necessary Python files
COPY pyproject.toml uv.lock ./
COPY app.py ./
COPY llm_client_openai.py ./
COPY llm_client_deepseek.py ./
COPY kernel_gateway_client.py ./
COPY assets/ ./assets/

RUN pip install uv
RUN uv sync --no-dev --frozen

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["uv", "run", "streamlit", "run", "app.py", "--server.port=8000", "--server.address=0.0.0.0"]
