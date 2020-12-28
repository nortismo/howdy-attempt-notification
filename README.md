# Howdy Attempt Notification

After installation of howdy and the automated login, I wanted to have notifications of failed attempts. This repository contains scripts to detect failed attempts and notify the user after successful login. 

## Configuration Files

The file [howdy-config-example.ini](howdy-config-example.ini) contains a example configuration for howdy. Futhermore, the file [config.ini](config.ini) can be used to configure the scripts. IMPORTANT: Change the paths in the configuartion file accordingly to the location of the scripts.

## Configuration in KDE

In order to run the scripts on unlock and lock events, open the configuration at 'system settings' > 'Notifications' > 'Applications' > 'Screen Saver' -> 'Configure Event'. Add the file [onLock](onLock) as 'Run Command' on the event 'Screen locked'. On the other hand, add the file [onUnlock](onUnlock) as 'Run Command' on the event 'Screen unlocked'. 

## Access rights

Make sure the scripts can be run from the system and the folder where the snapshots of howdy are stores (usually '/lib/security/howdy/snapshots') can be accessed from the system.