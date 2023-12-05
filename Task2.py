import socket
import threading


class EchoServerThreaded:
    def __init__(self, host, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        print(f"Echo Server is listening on {host}:{port}")

    def handle_client(self, client_socket):
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            client_socket.sendall(data)
        client_socket.close()

    def start(self):
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Accepted connection from {client_address}")

            client_thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_thread.start()


if __name__ == "__main__":
    host = "localhost"
    port = 5555

    echo_server = EchoServerThreaded(host, port)
    echo_server.start()
