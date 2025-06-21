import time
from plyer import notification
while True:
    print("Reminder: Take a break and stretch!")
    notification.notify(
        title="Break Reminder",
        message="It's time to take a break and stretch your legs!",
        
    )
    time.sleep(60*60)  # Wait for 1 hour before reminding again