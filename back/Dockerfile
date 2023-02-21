FROM python:3.9-slim
WORKDIR /usr/app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

VOLUME /usr/app/models

EXPOSE 5000
CMD ["python","app.py"]