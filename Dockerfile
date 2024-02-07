FROM python:3.8

WORKDIR /app

COPY main.py .
COPY mylib ./mylib
COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8080

CMD ["python", "main.py"]
