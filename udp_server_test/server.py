"""UDP Server: รับ datagram แล้วตอบกลับไปยังผู้ส่ง
HOST/PORT อ่านจาก environment variable (ค่าเริ่มต้น 127.0.0.1:6000) เพื่อให้รันใน Docker ได้"""
import os
import socket

HOST = os.environ.get("HOST", "127.0.0.1")
PORT = int(os.environ.get("PORT", "6000"))


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print(f"[UDP] Server รันที่ {HOST}:{PORT}", flush=True)
        while True:
            data, addr = s.recvfrom(1024)
            print(f"[UDP] รับจาก {addr}: {data.decode('utf-8')}", flush=True)
            s.sendto(b"ACK: " + data, addr)


if __name__ == "__main__":
    main()
