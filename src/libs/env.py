
import os


class Env:
    DEBUG = bool(int(os.getenv('DEBUG', False)))

    POSTGRES_URL = os.getenv('POSTGRES_URL', 'postgresql://root:abc321@localhost/robert_ai')
