from ..config import Config


def verify_credentials(username: str, password: str) -> bool:
    expected_password = Config.DEMO_USERS.get(username.strip().lower())
    return expected_password is not None and expected_password == password
