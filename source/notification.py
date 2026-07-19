class EmailService:

    def send_email(self, email, message):
        print(f"Email sent to {email}")


def notify_user(email):

    service = EmailService()

    service.send_email(
        email,
        "Welcome to Pytest!"
    )

    return "Notification Sent"