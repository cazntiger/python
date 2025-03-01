import webbrowser
import json
from urllib.request import urlopen

#print("let's find an old website")
#site = input("Type a website URL: ")
#era = input("Type a year, month, and day, like 20150613: ")

income_str = input("Please provide an income: ")
income = int(income_str)

TAXL1=23200
TAXL2=94300
TAXL3=201050
TAXL4=383900
TAXL5=487450
TAXL6=731200

TAXL1R=0.1
TAXL2R=0.12
TAXL3R=0.22
TAXL4R=0.24
TAXL5R=0.32
TAXL6R=0.35
TAXL7R=0.37

def calculateTaxL1(income, taxr):
    tax = income*taxr
    return tax

if income <= TAXL1:
    calc_tax = calculateTaxL1(income, TAXL1R)
    print("income tax: ", calc_tax)

    