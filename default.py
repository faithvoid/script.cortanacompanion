import xbmc
import xbmcgui
import xml.etree.ElementTree as ET
import sys

def main():
    dialog = xbmcgui.Dialog()
    feeds = [
        ("- System Stats - )", ""),
        ("Enable", "RunScript(Q:\\scripts\\RemoteStats\\stats.py)"),
        ("Disable", "StopScript(Q:\\scripts\\RemoteStats\\stats.py)"),
        ("- Media Info - )", ""),
        ("Enable", "RunScript(Q:\\scripts\\RemoteStats\\media.py)"),
        ("Disable", "StopScript(Q:\\scripts\\RemoteStats\\media.py)"),
    ]
    
    feed_list = [name for name, _ in feeds]
    selected = dialog.select(u"Cortana Display", feed_list)
    
    if selected >= 0:
        name, url = feeds[selected]
        if "RunScript" in url:
            xbmc.executebuiltin(url)

if __name__ == '__main__':
    main()
