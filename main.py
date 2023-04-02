from plyer import notification
import time
if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Drink Water!",
            message = "Drinking Water Increases Energy & Relieves Fatigue.About 15.5 cups(3.7 liters)of fluids a day for men.About 11.5 cups (2.7 liters) of fluids a day for women.",
            app_icon ="F:\python project\Water drinking notifer\icon.ico",
            timeout = 12
        )
        time.sleep(60*60) 
