# networkPro-lab1-6714951018

**ชื่อ-สกุล:** ธัญรัตน์ พูนทอง  **รหัสนักศึกษา:** 6714951018
**รายวิชา:** Network Programming (CH1: Python Network)

## โครงสร้างโปรเจกต์
```
tcp_echo_server/   server.py, client.py, Dockerfile.server, Dockerfile.client
udp_server_test/   server.py, client.py, Dockerfile.server, Dockerfile.client
screenshots/       ภาพผลการทดสอบ
```

## วิธีรัน (Python ปกติ)
**TCP** (เปิด 2 terminal)
```
cd tcp_echo_server
python server.py
python client.py
```
**UDP** (เปิด 2 terminal)
```
cd udp_server_test
python server.py
python client.py
```
พิมพ์ `exit` ที่ฝั่ง client เพื่อออกจากโปรแกรม

## วิธีรันด้วย Docker
สร้างเครือข่ายให้ container คุยกันได้ (ทำครั้งเดียว)
```
docker network create lab1-net
```
**TCP**
```
cd tcp_echo_server
docker build -f Dockerfile.server -t tcp-server .
docker build -f Dockerfile.client -t tcp-client .
docker run --rm --name tcp-server --network lab1-net -p 5000:5000 tcp-server
docker run --rm -it --network lab1-net tcp-client
```
**UDP**
```
cd udp_server_test
docker build -f Dockerfile.server -t udp-server .
docker build -f Dockerfile.client -t udp-client .
docker run --rm --name udp-server --network lab1-net -p 6000:6000/udp udp-server
docker run --rm -it --network lab1-net udp-client
```
client หา server ผ่านชื่อ container (`tcp-server` / `udp-server`) บนเครือข่าย `lab1-net` ถ้ารัน client โดยไม่ใส่ `-it` จะส่งข้อความทดสอบให้อัตโนมัติ

## การออกแบบและเหตุผลที่เลือกเทคนิค
- ใช้โมดูล `socket` มาตรฐานของ Python ไม่ต้องติดตั้งเพิ่ม
- TCP (`SOCK_STREAM`): เชื่อมต่อแบบ connection-oriented ข้อมูลครบและเรียงลำดับ เหมาะกับ echo ที่ต้องการความถูกต้อง ใช้ thread เพื่อรองรับหลาย client
- UDP (`SOCK_DGRAM`): ไม่ต้องเชื่อมต่อ เร็วและเบา แต่ไม่รับประกันการส่งถึง จึงตั้ง `timeout` ฝั่ง client
- Docker: แพ็กโปรแกรมให้รันได้เหมือนกันทุกเครื่อง แยก server/client เป็นคนละ image อ่านค่า host/port จาก environment variable (ค่าเริ่มต้นยังเป็น 127.0.0.1 จึงรันปกติได้เหมือนเดิม)

## ผลการทดสอบ
### TCP
![TCP result](screenshots/tcp_result.png)
### UDP
![UDP result](screenshots/udp_result.png)

## แหล่งอ้างอิง
- Python docs: https://docs.python.org/3/library/socket.html
- Docker docs: https://docs.docker.com/

