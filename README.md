# script.cortanadisplay
A remote SH1106/SSD1306 display script for XBMC4Xbox using a Raspberry Pi, designed to emulate the front LCD/OLED screen of a hardmodded Xbox for softmodded units.

![Cortana Display running on a Pi Zero W](https://github.com/user-attachments/assets/8f7967d1-0f36-470a-a11d-6e1d9a6dd0da)


## Requirements:
- Any Raspberry Pi model with a GPIO interface, with python3, python3-rpi.gpio & python3-luma.oled installed.
- Either an SH1106 (recommended) or SSD1306 display (requires a line or two of modification to work)
- An Xbox running some variation of XBMC4Xbox (XBMC4Gamers and XBMC-Emustation should work just fine).
- A solid internet connection on your Raspberry Pi and your Xbox (ideas, ideas...)
- Python 2.7 on XBMC4Xbox, Python 3+ for Raspberry Pi.

## Raspberry Pi Instructions:
- Copy "raspberry.pi" anywhere on your Raspberry Pi.
- Install the required dependencies (sudo apt install python3 python3-rpi.gpio python3-luma.oled)
- Launch "raspberry.py" on your Raspberry Pi so that it's running in the background.

## Xbox Instructions:
- Extract XBMCDisplay into any Q:\scripts folder (ideally CortanaDisplay)
- Launch "default.py" from the Scripts manager in XBMC and select "Start Remote Display"
- You should immediately start seeing stats on your Raspberry Pi display!

## Bugs:
- Fan speed will say "N/A" on first boot. This usually sorts itself out after 1-2 refreshes.
- CPU Temperature may not be able to be logged via softmods and may also show up as "N/A", more testing needs to be done! 

## TODO: 
- Clean up code further
- Generate systemctl startup file for Pi to launch the script on boot.
- [Integrate multi-page support like in my other script, PiHOLED.](https://github.com/faithvoid/PiHOLED)
- [Integrate with Cortana Wireless to also function as a network adapter for the original Xbox.](https://github.com/faithvoid/script.cortanawireless)
