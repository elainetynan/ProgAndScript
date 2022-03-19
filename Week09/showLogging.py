# showLogging.py
#
# Trying out logging
#
# Andrew Beatty

import logging

# Default is at warning level
#logging.basicConfig(level=logging.DEBUG)

# To send debugging messages to a file (You can only run basic config once)
logging.basicConfig(filename="Debugging.log",
                    filemode="w", # a = append, w = write
                    level=logging.DEBUG,
                    format ="%(asctime)s - %(name)s -%(levelname)s - %(message)s - line: %(lineno)d")

# Levels are (From Highest to lowest):
# Critical, Error, Warning, Info, Debug

name = "Elaine"
logging.critical("This is a critical error")
logging.error("This is an error")
logging.warning("This is a warning, name is %s", name)
logging.info("This is an info message")
logging.debug("This is a debugging message")