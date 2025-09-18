import time

def stopwatch():
    print("⏱️ Simple Stopwatch")
    print("Press ENTER to start, ENTER to stop, and type 'exit' to quit.\n")

    while True:
        command = input("Press ENTER to start or type 'exit' to quit: ")
        if command.lower() == "exit":
            print("👋 Exiting stopwatch.")
            break

        start_time = time.time()
        input("Stopwatch running... Press ENTER to stop. ")
        end_time = time.time()

        elapsed_time = end_time - start_time
        mins, secs = divmod(int(elapsed_time), 60)
        millis = int((elapsed_time - int(elapsed_time)) * 1000)

        print(f"⏲️ Elapsed Time: {mins:02}:{secs:02}.{millis:03}\n")

if __name__ == "__main__":
    stopwatch()
