"""
Logging levels
Debug
info
warning
error
critical
"""

import logging



logging.basicConfig(filename="test.log", level=logging.DEBUG)
logging.warning("warning message")
logging.info('info message')
logging.error('error message')