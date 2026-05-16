import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "practice-secret-key")
    MAX_CONTENT_LENGTH = 4 * 1024 * 1024
    DEMO_USERS = {
        "student": "practice123",
        "admin": "camera456",
    }
