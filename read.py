from evdev import InputDevice, categorize, ecodes, KeyEvent

# Based on http://python-evdev.readthedocs.org/en/latest/index.html
import evdev
import glob
import select
import sys
import time
import json
import argparse


def list_active_evdev():
    '''Lists the next /dev/input/event* devices to generate input events.
       Will usually only be a single device.'''

    devices = []
    for dev in glob.glob('/dev/input/event*'):
        try:
            devices.append(evdev.device.InputDevice(dev))
        except (IOError, OSError):
            # Don't have permissions for that device, ignore it.
            pass
    devices = {dev.fd: dev for dev in devices}

    output = []
    anyInput = False
    while not anyInput:
        # use select to wait for input
        r, w, x = select.select(devices, [], [])
        for fd in r:
            for event in list(devices[fd].read())[:1]:
                output.append(devices[fd].fn)
                anyInput = True

    return output

def handle_args():

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-f', "--file_name", default="meta.json")

    args = parser.parse_args()
    return args


def record_macro(out_file):
    # Print the next /dev/input/event* device to generate an input event.
    output = list_active_evdev()

    device = InputDevice(output[0])

    t = 0.0

    events = []

    first_event = True

    try:
        for event in device.read_loop():
            # if event.type == ecodes.EV_KEY:
            #    keyevent = categorize(event)
            #    if keyevent.keystate == KeyEvent.key_down:
            #        print(keyevent.keycode)
            # if event.type == ecodes.EV_ABS:
            #    keyevent = categorize(event)
            #    print(keyevent.event)
            keyevent = categorize(event)

            sec = event.sec + (event.usec / 1000000)
            if first_event:
                t = sec
                first_event = False
            current_event = {"sec": sec - t, "type": event.type, "code": event.code,
                             "value": event.value}
            events.append(current_event)

    except KeyboardInterrupt:
        with open(out_file, 'w') as json_file:
            json.dump(events, json_file)
        sys.exit()

def main():
    args = handle_args()

    record_macro(args.file_name)

if __name__ == "__main__":
    main()
