import logging
import logging.handlers as handlers

logging.basicConfig(filename='app.log', 
                    format='%(name)s - %(levelname)s - %(message)s', 
                    encoding='utf-8', 
                    level=logging.DEBUG)

logHandler = handlers.RotatingFileHandler('app.log', maxBytes=10, backupCount=2)
logHandler.setLevel(logging.INFO)
logging.getLogger("myapp").addHandler(logHandler)