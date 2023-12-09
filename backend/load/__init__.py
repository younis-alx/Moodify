from os import getenv

from dotenv import load_dotenv

load_dotenv()

storage = getenv("STORAGE")

if storage == "db":
    # Will be added on later adaptations
    pass
else:
    from .storage import Storage
    storage = Storage('../../storage.json')