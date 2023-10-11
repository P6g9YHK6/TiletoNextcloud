import asyncio
import aiohttp
from pytile import async_login
import urllib.parse
import os
from datetime import datetime
import time

server_url = "https:///apps/phonetrack/logGet//"
email = "@."
password = ""
coordinate_file = "last_coordinates.txt"

async def main() -> None:
    async with aiohttp.ClientSession() as session:
        api = await async_login(email, password, session)
        tiles = await api.async_get_tiles()

        for tile_uuid, tile in tiles.items():
            name = tile.name
            timestamp = int(time.mktime(datetime.fromisoformat(str(tile.last_timestamp)).timetuple()))

            stored_timestamp = get_stored_timestamp(name)

            print(f"Tile: {name}")
            print(f"Current Timestamp: {timestamp}")
            print(f"Stored Timestamp:  {stored_timestamp}")

            if stored_timestamp is not None and stored_timestamp == timestamp:
                print("Timestamp has not changed. Skipping update.")
                continue

            url = f"{server_url}{name}?lat={tile.latitude}&lon={tile.longitude}&alt={tile.altitude}&timestamp={timestamp}"
            headers = {
                "User-Agent": "TileWorker"
            }

            print("Sending position to Phonetrack server:")
            print(url)

            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    print(f"{response.status} | Position sent successfully.")
                    update_coordinate_file(name, timestamp)
                else:
                    print(f"{response.status} | Failed to send position.")

def get_stored_timestamp(name):
    if not os.path.isfile(coordinate_file):
        return None

    with open(coordinate_file, "r") as file:
        for line in file:
            stored_name, stored_timestamp = line.strip().split(",")

            # Check if the line has the correct format
            if len(line.strip().split(",")) != 2:
                continue

            if stored_name == name:
                return int(stored_timestamp)

    return None

def update_coordinate_file(name, timestamp):
    with open(coordinate_file, "w") as file:
        file.write(f"{name},{timestamp}")

asyncio.run(main())
