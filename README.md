# Cortana Companion
A remote SH1106/SSD1306 display script for XBMC4Xbox using a Raspberry Pi, designed to emulate the front LCD/OLED screen of a hardmodded Xbox for softmodded units. 

![Cortana Companion running on a Pi Zero W](https://github.com/user-attachments/assets/3a22c738-d332-4a33-b841-3ec1ceb503a3)


## Requirements:
- Any Raspberry Pi model with a GPIO interface, with python3, python3-rpi.gpio & python3-luma.oled installed.
- Either an SH1106 (recommended) or SSD1306 display (requires a line or two of modification to work)
- An Xbox running some variation of XBMC4Xbox (XBMC4Gamers and XBMC-Emustation should work just fine).
- A solid internet connection on your Raspberry Pi and your Xbox (ideally connected directly to your Pi using [Cortana Wireless!](https://github.com/faithvoid/script.cortanawireless)) 
- Python 2.7 on XBMC4Xbox, Python 3+ for Raspberry Pi.

## Raspberry Pi Instructions:
- Enter the line down below in your Pi's terminal after setting up your distro of choice!
- ``` curl -sL https://raw.githubusercontent.com/faithvoid/script.cortanacompanion/refs/heads/main/install.sh | bash ```

## Xbox Instructions:
- Extract CortanaCompanion into Q:\scripts\CortanaCompanion
- Modify the IP address section in "stats.py" to point to the IP address of your Raspberry Pi
- Launch "default.py" from the Scripts manager in XBMC and select "Start Cortana Companion", and select "Stop Cortana Companion" to stop the script.
- You should immediately start seeing stats on your Raspberry Pi display! Note that this does nothing outside of XBMC, so that means when you're in-game your system stats won't update until you boot into XBMC again!

## Customization:
Cortana Companion supports a wide array of customization options, as it's a parser for XBMC InfoLabels. Let's say you want to replace the "Playing" screen with BIOS information. Open raspberry.py, add the "BIOS" value to "last_values" if it's not already there, replace "Playing: {track}" in the display_info section with "BIOS: {bios}", scroll to and insert "bios = last_values["BIOS"]" under "# Extract the updated values" and "bios" into both "display info(bios, memory, etc)" functions if it doesn't exist already.

Next, open "stats.py", add "bios_version = xbmc.getInfoLabel("system.bios")" under "def get_system_info()" if it doesn't exist already, " "bios_version": bios_version, " between the return {} statements underneath that, then add "BIOS: {bios_version}" to the "message =" field if it doesn't exist already.

If all is said and done, you should see BIOS information instead of Now Playing information upon the next script launch!

## Bugs:
- Some songs return symbols that cause the title/track names to bug out and not appear or spam errors in the log. 
- You tell me.

## TODO: 
- Fix "Storage" command (currently returns total HDD space instead of total **FREE** HDD space.)
- Add scrolling to "Playing" section.
- Set up key buttons to function with XBMC (play / pause / stop? or shutdown / restart / reboot?)
- Clean up code further
- Explain the customization section better.
- [Integrate multi-page support like in my other script, PiHOLED.](https://github.com/faithvoid/PiHOLED). Default page will be system staps, then moving the joystick will select either Music or Movie information.
- [Integrate with Cortana Wireless to also function as a network adapter for the original Xbox.](https://github.com/faithvoid/script.cortanawireless)
- 
# Why?
I just think it's neat. :) As someone using a 1.6 softmod I love how the LCD on hardmods looks and wanted to replicate something for softmod users to place on/around their Xbox with no hardware modification required.
