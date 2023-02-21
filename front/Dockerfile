FROM python:3.9-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .
COPY predict.py .
COPY search.py .
COPY data /app/data

ENV PYTHONPATH "${PYTHONPATH}:/app/"

EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501"] 