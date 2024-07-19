import socket
import time

def start_sync_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))
    server_socket.listen()
    print("Server started and listening")

    while True:
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                message = data.decode()
                print(f"Received: {message}")
                if message == "Ping":
                    response = "Pong"
                else:
                    response = message
                time.sleep(3)  # 3초 대기
                conn.sendall(response.encode())
                print(f"Send: {response}")

if __name__ == "__main__":
    start_sync_server()
