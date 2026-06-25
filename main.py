from aiomqtt import Client

import os
import asyncio

async def publish_state(client):
    pass

async def listen_for_changes(client):
    pass


async def main(mqtt_user, mqtt_pass, mqtt_server, mqtt_path, display_id):
    async with Client(hostname=mqtt_server, username=mqtt_user, password=mqtt_pass) as client:
        await asyncio.gather(
            publish_state(client),
            listen_for_changes(client)
        )


if __name__ == "__main__":
    mqtt_user   = os.environ.get('MQTT_USER', None)
    mqtt_pass   = os.environ.get('MQTT_PASS', None)
    mqtt_server = os.environ.get('MQTT_SERVER', 'localhost')
    mqtt_path   = os.environ.get('MQTT_PATH', 'raspberrypi/display/status')

    display_id = os.environ.get('DISPLAY_ID', "2")

    asyncio.run(main(mqtt_user=mqtt_user, mqtt_pass=mqtt_pass, mqtt_server=mqtt_server, mqtt_path=mqtt_pass, display_id=display_id))
