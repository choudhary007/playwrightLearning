from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://the-internet.herokuapp.com")
USERNAME = os.getenv("APP_USERNAME", "tomsmith")
PASSWORD = os.getenv("APP_PASSWORD", "SuperSecretPassword!")

# BASE_URL = os.getenv("BASE_URL", "https://the-internet.herokuapp.com")
# USERNAME = os.getenv("USERNAME", "tomsmith")
# PASSWORD = os.getenv("PASSWORD", "SuperSecretPassword!")