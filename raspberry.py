import socket
import time
from luma.core.interface.serial import spi
from luma.oled.device import sh1106
from luma.core.render import canvas
from PIL import ImageFont

# Constants
WIDTH = 128
HEIGHT = 64
FONT = ImageFont.load_default()
LISTEN_PORT = 3074

# Initialize SH1106 via SPI, replace with SSD1306 if using that instead.
serial = spi(device=0, port=0)
device = sh1106(serial, width=WIDTH, height=HEIGHT, rotate=2)

def display_info(bios, memory, ip, fan_speed, temp):
    with canvas(device) as draw:
        draw.text((0, 0), f"{bios}", font=FONT, fill=255)
        draw.text((0, 10), f"Free Mem: {memory}", font=FONT, fill=255)
        draw.text((0, 20), f"IP: {ip}", font=FONT, fill=255)
        draw.text((0, 30), f"Fan: {fan_speed} | CPU: {temp}", font=FONT, fill=255)
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", LISTEN_PORT))
    
    while True:
        data, _ = sock.recvfrom(1024)
        message = data.decode("utf-8")
        parts = dict(item.split(": ") for item in message.split(", "))
        
        bios = parts.get("BIOS", "N/A")
        memory = parts.get("Free Mem", "N/A")
        ip = parts.get("IP", "N/A")
        fan_speed = parts.get("Fan Speed", "N/A")
        temp = parts.get("CPU Temp", "N/A")
        
        display_info(bios, memory, ip, fan_speed, temp)
        time.sleep(5)

if __name__ == "__main__":
    main()
