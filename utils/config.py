import os
from dotenv import load_dotenv

load_dotenv()

env = os.environ

mongo_uri = env.get("MONGO_URI")
mongo_db = env.get("MONGO_DB")

envValues = {
    "mongo": {
        "uri": mongo_uri,
        "db": mongo_db
    }
}
