# TiletoNextcloud

This script demonstrates how to retrieve bluetooth Tile trackers information using the pytile library and send the device position to a Nextcloud Phonetrack server.

With this soft, you can easily obtain details such as device name, latitude, longitude, altitude, and last updated timestamp for your Tile devices. It then constructs a URL with these parameters and sends a GET request to the Nextcloud Phonetrack server to update the device's position.

To make use of this script, you need to provide the server URL of your Nextcloud Phonetrack server, your Tile account email and password. The name of the logger will be the name of the tile device.

Execute this script to automate the retrieval of Tile device information and update the device positions in your Nextcloud Phonetrack server effortlessly!

There is a built in rate limit to avoid bloating the nextcloud DB with unhelpfull information.

# Todo
Get more tile to see if it can handle more data sent a once currently only one device at a time has been tested.


# How to use ?

Replace the following and run the .py as often as you desire to refresh the data

server_url = "https://EXEMPLE.COM/apps/phonetrack/logGet/JOBID/"

email = "TILE@MAIL.ADD"

password = "********"

