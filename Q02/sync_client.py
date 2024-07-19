import socket

def start_sync_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 65432))

    try:
        messages = ["Ping", "Ping", "foobar"]
        for message in messages:
            print(f"Send: {message}")
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)
            print(f"Received: {data.decode()}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_sync_client()
