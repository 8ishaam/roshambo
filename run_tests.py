#!/usr/bin/python

"""Main script to run unit tests
"""

from os import environ, path
import sys
environ["ROSHAMBO_CONFFILE"] = path.join(path.abspath(path.curdir), "conf.json")
sys.path.append("src")
sys.path.append("test")

# Here we run the tests: for instance in our case the small tests done on the playgame state
from test_fsm.test_states import *
suite = unittest.TestLoader().loadTestsFromTestCase(TestPlayGameState)
unittest.TextTestRunner(verbosity=2).run(suite)
