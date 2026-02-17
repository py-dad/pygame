
from dotenv import load_dotenv
import os

# reference data in another file .env
# good for hiding API secrets, etc

load_dotenv()
# environment variables

#os look for python in the printed folders
print(os.getenv("PATH"))
API_KEY = os.getenv("API_KEY")
EMAIL_ADDR = os.getenv("EMAIL_ADDR")
PASSWORD = os.getenv("PASSWORD")

print(API_KEY)
print(EMAIL_ADDR)
print(PASSWORD)



