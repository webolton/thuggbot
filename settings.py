import os
from pathlib import Path
from dotenv import load_dotenv

THUGGBOT_ENV = os.getenv('THUGGBOT_ENV')  # set production or leave blank

load_dotenv(verbose=True)

if THUGGBOT_ENV == 'production':
    env_path = Path('.') / '.env.production'
else:
    env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

HAARCASCADE_URL=os.getenv('HAARCASCADE_URL')
