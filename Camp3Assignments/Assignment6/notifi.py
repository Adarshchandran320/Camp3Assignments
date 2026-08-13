from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message, recipient):
        pass

class EmailNotification(Notification):
    def send(self, message, recipient):
        print(f"[EMAIL] Sending email to '{recipient}'...")
        print(f"Content: {message}")
        print("Email delivered successfully!\n")


class SMSNotification(Notification):
    def send(self, message, recipient):
        print(f"[SMS] Sending text message to phone number '{recipient}'...")
        print(f"Content: {message}")
        print("SMS sent via cellular network!\n")


class PushNotification(Notification):
    def send(self, message, recipient):
        print(f"[PUSH] Sending app banner alert to User ID '{recipient}'...")
        print(f"Content: {message}")
        print("Push notification delivered to device screen!\n")



email = EmailNotification()
sms = SMSNotification()
push = PushNotification()

email.send("Your OTP is 4921", "user@example.com")
sms.send("Your package has arrived!", "+1-555-0192")
push.send("You have a new friend request!", "user_id_881")