import logging
import os
from datetime import datetime


LOG_FILE=f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

log_path=os.path.join(os.getcwd(),"logs")

os.makedir(log_path,exit_ok=True)

LOG_FILEPATH=os.path.join(log_path,LOG_FILE)

logging.basicConfig(level=logging.INFO,
                    filename=LOGFILE_PATH,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"

)



