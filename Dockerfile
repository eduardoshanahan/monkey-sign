FROM python:3.10-slim
WORKDIR /code
COPY ./server/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade pip --upgrade -r /code/requirements.txt
COPY ./server /code/server
CMD ["uvicorn", "server.monkeysign:app", "--reload", "--host", "0.0.0.0", "--port", "80"]