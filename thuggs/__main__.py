from .app import Thuggs
import sys
import os
os.environ["SETTINGS_MODULE"] = 'settings'

# get commandline arguments to detect either cats or humans
identification_type = sys.argv[1]

if __name__ == '__main__':
    Thuggs.run(identification_type)
