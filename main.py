import os
import psutil
from plyer import notification
from tqdm import trange
from time import sleep
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from pygame import mixer
from datetime import datetime

mixer.init()
mixer.music.load('battery_charged.mp3')

APPNAME = "BFC"

def check_battery():
    battery = psutil.sensors_battery()
    if battery is not None:
        plugged = battery.power_plugged
        percent = battery.percent
        if plugged:
            if percent == 100:
                return (True, percent, True)
            return (False, percent, True)
        else:
            return (None, percent, False)
    return (False, None, None)

def notify(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name=APPNAME,
        timeout=20
    )

# Function to set system volume to 100%
def set_system_volume_100():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(1.0, None)
    print("System volume set to 100%")

# Get the current volume 
def get_current_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current_volume = volume.GetMasterVolumeLevelScalar()
    return current_volume

# Set system volume to certain volume
def set_system_volume(volume_level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(volume_level, None)

def notifyBattery():
    print(f"\n{APPNAME} now working in the background and will notify you once your PC is fully charged")
    current_percent = 0
    sleep(1.5)
    print("DO NOT close this window, you can minimize the window\n")
    sleep(.8)
    while True:
        try:
            battery_status = check_battery()
            is_charged = battery_status[0]
            percent = battery_status[1]
            if percent:
                if current_percent < percent:
                    
                    print(f"Your Battery is currently at {'.'*50}{percent}% as at {datetime.now():%H:%M:%S (%h, %d)}\n")
                elif current_percent > percent and current_percent != 0:
                    print(f"WARNING: Your PC is discharging in a funny way\n\nYour Battery is currently at {'.'*50}{percent}%\n")
                current_percent = percent

                if is_charged:
                    notify("Battery Fully Charged", "Your battery is fully charged, you can unplug it!")
                    print("\n\nYour PC is fully charged, you can unplug it now")
                    current_volume = get_current_volume()
                    # Set the system volume to 100%
                    set_system_volume_100()
                    mixer.music.play(-1)
                    while check_battery()[2] == True:
                        sleep(0.2)
                    mixer.music.stop()
                    set_system_volume(current_volume)
                    break
                elif is_charged is None:
                    sleep(1)
                    print("\n\nYour PC is not Plugged, Plug your PC to use", APPNAME, "then try again")
                    input("\nHit the Enter Key to close: ")
                    break
            sleep(10)  # Check every 10 seconds
        except KeyboardInterrupt:
            break


def notifyPercent():
    while True:
        targetPercent = input("What is the target percent?\n>>> ")
        try:
            targetPercent = int(targetPercent)
            break
        except:
            print("Input must be an INTEGER\n\n")
    print(f"\n{APPNAME} now working in the background and will notify you once your PC reached the terget percentage")
    sleep(.8)
    print("DO NOT close this window, you can minimize the window\n")
    sleep(.8)
    while True:
        battery_status = check_battery()
        is_charged = battery_status[0]
        percent = battery_status[1]
        if percent:
            if (percent == targetPercent):
                notify("Battery Reached Target Percentage", f"Battery at {targetPercent}")
                print(f"Battery has reached {targetPercent}")
                break
        sleep(5)


def main():
    print(f"Welcome to {APPNAME}\n\n")
    sleep(0.5)
    for i in trange(100):
        sleep(.02)
    while True:
        task = input("\n\nWhat will you like yo do?\n\n1) Notify when PC is fully charge\n2) Notify me when PC reach certain Percent\n>>> ")
        try:
            int(task)
            break
        except:
            print("Invalid Input, Enter 1 or 2\n")

    if task == "1":
        notifyBattery()
    elif task == "2":
        notifyPercent()
    else:
        print("Invalid  choice")

if __name__ == "__main__":
    main()

