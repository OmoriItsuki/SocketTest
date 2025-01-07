import socket

def Server(message):
    HOST = '127.0.0.1'  # localhost
    PORT = 12345        # クライアント側と同じポート番号

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)

    print("サーバーが起動しました。クライアントからの接続を待機中...")

    try:
        while True:
            print("クライアントからの接続を待機中...")
            conn, addr = server.accept()
            print(f"クライアント {addr} が接続しました")
            
            conn.send(message.encode())
            
            conn.close()
            break

    except KeyboardInterrupt:
        print("サーバーを停止します。")
        server.close()

    server.close()
