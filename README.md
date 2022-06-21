# SprinklerScript
SImple script to run locally on a Pi or other GPIO device


When copying over the pi, it did so with 5-space tabs. Maybe thats a nano thing, but just be aware in case you are used to 4 space tabs

You can set up this script to run via crontab or another system. Here ae the entries I use on raspbian (Rasypberry Pi OS)

0 6 * * 2 python /home/pi/sprinklers.py

0 6 * * 5 python /home/pi/sprinklers.py

30 6 * * * python /home/pi/sprinklers_drip.py


The following is the GPIO to MQTT bridge I use to controll and monitor via Home assistant. This is the direcction I will move in the future

@reboot sleep 60 && /usr/bin/screen -d -m -S MQTT-GPIO /usr/bin/python -m pi_mqtt_gpio.server /home/pi/mqtt_config.yml &
