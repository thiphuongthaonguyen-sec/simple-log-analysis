FROM python:3.11-slim

RUN useradd -m appuser
WORKDIR /app

COPY logs ./logs
COPY log_analysis.py .

RUN chown -R appuser:appuser /app
USER appuser

CMD ["python", "log_analysis.py"]
