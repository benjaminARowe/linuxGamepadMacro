from evdev import InputDevice, UInput, ecodes
from time import sleep
from read import list_active_evdev, handle_args 
import json

def play_macro(file_name, dev):

    macro = []
    with open(file_name) as f:
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
        last_sec = sec



def main():
    args = handle_args()

    output = list_active_evdev()
    dev = InputDevice(output[0])

    play_macro(args.file_name, dev)

if __name__ == "__main__":
    main()



