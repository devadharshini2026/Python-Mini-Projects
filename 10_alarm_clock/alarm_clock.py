import time
import platform

# Optional: for Windows beep
if platform.system() == "Windows":
    import winsound

def alarm_ring():
    print("⏰ Alarm! Time's up!")
    if platform.system() == "Windows":
        for i in range(5):  # beep 5 times
            winsound.Beep(1000, 1000)  # 1000 Hz, 1 sec
    else:
        print("\a")  # Terminal bell for other OS

def main():
    print("=== Simple Alarm Clock ===")
    alarm_time = input("Set alarm time (HH:MM in 24-hour format): ")

    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            alarm_ring()
            break
        time.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
    main()
