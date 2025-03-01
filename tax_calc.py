#print("let's find an old website")
#site = input("Type a website URL: ")
#era = input("Type a year, month, and day, like 20150613: ")
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

STATER=0.06

def calculateTax(income, taxr):
    tax = income*taxr
    return tax

program_run = True
while program_run:
    print("Welcome to the income calculator.  Please provide an income to calculate the tax.")

    income_str = input("Your income: ")
    income = int(income_str)

    if income <= TAXL1:
        calc_tax = calculateTax(income, TAXL1R)
    elif income <= TAXL2:
        calc_tax = calculateTax(TAXL1, TAXL1R) + calculateTax(income-TAXL1, TAXL2R)
    elif income <= TAXL3:
        calc_tax = calculateTax(TAXL1, TAXL1R) + calculateTax(TAXL2-TAXL1, TAXL2R) + calculateTax(income-TAXL2, TAXL3R)
    elif income <= TAXL4:
        calc_tax = calculateTax(TAXL1, TAXL1R) + calculateTax(TAXL2-TAXL1, TAXL2R) + calculateTax(TAXL3-TAXL2, TAXL3R) + calculateTax(income-TAXL3, TAXL4R)
    elif income <= TAXL5:
        calc_tax = calculateTax(TAXL1, TAXL1R) + calculateTax(TAXL2-TAXL1, TAXL2R) + calculateTax(TAXL3-TAXL2, TAXL3R) + calculateTax(TAXL4-TAXL3, TAXL4R) + calculateTax(income-TAXL4, TAXL5R)
    elif income <= TAXL6:
        calc_tax = calculateTax(TAXL1, TAXL1R) + calculateTax(TAXL2-TAXL1, TAXL2R) + calculateTax(TAXL3-TAXL2, TAXL3R) + calculateTax(TAXL4-TAXL3, TAXL4R) + calculateTax(TAXL5-TAXL4, TAXL5R) + calculateTax(income-TAXL5, TAXL6R)
    else:
        calc_tax = calculateTax(TAXL1, TAXL1R) + calculateTax(TAXL2-TAXL1, TAXL2R) + calculateTax(TAXL3-TAXL2, TAXL3R) + calculateTax(TAXL4-TAXL3, TAXL4R) + calculateTax(TAXL5-TAXL4, TAXL5R) + calculateTax(TAXL6-TAXL5, TAXL6R) + calculateTax(income-TAXL6, TAXL7R)

    stateTax = calculateTax(income, STATER)
    # stateTax = 2000
    taxWithheld = 0.12*income

    print("The total federal tax is: ", calc_tax)
    print("The total state tax is: ", stateTax)
    print("The total tax is: ", calc_tax+stateTax)
    print("The income before federal tax is: ", income)
    print("The income after federal tax is: ", income-calc_tax)
    print("The income after federal and state tax is: ", income-calc_tax-stateTax)
    print("The withholding tax is: ", taxWithheld)

    if taxWithheld > calc_tax+stateTax:
        print("You will get a refund of: ", taxWithheld-calc_tax-stateTax)
    else:
        print("You owe: ", calc_tax+stateTax-taxWithheld)

    program_run = input("Do you want to run the program again? (yes/no): ")
    if program_run == "no":
        program_run = False
    else:
        program_run = True

#webbrowser.open("http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era))

    