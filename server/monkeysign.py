from fastapi import FastAPI
import socket
import uuid

app = FastAPI()

@app.get('/')
def get_ip_address():
    name = socket.gethostname()
    ip = socket.gethostbyname(name)
    id = uuid.uuid4()
    result = { 'ip': ip, 'name': name, 'id': id}
    return result