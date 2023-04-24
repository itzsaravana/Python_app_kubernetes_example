FROM python:3.8-alpine as base
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN pip install --upgrade pip
COPY . .
RUN pip install --no-cache-dir -r ./requirements.txt
ENV PYTHONPATH /app
CMD ["python","-u","reader.py"]
