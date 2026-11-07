try:
	from pymongo import MongoClient
except ImportError as e:
	raise ImportError(
		"pymongo no está instalado. Instálalo con: pip install pymongo"
	) from e
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))

db = client[os.getenv("DATABASE_NAME")]
