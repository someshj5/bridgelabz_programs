import Util

def TempConversion():
    temp = int(input('Enter a number:\n')) # Ask input as temperature
    n = int(input('Enter n = 0 for Celcius or n = 1 for Fahrenheit conversion:')) # Ask for conversion in Celcius or Fahrenhiet
    Util.Utilities.Temp_conversion(temp,n)  # Call Util Function And Pass The Inputs
    return 

TempConversion() # Function call