from evdev import InputDevice, UInput, ecodes
from time import sleep
from read import list_active_evdev

ui = UInput()
output = list_active_evdev()
dev = InputDevice(output[0])

e = {
    'a': ecodes.BTN_A,
    'b': ecodes.BTN_B,
    'x': ecodes.BTN_X,
    'y': ecodes.BTN_Y,

    'tr': ecodes.BTN_TR,
    'tl': ecodes.BTN_TL,
    'tr2': ecodes.BTN_TR2,
    'tl2': ecodes.BTN_TL2,

    'thumbl': ecodes.BTN_THUMBL,
    'thumbr': ecodes.BTN_THUMBR,

    'select': ecodes.BTN_SELECT,
    'start': ecodes.BTN_START,

    'dpadh': ecodes.ABS_HAT0X,
    'dpadv': ecodes.bytype[ecodes.EV_ABS][17],
}

def keydown(key):
    ui.write(ecodes.EV_KEY, key, 1)
    ui.write(ecodes.EV_SYN, 0, 0)

def keyup(key):
    ui.write(ecodes.EV_KEY, key, 1)
    ui.write(ecodes.EV_SYN, 0, 0)

def dirdown(key, direction):
    dev.write(ecodes.EV_ABS, key, direction)
    dev.write(ecodes.EV_SYN, 0, 0)

def dirup(key, direction):
    dev.write(ecodes.EV_ABS, key, direction)
    dev.write(ecodes.EV_SYN, 0, 0)

#keydown(e['a'])
#sleep(0.5)
#keyup(e['a'])
dirdown(e['dpadh'], 1)
sleep(5)
dirup(e['dpadh'], 0)




ui.close()
