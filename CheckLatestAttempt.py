from gi.repository import Notify
from configparser import ConfigParser
import os
import glob
import pathlib

with open("/tmp/testest.txt", 'w+') as file:
    file.write("1")

#Read config.ini file
config_object = ConfigParser()
config_object.read(str(pathlib.Path(__file__).parent.absolute()) + "/config.ini")
paths = config_object["PATH"]
notification = config_object["NOTIFICATION"]

with open("/tmp/testest.txt", 'w+') as file:
    file.write("2")

#Check last attempt
with open(paths["last-attempt"], 'r') as file:
    last_attempt = file.read()

list_of_files = glob.glob(paths["snapshots"])
latest_file = max(list_of_files, key=os.path.getctime)

with open("/tmp/testest.txt", 'w+') as file:
    file.write("3")

#If there is a new attempt, notify
if(latest_file != last_attempt):           
    Notify.init(notification["title"])
    info = Notify.Notification.new(notification["title"], notification["text"], paths["notify-icon"])
    info.set_timeout(Notify.EXPIRES_DEFAULT)
    info.set_urgency(Notify.Urgency.NORMAL)
    info.show()
    os.system('xdg-open ' + latest_file)
else:
    with open("/tmp/testest.txt", 'w+') as file:
        file.write("same file")