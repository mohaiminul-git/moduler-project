from src.logger import logging

log_file = "my_log.log"

logging.debug("This is a DEBUG message.")   # Will not be logged (INFO level is set)
logging.info("This is an INFO message.")    # ✅ Logged
logging.warning("This is a WARNING message.")  # ✅ Logged
logging.error("This is an ERROR message.")  # ✅ Logged
logging.critical("This is a CRITICAL message.")  # ✅ Logged

print(f"Logs have been written to {log_file}")

