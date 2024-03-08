import os
import socket
import time

def size():
    size = 0
    name = socket.gethostname()
    part = name.split("s-")
    username = part[0]
    # assign folder path
    Folderpath = f"/Users/{username}/Library/Caches"

    # get size
    for path, dirs, files in os.walk(Folderpath):
        for f in files:
            fp = os.path.join(path, f)
            size += os.path.getsize(fp)
    size_in_megabits = (size) / (1024 * 1024)

    return "{:.2f} megabyte".format(size_in_megabits)

def display_notification(title, subtitle, message):
    script = f'display notification "{message}" with title "{title}"'
    if subtitle:
        script += f' subtitle "{subtitle}"'
    os.system(f"osascript -e '{script}'")
    timeout = 10


time.sleep(3)    
display_notification(f"Cyber-sec", size(),"Cache is cleared successfully")
