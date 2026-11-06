import socket

HOST = "127.0.0.1"
PORT = 6000


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(3)
        print("พิมพ์ exit เพื่อออก")
        while True:
            msg = input("ข้อความ: ")
            if msg.lower() == "exit":
                break
            s.sendto(msg.encode("utf-8"), (HOST, PORT))
            try:
                reply, _ = s.recvfrom(1024)
                print(f"ตอบกลับ: {reply.decode('utf-8')}")
            except socket.timeout:
                print("ไม่ได้รับคำตอบ (timeout)")


if __name__ == "__main__":
    main()
