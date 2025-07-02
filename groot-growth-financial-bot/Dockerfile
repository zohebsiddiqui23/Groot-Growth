FROM python:3.12-slim

WORKDIR /app

# Install your dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

# ─── Create & chmod the two runtime dirs ────────────────────────────────
# /cache — for huggingface models, datasets, metrics
# /app/.streamlit — for Streamlit’s config
RUN mkdir -p /cache /app/.streamlit \
 && chmod -R 777 /cache /app/.streamlit

# ─── Point all relevant env vars at those dirs ──────────────────────────
ENV HF_HOME=/cache \
    TRANSFORMERS_CACHE=/cache \
    HF_DATASETS_CACHE=/cache \
    HF_METRICS_CACHE=/cache \
    STREAMLIT_CONFIG_DIR=/app/.streamlit

# Copy in your app
COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", \
     "--server.port", "8501", \
     "--server.address", "0.0.0.0"]
