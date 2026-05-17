FROM python:3.11.10-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV BOOTCAMP_HOST=0.0.0.0
ENV BOOTCAMP_PORT=8000
WORKDIR /workspace
RUN addgroup --system appuser && adduser --system --ingroup appuser appuser
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY . .
RUN mkdir -p /workspace/app/saved_notebooks && chown -R appuser:appuser /workspace
USER appuser
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 CMD python -c "from urllib.request import urlopen; urlopen('http://127.0.0.1:8000/health').read()"
CMD ["python", "-m", "app.app"]
