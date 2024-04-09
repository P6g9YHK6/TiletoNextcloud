# TiletoNextcloud

This script retrieve bluetooth Tile trackers information using the pytile library and send the device position to a Nextcloud Phonetrack server.

With this soft, you can easily obtain details such as device name, latitude, longitude, altitude, and last updated timestamp for your Tile devices. It then constructs a URL with these parameters and sends a GET request to the Nextcloud Phonetrack server to update the device's position.

Execute this script to automate the retrieval of Tile device information and update the device positions in your Nextcloud Phonetrack server effortlessly!

There is a built in rate limit to avoid bloating the nextcloud DB with unhelpfull information.

# Todo

🔲Get rid of stderr in case of device without data

🔲Add health monitoring (probabably uptimekuma push)

# How to use ?

Replace the following and run the .py as often as you desire to refresh the data

server_url = "https://EXEMPLE.COM/apps/phonetrack/logGet/JOBID/"

email = "TILE@MAIL.ADD"

password = "********"

The name of the logger that your expect after the jobid will be the name of the tile device.

## Tested on
[Chronos](https://github.com/simse/chronos), Windows
