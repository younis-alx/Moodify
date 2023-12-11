from os import getenv
from os.path import dirname, abspath

from dotenv import load_dotenv

load_dotenv()

storage = getenv("STORAGE")

if storage == "db":
    # Will be added on later adaptations
    pass
else:
    from backend.load.storage import Storage
    storage = Storage(storage_path=abspath(
        dirname(dirname(__file__))) + '/storage.json')
