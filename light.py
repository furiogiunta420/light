import tinytuya
import sys 
import os
import subprocess
import time

PID_FILE = "show.pid"
SHOW = "show.py"

DEVICE_ID = ""
IP        = ""
LOCAL_KEY = ""
VERSION   = 3.5 
d = tinytuya.BulbDevice(DEVICE_ID, IP, LOCAL_KEY)
d.set_version(VERSION)
d.set_socketPersistent(False)

def farbe():
    os.system('color 5' if os.name == 'nt' else 'color 5')

def esee():
    os.system('title .' if os.name == 'nt' else '.')
    
def raus():
    os.system('cls' if os.name == 'nt' else 'clear')

def longara():
    os.system('mode 38, 18' if os.name == 'nt' else 'mode 38, 18')


def skip():
    os.system('echo.' if os.name == 'nt' else 'echo.')


def oner():
    stop_show()
    raus()
    d.turn_on()
    mainmen()

def offer():
    stop_show()
    raus()
    d.turn_off()
    mainmen()

def brig():
    stop_show()
    raus()
    print("=" * 38)
    skip()
    print("Brightness level 0-100?")
    skip()
    print("=" * 38)
    skip()
    brigi = int(input())
    d.set_brightness_percentage(brigi)
    mainmen()

def custom1():
    raus()
    print("=" * 38)
    skip()
    cusr = int(input("Please enter your RED value: "))
    skip()
    cusg = int(input("Please enter your GREEN value: "))
    skip()
    cusb = int(input("Please enter your BLUE value: "))
    skip()
    print("=" * 38)
    d.set_colour(cusr, cusg, cusb)
    custom()

def custom2():
    raus()
    print("=" * 38)
    skip()
    print("1: Red")
    skip()
    print("2: Green")
    skip()
    print("3: Blue")
    skip()
    print("7: Purple")
    skip()
    print("9: Exit")
    skip()
    print("=" * 38)
    olaa = input()
    if olaa == "1":
        d.set_colour(255, 0, 0)
        custom()
    elif olaa == "2":
        d.set_colour(0, 255, 0)
        custom()
    elif olaa == "3":
        d.set_colour(0, 0, 255)
        custom()
    elif olaa == "7":
        d.set_colour(128, 0, 128)
        custom()
    elif olaa == "9":
        custom()
    else:
        custom2()

def custom():
    stop_show()
    raus()
    print("=" * 38)
    skip()
    print("0: Preselected colours")
    skip()
    print("5: Custom colour")
    skip()
    print("9: Exit")
    skip()
    print("=" * 38)
    skip()
    opaa = input()
    if opaa == "0":
        custom2()
    elif opaa == "5":
        custom1()
    elif opaa == "9":
        mainmen()
    else:
        custom() 

def is_running():
    if not os.path.exists(PID_FILE):
        return False
    pid = open(PID_FILE).read().strip()
    out = subprocess.run(["tasklist", "/FI", f"PID eq {pid}"],
                         capture_output=True, text=True).stdout
    return "pythonw.exe" in out.lower()

def show():
    if is_running():
        pid = open(PID_FILE).read().strip()
        subprocess.run(["taskkill", "/PID", pid, "/F"], capture_output=True)
        if os.path.exists(PID_FILE):
            os.remove(PID_FILE)
        time.sleep(1)
        mainmen()
        return
    pythonw = sys.executable.replace("python.exe", "pythonw.exe")
    p = subprocess.Popen(
        [pythonw, SHOW],
        creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP,
        stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        close_fds=True,
    )
    with open(PID_FILE, "w") as f:
        f.write(str(p.pid))
    time.sleep(1)
    mainmen()

def stop_show():
    if is_running():
        pid = open(PID_FILE).read().strip()
        subprocess.run(["taskkill", "/PID", pid, "/F"], capture_output=True)
        if os.path.exist(PID_FILE):
            os.remove(PID_FILE)






def mainmen():
    try:
        raus()
        esee()
        farbe()
        longara()
        print("=" * 38)
        print("What do you want to do?")
        skip()
        print("1: Turn on the light")
        skip()
        print("3: Turn off the light")
        skip()
        print("5: Change brightness")
        skip()
        print("7: Custom colour")
        skip()
        print("8: Start/Stop Fade")
        skip()
        print("9: Exit")
        skip()
        print("=" * 38)
        skip()
        answi = input()

        if answi == "1":
            oner()
        elif answi == "3":
            offer()
        elif answi == "5":
            brig()
        elif answi == "7":
            custom()
        elif answi == "9":
            sys.exit(0)
        elif answi == "8":
            show()
        else:
            mainmen()

    except KeyboardInterrupt:
        sys.exit(0)

    except Exception as e:
        print("=" * 38)
        skip()
        print(f"Error: {e}")
        input("Press any key to exit...")
        sys.exit(0)

if __name__ == '__main__':
    mainmen()
