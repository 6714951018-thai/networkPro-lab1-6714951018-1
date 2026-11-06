import socket

HOST = "127.0.0.1"
PORT = 5000


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print("เชื่อมต่อสำเร็จ (พิมพ์ exit เพื่อออก)")
        while True:
            msg = input("ข้อความ: ")
            if msg.lower() == "exit":
                break
            s.sendall(msg.encode("utf-8"))
            reply = s.recv(1024)
            print(f"Echo จาก server: {reply.decode('utf-8')}")


if __name__ == "__main__":
    main()
