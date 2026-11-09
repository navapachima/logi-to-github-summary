import os
from dotenv import load_dotenv  

DEFAULT_TIMEOUT_MS = int(os.getenv("DEFAULT_TIMEOUT_MS", 15000))

load_dotenv()

GITHUB_URL = "https://www.github.com"
TEST_USERNAME_GITHUB = os.getenv("NAVA_USERNAME_GITHUB")
TEST_PASSWORD_GITHUB = os.getenv("NAVA_PASSWORD_GITHUB")

