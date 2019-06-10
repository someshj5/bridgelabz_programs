import Util                                      # importing Util module
import sys                                       # importing sys module

day = int(sys.argv[1])                          # Asks for command line input day
month = int(sys.argv[2])                        # Asks for command line input
year = int(sys.argv[3])                         # Asks for command line input
Util.Utilities.dayofWeek(day,month,year)        # Calls the staticmethod from the Utilities class to calculate day of week