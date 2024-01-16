import threading
import time
from plyer import notification


def show_notification():
    notification.notify(
        title="EXAMPLE!!",
        message="Add this function on script selenium",
        timeout=10
    )


def close_notification():
    time.sleep(10)
    notification.hide()


if __name__ == "__main__":
    show_notification()
    close_notification_thread = threading.Thread(target=close_notification)
    close_notification_thread.start()

# from win10toast import ToastNotifier
# import time
#
#
# def show_notification():
#     toaster = ToastNotifier()
#     toaster.show_toast(
#         "EXAMPLE!!",
#         "Add this function on script selenium",
#         duration=1  # Set the duration in seconds
#     )
#
#
# if __name__ == "__main__":
#     while True:
#         show_notification()
#         time.sleep(2)
