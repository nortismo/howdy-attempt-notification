from configparser import ConfigParser
import glob
import os
import pathlib

#Read config.ini file
config_object = ConfigParser()
config_object.read(str(pathlib.Path(__file__).parent.absolute()) + "/config.ini")
paths = config_object["PATH"]

#Check latest snapshot files
list_of_snapshots = glob.glob(paths["snapshots"])
latest_file = max(list_of_snapshots, key=os.path.getctime)

#Save
with open(paths["last-attempt"], 'w+') as file:
    file.write(latest_file)