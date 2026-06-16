def validate_login(username, password):
    """Return True if username and password are valid for login.

    Args:
        username: The username string.
        password: The password string.

    Returns:
        True if both strings are non-empty and the password is at least
        8 characters long; otherwise False.
    """
    if not username or not password:
        return False
    return len(password) >= 8
