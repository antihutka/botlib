from configparser import ConfigParser
import sys

Config = ConfigParser()

def read_config():
  if len(sys.argv) != 2:
    raise Exception("Wrong number of arguments")
  Config.read(sys.argv[1])
