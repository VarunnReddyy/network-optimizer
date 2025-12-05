FROM python:3.10-slim

WORKDIR /opt
COPY exporter.py .

RUN pip install flask requests

EXPOSE 9000

CMD ["python3", "/opt/exporter.py"]
