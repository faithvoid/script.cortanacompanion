import socket
import xbmc
import xbmcaddon

# Constants
BROADCAST_IP = "192.168.1.113"  # Replace with the correct broadcast IP for your network
BROADCAST_PORT = 3074

# Typical XBMC command stuff, grabs system info from info labels.

def get_system_info():
    bios_version = xbmc.getInfoLabel("system.bios")
    free_memory = xbmc.getInfoLabel("System.FreeMemory")
    ip_address = xbmc.getIPAddress()
    fan_speed = xbmc.getInfoLabel("System.FanSpeed")
    cpu_temp = xbmc.getInfoLabel("System.CPUTemperature")
    
    # Music
    track = xbmc.getInfoLabel("MusicPlayer.Title")
    artist_music = xbmc.getInfoLabel("MusicPlayer.Artist")
    album_music = xbmc.getInfoLabel("MusicPlayer.Album")
    time_during_music = xbmc.getInfoLabel("MusicPlayer.Time")
    time_remaining_music = xbmc.getInfoLabel("MusicPlayer.TimeRemaining")
    
    # Video
    title_video = xbmc.getInfoLabel("VideoPlayer.Title")
    artist_video = xbmc.getInfoLabel("VideoPlayer.Artist")
    album_video = xbmc.getInfoLabel("VideoPlayer.Album")
    time_during_video = xbmc.getInfoLabel("VideoPlayer.Time")
    time_remaining_video = xbmc.getInfoLabel("VideoPlayer.TimeRemaining")
    
    return {
        "bios_version": bios_version,
        "free_memory": free_memory,
        "ip_address": ip_address,
        "fan_speed": fan_speed,
        "cpu_temp": cpu_temp,
        # Music
        "track": track,
        "artist": artist,
        "album": album,
        "time_during": time_during,
        "time_remaining": time_remaining,
        # Video
        "title": title,
        "time_during_video": time_during_video,
        "time_remaining_video": time_remaining_video
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
        # First send a PING message to signal the Raspberry Pi to update the LCD
        try:
            sock.sendto("PING", (BROADCAST_IP, BROADCAST_PORT))
        except Exception as e:
            xbmc.log("Broadcast Error: {}".format(str(e)), xbmc.LOGERROR)
        
        # Then send the system info
        system_info = get_system_info()
        sanitized_info = {k: sanitize(v) for k, v in system_info.items()}  # Sanitize all fields
        
        message = "BIOS: {bios_version}, Free Mem: {free_memory}, IP: {ip_address}, Fan: {fan_speed}, CPU: {cpu_temp}, Track: {track}".format(**sanitized_info)
        
        try:
            sock.sendto(message, (BROADCAST_IP, BROADCAST_PORT))
        except Exception as e:
            xbmc.log("Broadcast Error: {}".format(str(e)), xbmc.LOGERROR)
        
        xbmc.sleep(5000)  # Send every 5 seconds

if __name__ == "__main__":
    broadcast_system_info()
