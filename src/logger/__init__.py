import logging
import os, sys
from datetime import datetime  

log_dir= "logs"
log_dir= os.path.join(os.getcwd(), log_dir)

os.makedirs(log_dir, exist_ok=True)

current_time_stamp = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
file_name = f"log_{current_time_stamp}.log"
log_file=os.path.join(log_dir,file_name)

logging.basicConfig(filename=log_file,
                    filemode="w",
                    format= '%(asctime)s :: %(levelname)s :: %(message)s',
                    level=logging.INFO)    