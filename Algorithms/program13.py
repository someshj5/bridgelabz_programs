import Util
import sys
'''
    It takes input amount P and calculates the monthly payments
    you would have to make over Y years to pay off a P principal loan amount
    at R per cent interest 
    Pass All Three Input To The Util Function calcPayment()
    '''


def calcPayment():
    P = float(input('Enter a Principle amount:')) #Ask for P input
    Y = float(input('Enter the years for tenure:')) # Ask for Y input
    R = float(input('Enter the rate of interest:')) # Ask for R input
    Util.Utilities.calculatePayment(P,Y,R) #Call Util Function And Pass The Inputs
    return
    

calcPayment()# Function call