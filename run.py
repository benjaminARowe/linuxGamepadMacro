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

    for current_event in macro:
        etype = ecodes.EV[current_event["type"]]
        code = current_event["code"]

        dev.write(ecodes.EV_ABS, key, direction)
        
        print(current_event["sec"])



