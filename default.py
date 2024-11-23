import xbmc
import xbmcgui
import xml.etree.ElementTree as ET
import sys

def main():
    dialog = xbmcgui.Dialog()
    feeds = [
        ("- System Stats - )", ""),
        ("Start Cortana Display", "RunScript(Q:\\scripts\\RemoteStats\\stats.py)"),
        ("Stop Cortana Display", "StopScript(Q:\\scripts\\RemoteStats\\stats.py)"),
    ]
    
    feed_list = [name for name, _ in feeds]
    selected = dialog.select(u"Cortana Display", feed_list)
    
    if selected >= 0:
        name, url = feeds[selected]
        if "RunScript" in url:
            xbmc.executebuiltin(url)

if __name__ == '__main__':
    main()
