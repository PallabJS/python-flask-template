import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

wazirx = os.getenv("BASE_URI")
api_key = os.getenv("API_KEY")
secret_key = os.getenv("SECRET_KEY")
