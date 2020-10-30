from evdev import InputDevice, UInput, ecodes
from time import sleep
from read import list_active_evdev
import json

if __name__ == "__main__":
    output = list_active_evdev()
    dev = InputDevice(output[0])

    macro = []
    with open('macro.json') as f:
      macro = json.load(f)

    last_sec = 0
    for current_event in macro:
        sec = current_event["sec"]
        sleep(sec - last_sec)

        etype = ecodes.EV[current_event["type"]]
        ntype = current_event["type"]

        code = current_event["code"]

        value = current_event["value"]

        dev.write(ntype, code, value)
        print(f"Wrote: {sec - last_sec}")
        last_sec = sec





