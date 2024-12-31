import time 
from plyer import notification

# while True:
#     time.sleep(2)
#     print("Drink water")

while True:
        notification.notify(
            title="Water Reminder",
            message="It's time to drink water!",
            timeout=10  # Notification stays for 10 seconds
        )
        time.sleep(5)  
