FROM python:3.9-slim
WORKDIR /app
COPY messaging* /app
COPY server.py /app
RUN pip install grpcio grpcio-tools grpcio-reflection
CMD ["python3", "server.py"]
