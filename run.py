import logging.config
import os

log_config = os.path.join(os.path.dirname(__file__), "logger.conf")
logging.config.fileConfig(log_config, disable_existing_loggers=False)

from floater import app

app.run(host="0.0.0.0", port=4099, threaded=True, debug=False)
