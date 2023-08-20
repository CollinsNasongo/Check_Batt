import psutil
from win10toast import ToastNotifier

def check_plugged():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    plugged = True if plugged else False
    return plugged


def read_percentage():
    battery = psutil.sensors_battery()
    percent = int(battery.percent)
    return percent


def check_batt():
    is_plugged = check_plugged()
    if is_plugged:
        batt_perc = read_percentage()
        if batt_perc >= 80:
            return batt_perc

        elif batt_perc <= 40:
            return batt_perc

def batt_not():
    batt_perc = check_batt()
    toaster = ToastNotifier()
    
    if batt_perc >= 80:
        message = f"Battery at {batt_perc}%, Unplug charger."
        toaster.show_toast("Battery Notification",message,
                   "icons\full-battery.ico",
                   duration=10)
    elif batt_perc <= 40:
        message = f"Battery at {batt_perc}%, Plug in charger."
        toaster.show_toast("Battery Notification",message,
                   "icons\full-battery.ico",
                   duration=10)