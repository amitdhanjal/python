import traceback
import os
import datetime
from datetime import datetime

def exception_logger():
	exception_log = traceback.format_exc().splitlines()
	exception_log.append(str(datetime.now()))
	print(exception_log)
	return exception_log
