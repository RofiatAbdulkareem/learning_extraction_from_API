FROM python:3.12.10-alpine3.20
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python","extract.py"]