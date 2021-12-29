import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

env = os.getenv("ENV")

wazirx = os.getenv("BASE_URI")
api_key = os.getenv("API_KEY")
secret_key = os.getenv("SECRET_KEY")


# MongoDB variables

mongo_uri = "mongodb://127.0.0.1:27017/test"
if(env == "production"):
    mongo_uri = os.getenv("MONGO_URI")
