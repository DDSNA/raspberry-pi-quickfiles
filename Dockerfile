FROM python:latest

RUN pip install pandas

WORKDIR /app

COPY pipeline.py pipeline.py

ENTRYPOINT [ "bash" ]
