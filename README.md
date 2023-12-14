pip freeze > requirements.txt
========================================================================
Create a python file whatever you like. I’m going to call mine test.py.

sudo nano test.py

import time
from datetime import datetime
while True:
    with open("timestamp.txt", "a") as f:
        f.write("The current timestamp is: " + str(datetime.now()))
        f.close()
    time.sleep(10)
========================================================================
The above script will write the current timestamp in the file after every 10 seconds. Let’s write the service now.

sudo nano /etc/systemd/system/test.service (name of the service which is test in this case)

[Unit]
Description=My test service
After=multi-user.target
[Service]
Type=simple
Restart=always
ExecStart=/usr/bin/python3 /home/<username>/test.py
[Install]
WantedBy=multi-user.target
=========================================================================

sudo systemctl daemon-reload

Let’s enable our service so that it doesn’t get disabled if the server restarts.

sudo systemctl enable test.service
