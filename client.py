#!/usr/bin/env python
import os
import subprocess
import sys

from config.config import Config


sys.path.insert(0, os.getcwd())


# Get the args
def main():
    # Clear the screen
    subprocess.call('clear', shell=True)
    config_object = Config(os.getcwd() + '/config/config.ini').raw_config_object

    try:

        while True:
            '''
            do stuff
            '''
            print('\nPrint doing stuff\n')

    except LookupError as e:
        print(e)
        sys.exit(2)

    except KeyboardInterrupt:
        print('keyboard interruption')
        sys.exit(1)


if __name__ == "__main__":
    main()