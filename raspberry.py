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

# Joystick code to utilize later.

# Button GPIO pins
#BUTTON1_PIN = 21  # GPIO pin for KEY1
#BUTTON2_PIN = 20  # GPIO pin for KEY2
#BUTTON3_PIN = 16  # GPIO pin for KEY3

# Joystick GPIO pins - Uncomment Up/Down/Press if adding your own functionality that requires it.
## JOYSTICK_UP_PIN = 6
## JOYSTICK_DOWN_PIN = 19
#JOYSTICK_LEFT_PIN = 5
#JOYSTICK_RIGHT_PIN = 26
## JOYSTICK_PRESS_PIN = 13

# Button objects
#button1 = Button(BUTTON1_PIN, hold_time=3)
#button2 = Button(BUTTON2_PIN, hold_time=3)
#button3 = Button(BUTTON3_PIN, hold_time=3)

# Joystick objects - Uncomment Up/Down/Press if adding your own functionality that requires it.
## joystick_press = Button(JOYSTICK_PRESS_PIN, hold_time=0)
## joystick_up = Button(JOYSTICK_UP_PIN, hold_time=0)
## joystick_down = Button(JOYSTICK_DOWN_PIN, hold_time=0)
#joystick_left = Button(JOYSTICK_LEFT_PIN, hold_time=0)
#joystick_right = Button(JOYSTICK_RIGHT_PIN, hold_time=0)

# Brightness levels
#brightness_levels = [0.1, 0.5, 1.0]  # Low, medium, high
#current_brightness_index = 0

# Menu states
#SYS_MENU = 0
#MEDIA_MENU = 1
#current_menu_state = SYS_MENU

# End of code to utilize later

def display_info(bios, memory, ip, fan_speed, cpu_temp, artist, track):
    with canvas(device) as draw:
        draw.text((0, 0), f"{bios}", font=FONT, fill=255)
        draw.text((0, 10), f"Free Mem: {memory}", font=FONT, fill=255)
        draw.text((0, 20), f"IP: {ip}", font=FONT, fill=255)
        draw.text((0, 30), f"Fan: {fan_speed} | CPU: {cpu_temp}", font=FONT, fill=255)
        draw.text((0, 40), f"{artist} - {track}", font=FONT, fill=255)
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", LISTEN_PORT))
    
    display_message = False  # Flag to track if we should update the LCD screen
    
    while True:
        data, _ = sock.recvfrom(1024)
        message = data.decode("utf-8")
        message_music = data.decode("utf-8")
        message_video = data.decode("utf-8")

        if message == "PING":
            display_message = True  # Set the flag to True to allow display update

        elif display_message:  # Only process system info message if "PING" was received first
            parts = dict(item.split(": ") for item in message.split(", "))

            bios = parts.get("BIOS", "N/A")
            memory = parts.get("Free Mem", "N/A")
            ip = parts.get("IP", "N/A")
            fan_speed = parts.get("Fan", "N/A")
            cpu_temp = parts.get("CPU", "N/A")
            artist = parts.get("Artist", "N/A")
            track = parts.get("Track", "N/A")
            album = parts.get("Album", "N/A")
            time_during = parts.get("Time", "N/A")
            time_remaining = parts.get("Time Remaining", "N/A")


            display_info(bios, memory, ip, fan_speed, cpu_temp, artist, track)
            display_message = False  # Reset the flag after displaying the message

        time.sleep(1)  # Wait for a while before checking for the next message

if __name__ == "__main__":
    main()
