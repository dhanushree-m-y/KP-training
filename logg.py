import logging

import logging

logging.basicConfig(level=logging.DEBUG,)
logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")


password="abc123"
user_input="abc123"

logging.debug("user eneter the pasword ",user_input)

if user_input == password:
    logging.info("pasword right")
else:
    logging.warning("password wrong")