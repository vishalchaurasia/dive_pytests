from unittest.mock import MagicMock

from source.orders import OrderService


def test_place_order():

    # Create a fake EmailService
    mock_email_service = MagicMock()

    # Inject fake dependency
    order_service = OrderService(mock_email_service)

    # Execute
    result = order_service.place_order(
        "example@test.com",
        "Laptop"
    )

    # Verify business result
    assert result == "SUCCESS"

    # Verify email was "called"
    mock_email_service.send_email.assert_called_once_with(
        "example@test.com",
        "Your order for Laptop has been placed."
    )