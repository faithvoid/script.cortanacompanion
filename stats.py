import socket
import xbmc
import xbmcaddon

# Constants
BROADCAST_IP = "192.168.1.255"  # Replace with the correct broadcast IP for your network
BROADCAST_PORT = 3074

# Typical XBMC command stuff, grabs system info from info labels.
def get_system_info():
    # XBMC4Xbox-specific system info retrieval
    bios_version = xbmc.getInfoLabel("system.bios")
    free_memory = xbmc.getInfoLabel("System.FreeMemory")
    ip_address = xbmc.getIPAddress()
    fan_speed = xbmc.getInfoLabel("System.FanSpeed")
    cpu_temp = xbmc.getInfoLabel("System.CPUTemperature")
    return {
        "bios_version": bios_version,
        "free_memory": free_memory,
        "ip_address": ip_address,
        "fan_speed": fan_speed,
        "cpu_temp": cpu_temp
    }

# We love text sanitization, yay!
def sanitize(text):
    try:
        return text.encode('ascii', 'ignore')  # Ignore non-ASCII characters
    except:
        return "N/A"

# Network code to broadcast to raspberry.py! 
def broadcast_system_info():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    while True:
        system_info = get_system_info()
        sanitized_info = {k: sanitize(v) for k, v in system_info.items()}  # Sanitize all fields
        
        message = "{bios_version}, Free Mem: {free_memory}, IP: {ip_address}, Fan: {fan_speed}, CPU: {cpu_temp}".format(**sanitized_info)
        
        try:
            sock.sendto(message, (BROADCAST_IP, BROADCAST_PORT))
        except Exception as e:
            xbmc.log("Broadcast Error: {}".format(str(e)), xbmc.LOGERROR)
        
        xbmc.sleep(5000)  # Send every 5 seconds

if __name__ == "__main__":
    broadcast_system_info()
