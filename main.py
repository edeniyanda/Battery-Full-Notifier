import psutil
from plyer import notification
from tqdm import trange
from time import sleep


APPNAME = "BFC"




def check_battery():
    battery = psutil.sensors_battery()
    if battery is not None:
        plugged = battery.power_plugged
        percent = battery.percent
        if plugged :
            if percent == 100:
                return (True, percent)
        else:
            return (None, percent)
    return (False, percent)

def notify(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name=APPNAME,
        timeout=1000
    )

def main():
    current_percent = 0
    print(F"Welcome to {APPNAME}\n\n")
    sleep(0.5) 
    for i in trange(100):
        sleep(.02)
    sleep(1)
    print(f"\n{APPNAME} now working in background, and will notify you once your PC is fully charged")
    print("DO NOT close this window, you can minimize the window\n")
    while True:
        try:
            percent = check_battery()[1]
            if current_percent < percent:
                print(f"Your Battery is currently at {'.'*50}{percent}%\n")
            elif current_percent > percent and current_percent != 0:
                print(f"WARNING: Your PC is discharging in a funny way\n\nYour Battery is currently at {'.'*50}{percent}%\n")
            current_percent = percent

            if check_battery()[0]:
                notify("Battery Fully Charged", "Your battery is fully charged, you can unplug it!")
                print("\n\nYour PC is fully charged, you can unplug it now")
                quit()  
            elif check_battery()[0] is None:
                sleep(1)
                print("\n\nYour PC is not Plugged, Plug your PC to use", APPNAME, "then try again")   
                input("\nHit the Enter Key to close: ")
                break
            sleep(5)
            # Check every half a minute 
        except KeyboardInterrupt:
            continue 

if __name__ == "__main__":
    main()
