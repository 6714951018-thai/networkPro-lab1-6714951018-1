"""TCP Client: ส่งข้อความไปที่ echo server แล้วแสดงผลที่ได้รับกลับมา
SERVER_HOST/SERVER_PORT อ่านจาก environment variable (ค่าเริ่มต้น 127.0.0.1:5000)
ถ้ารันโดยไม่มี terminal (เช่น docker run ไม่ใส่ -it) จะส่งข้อความทดสอบให้อัตโนมัติ"""
import os
import socket
import sys

HOST = os.environ.get("SERVER_HOST", "127.0.0.1")
PORT = int(os.environ.get("SERVER_PORT", "5000"))


def send_and_print(s, msg):
    s.sendall(msg.encode("utf-8"))
    reply = s.recv(1024)
    print(f"Echo จาก server: {reply.decode('utf-8')}", flush=True)


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"เชื่อมต่อ {HOST}:{PORT} สำเร็จ", flush=True)
        if sys.stdin.isatty():
            print("พิมพ์ exit เพื่อออก")
            while True:
                msg = input("ข้อความ: ")
                if msg.lower() == "exit":
                    break
                send_and_print(s, msg)
        else:
            for msg in ["hello", "network programming", "docker tcp test"]:
                print(f"ส่ง: {msg}", flush=True)
                send_and_print(s, msg)


if __name__ == "__main__":
    main()
