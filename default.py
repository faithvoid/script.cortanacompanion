import xbmc
import xbmcgui
import xml.etree.ElementTree as ET
import sys

def main():
    dialog = xbmcgui.Dialog()
    feeds = [
        ("- System Stats - )", ""),
        ("Start Cortana Companion", "RunScript(Q:\\scripts\\CortanaCompanion\\stats.py)"),
        ("Stop Cortana Companion", "StopScript(Q:\\scripts\\CortanaCompanion\\stats.py)"),
    ]
    
    feed_list = [name for name, _ in feeds]
    selected = dialog.select(u"Cortana Companion", feed_list)
    
    if selected >= 0:
        name, url = feeds[selected]
        if "RunScript" in url:
            xbmc.executebuiltin(url)

if __name__ == '__main__':
    main()
