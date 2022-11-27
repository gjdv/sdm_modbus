import os
import sys

sdm_modbus_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
try:
    sys.path.index(sdm_modbus_dir)
except ValueError:
    print("Added sdm_modbus to python path")
    sys.path.append(sdm_modbus_dir)

from sdm_modbus.meter import *
from sdm_modbus.sdm import *
from sdm_modbus.garo import *
from sdm_modbus.espp1 import *
