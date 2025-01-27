import logging
import os
from datetime import datetime

log_file = f"{datetime.now().strftime("%Y-%m-%d") }.log"
log_path = os.path.join (os.get cwd(), "logs", log_file)
os.makedirs(os.path.dirname(log_path), exist_ok=True)           

log_file_path= os.path.join(log_path, log_file)  

logging.basicConfig(
    
filename=log_file_path, 
format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
level=logging.INFO,


)    