class Notification:

    def get_notification(self):
        pass
class Instagram(Notification):
    def get_notification(self):
        print("Notification from instagram")

instagram=Instagram()
instagram.get_notification()