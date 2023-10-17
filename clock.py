import time

def set_alarm(alarm_time):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time to wake up!")
            break

def main():
    print("Welcome to the Alarm Clock program.")
    print("Please enter the time for your alarm in 24-hour format (e.g., 07:30:00):")
    
    alarm_time = input(">> ")
    
    try:
        time.strptime(alarm_time, "%H:%M:%S")
        print(f"Alarm set for {alarm_time}")
        set_alarm(alarm_time)
    except ValueError:
        print("Invalid time format. Please use HH:MM:SS format.")

if __name__ == "__main__":
    main()