"""TCP Echo Server: รับข้อความจาก client แล้วส่งกลับไปเหมือนเดิม
รองรับหลาย client พร้อมกันด้วย thread
HOST/PORT อ่านจาก environment variable (ค่าเริ่มต้น 127.0.0.1:5000) เพื่อให้รันใน Docker ได้"""
import os
import socket
import threading

HOST = os.environ.get("HOST", "127.0.0.1")
PORT = int(os.environ.get("PORT", "5000"))


def handle_client(conn, addr):
    print(f"[TCP] เชื่อมต่อจาก {addr}", flush=True)
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:  # client ปิดการเชื่อมต่อ
                break
            print(f"[TCP] รับจาก {addr}: {data.decode('utf-8')}", flush=True)
            conn.sendall(data)  # echo กลับ
    print(f"[TCP] ปิดการเชื่อมต่อ {addr}", flush=True)


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print(f"[TCP] Echo server รันที่ {HOST}:{PORT}", flush=True)
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()


if __name__ == "__main__":
    main()
