import socket

def Client():
    HOST = '127.0.0.1'  # localhost
    PORT = 12345        # サーバー側と同じポート番号

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(60)
    client.connect((HOST, PORT))

    response = client.recv(1024)
    print(f"サーバーからの応答: {response.decode()}")

    client.close()
