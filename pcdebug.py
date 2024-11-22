import socket
import time

# Constants
LISTEN_PORT = 3074

def log_info(bios, memory, ip, fan_speed, temp):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] BIOS: {bios}, Free Mem: {memory}, IP: {ip}, Fan: {fan_speed}, CPU Temp: {temp}")

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", LISTEN_PORT))
    print(f"Listening for data on port {LISTEN_PORT}...")

    while True:
        data, _ = sock.recvfrom(1024)
        message = data.decode("utf-8")
        parts = dict(item.split(": ") for item in message.split(", "))

        bios = parts.get("BIOS", "N/A")
        memory = parts.get("Free Mem", "N/A")
        ip = parts.get("IP", "N/A")
        fan_speed = parts.get("Fan Speed", "N/A")
        temp = parts.get("CPU Temp", "N/A")
        
        log_info(bios, memory, ip, fan_speed, temp)

if __name__ == "__main__":
    main()
