# screencontrol

This project is born of a need to control the on/off state of a touch screen attached to a raspberry pi. 
It publishes and consumes state data from an mqtt server, in my own setup that is part of homeassistant,
but that's in no way required.


# testing

In order to run the local mqtt server under podman the below command should work.
```bash
podman kube play mqtt-server.ya 
uv run main.py
```

