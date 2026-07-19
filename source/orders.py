class EmailService:

    def send_email(self, customer_email, message):
        """
        Imagine this method sends a real email.
        """
        print(f"Email sent to {customer_email}")


class OrderService:

    def __init__(self, email_service):
        self.email_service = email_service

    def place_order(self, customer_email, item):

        # Business logic
        order_status = "SUCCESS"

        # Notify customer
        self.email_service.send_email(
            customer_email,
            f"Your order for {item} has been placed."
        )

        return order_status