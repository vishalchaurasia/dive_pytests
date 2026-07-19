from unittest.mock import patch

from source.notification import notify_user


@patch("source.notification.EmailService")
def test_notify_user(mock_email_class):

    result = notify_user("example@test.com")

    assert result == "Notification Sent"

    mock_email_class.return_value.send_email.assert_called_once_with(
        "example@test.com",
        "Welcome to Pytest!"
    )
