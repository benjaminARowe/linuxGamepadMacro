from read import list_active_evdev, handle_args
from run import play_macro
from evdev import InputDevice, UInput, ecodes

from time import sleep



if __name__ == "__main__":
    output = list_active_evdev()
    dev = InputDevice(output[0])
    for j in range(0, 20):
        print(j)

        for i in range(0, 1000):
            play_macro("./walk_daycare.json" , dev)


        play_macro("./deposit_daycare.json" , dev)
        play_macro("./receive_daycare.json" , dev)
