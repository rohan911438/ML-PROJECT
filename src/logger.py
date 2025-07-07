import logging 

import os
from datetime import datetime
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(os.path.dirname(logs_path), exist_ok=True)

LOG_FILE_PATH= os.path.join(os.getcwd(), "logs", LOG_FILE)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
)

if __name__ == "__main__":
    logging.info("Logging has been set up successfully.")
    