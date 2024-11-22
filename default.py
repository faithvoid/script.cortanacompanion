import xbmc
import xbmcgui
import xml.etree.ElementTree as ET
import sys

def main():
    dialog = xbmcgui.Dialog()
    feeds = [
        ("Start Remote Display)", "RunScript(Q:\\scripts\\RemoteStats\\stats.py)"),
        ("Stop Remote Display", "RunScript(Q:\\scripts\\RemoteStats\\stats.py)"),
    ]
    
    feed_list = [name for name, _ in feeds]
    selected = dialog.select(u"XBMC Raspberry Pi Feed", feed_list)
    
    if selected >= 0:
        name, url = feeds[selected]
        if "RunScript" in url:
            xbmc.executebuiltin(url)

if __name__ == '__main__':
    main()
