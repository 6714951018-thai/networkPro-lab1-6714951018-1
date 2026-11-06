import socket
import threading

HOST = "127.0.0.1"
PORT = 5000


def handle_client(conn, addr):
    print(f"[TCP] เชื่อมต่อจาก {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:  # client ปิดการเชื่อมต่อ
                break
            print(f"[TCP] รับจาก {addr}: {data.decode('utf-8')}")
            conn.sendall(data)  # echo กลับ
    print(f"[TCP] ปิดการเชื่อมต่อ {addr}")


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print(f"[TCP] Echo server รันที่ {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()


if __name__ == "__main__":
    main()
