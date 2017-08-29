"""configuration loader
should be imported in all modules in need for configuration elements
"""

import json
from os import environ
fp = open(environ["ROSHAMBO_CONFFILE"],"r")
conf = json.load(fp, "UTF-8")
fp.close()
