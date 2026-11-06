"""UDP Client: ส่งข้อความไปที่ UDP server และรอคำตอบ (มี timeout เพราะ UDP ไม่รับประกันการส่งถึง)
SERVER_HOST/SERVER_PORT อ่านจาก environment variable (ค่าเริ่มต้น 127.0.0.1:6000)
ถ้ารันโดยไม่มี terminal (เช่น docker run ไม่ใส่ -it) จะส่งข้อความทดสอบให้อัตโนมัติ"""
import os
import socket
import sys

HOST = os.environ.get("SERVER_HOST", "127.0.0.1")
PORT = int(os.environ.get("SERVER_PORT", "6000"))


def send_and_print(s, msg):
    s.sendto(msg.encode("utf-8"), (HOST, PORT))
    try:
        reply, _ = s.recvfrom(1024)
        print(f"ตอบกลับ: {reply.decode('utf-8')}", flush=True)
    except socket.timeout:
        print("ไม่ได้รับคำตอบ (timeout)", flush=True)


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(3)
        if sys.stdin.isatty():
            print("พิมพ์ exit เพื่อออก")
            while True:
                msg = input("ข้อความ: ")
                if msg.lower() == "exit":
                    break
                send_and_print(s, msg)
        else:
            for msg in ["hello", "network programming", "docker udp test"]:
                print(f"ส่ง: {msg}", flush=True)
                send_and_print(s, msg)


if __name__ == "__main__":
    main()
