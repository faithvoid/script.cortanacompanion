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

# Persistent storage for the last known values
last_values = {
    "BIOS": "",
    "Free Mem": "",
    "IP": "",
    "Fan": "",
    "GPU": "",
    "CPU": "",
    "CPU Usage": "",
    "HDD": "",
    "Free Space": "",
    "Artist": "",
    "Track": "",
    "Title": "",
}

def display_info(bios, memory, ip, fan_speed, cpu_temp, cpu_usage, gpu_temp, hdd_temp, free_space, artist, track, title):
    with canvas(device) as draw:
        draw.rectangle((0, 0, WIDTH - 1, HEIGHT - 1), outline=255)
        draw.text((2, 2), f"Playing: {track}", font=FONT, fill=255)
        draw.text((2, 2), f"Playing: {title}", font=FONT, fill=255)
        # This implementation of track/title sucks but it works to show the title of both movies and music. I need to replace this ASAP.
        draw.text((2, 12), f"RAM: {memory} | CPU: {cpu_usage}", font=FONT, fill=255)
        draw.text((2, 22), f"IP: {ip}", font=FONT, fill=255)
        draw.text((2, 32), f"CPU: {cpu_temp} | GPU: {gpu_temp}", font=FONT, fill=255)
        draw.text((2, 42), f"Fan: {fan_speed} | HDD: {hdd_temp}", font=FONT, fill=255)
        draw.text((2, 52), f"Storage: {free_space}", font=FONT, fill=255)

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", LISTEN_PORT))
    
    display_message = False  # Flag to track if we should update the LCD screen
    
    while True:
        data, _ = sock.recvfrom(1024)
        message = data.decode("utf-8")

        if message == "PING":
            display_message = True  # Set the flag to True to allow display update

        elif display_message:  # Only process system info message if "PING" was received first
            try:
                # Parse the received message
                parts = dict(item.split(": ") for item in message.split(", "))

                # Update the last known values with new ones, fallback to previous values if missing
                for key in last_values:
                    if key in parts:
                        last_values[key] = parts[key]

                # Extract the updated values
                bios = last_values["BIOS"]
                memory = last_values["Free Mem"]
                ip = last_values["IP"]
                fan_speed = last_values["Fan"]
                gpu_temp = last_values["GPU"]
                cpu_temp = last_values["CPU"]
                cpu_usage = last_values["CPU Usage"]
                hdd_temp = last_values["HDD"]
                free_space = last_values["Free Space"]
                artist = last_values["Artist"]
                track = last_values["Track"]
                title = last_values["Title"]

                # Display the updated information
                display_info(bios, memory, ip, fan_speed, cpu_temp, cpu_usage, gpu_temp, hdd_temp, free_space, artist, track, title)
                display_message = False  # Reset the flag after displaying the message

            except Exception as e:
                print(f"Error processing message: {e}")

        time.sleep(1)  # Wait for a while before checking for the next message

if __name__ == "__main__":
    main()

