
import logging
from datetime import datetime

log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)



    
import logging

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    logging.info("Logging is started")
