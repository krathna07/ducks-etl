import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
TARGET_STATE = os.getenv("TARGET_STATE", "CA")
DU_API_URL = os.getenv("DU_API_URL", "https://www.ducks.org/api/university-chapters")
