import socket

HOST = "127.0.0.1"
PORT = 6000


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print(f"[UDP] Server รันที่ {HOST}:{PORT}")
        while True:
            data, addr = s.recvfrom(1024)
            print(f"[UDP] รับจาก {addr}: {data.decode('utf-8')}")
            s.sendto(b"ACK: " + data, addr)


if __name__ == "__main__":
    main()
