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

    w2_income_str = input("Your w2 income: ")
    w2_income = int(w2_income_str)

    interests_str = input("You taxable interests earnings: ")
    interests = int(interests_str)

    dividends_str = input("Your stock dividends: ")
    dividends = int(dividends_str)

    capital_gains_str = input("Your capital gains: ")
    capital_gains = int(capital_gains_str)

    other_income_str = input("Other income: ")
    other_income = int(other_income_str)

    retirement_contributions_str = input("Retirement contributions: ")
    retirement_contributions = int(retirement_contributions_str)

    standard_deduction_str = input("Standard deduction: ")
    standard_deduction = int(standard_deduction_str)
    
    total_income = w2_income + interests + dividends + capital_gains + other_income

    adjusted_gross_income = total_income - retirement_contributions

    taxable_income = adjusted_gross_income - standard_deduction


    w2_stateTax = calculateTax(w2_income, STATER)
    w2_taxWithheld = 0.12*w2_income

    if taxable_income <= TAXL1:
        calc_tax = calculateTax(taxable_income, TAXL1R)
    elif taxable_income <= TAXL2:
        calc_tax = calculateTax(TAXL1, TAXL1R) + calculateTax(taxable_income-TAXL1, TAXL2R)
    elif taxable_income <= TAXL3:
        calc_tax = calculateTax(TAXL1, TAXL1R) + calculateTax(TAXL2-TAXL1, TAXL2R) + calculateTax(taxable_income-TAXL2, TAXL3R)
    elif taxable_income <= TAXL4:
        calc_tax = calculateTax(TAXL1, TAXL1R) + calculateTax(TAXL2-TAXL1, TAXL2R) + calculateTax(TAXL3-TAXL2, TAXL3R) + calculateTax(taxable_income-TAXL3, TAXL4R)
    elif taxable_income <= TAXL5:
        calc_tax = calculateTax(TAXL1, TAXL1R) + calculateTax(TAXL2-TAXL1, TAXL2R) + calculateTax(TAXL3-TAXL2, TAXL3R) + calculateTax(TAXL4-TAXL3, TAXL4R) + calculateTax(taxable_income-TAXL4, TAXL5R)
    elif taxable_income <= TAXL6:
        calc_tax = calculateTax(TAXL1, TAXL1R) + calculateTax(TAXL2-TAXL1, TAXL2R) + calculateTax(TAXL3-TAXL2, TAXL3R) + calculateTax(TAXL4-TAXL3, TAXL4R) + calculateTax(TAXL5-TAXL4, TAXL5R) + calculateTax(taxable_income-TAXL5, TAXL6R)
    else:
        calc_tax = calculateTax(TAXL1, TAXL1R) + calculateTax(TAXL2-TAXL1, TAXL2R) + calculateTax(TAXL3-TAXL2, TAXL3R) + calculateTax(TAXL4-TAXL3, TAXL4R) + calculateTax(TAXL5-TAXL4, TAXL5R) + calculateTax(TAXL6-TAXL5, TAXL6R) + calculateTax(taxable_income-TAXL6, TAXL7R)

    stateTax = 0.06*taxable_income

    print("The total federal tax is: ", calc_tax)
    print("The total state tax is: ", stateTax)
    print("The total tax is: ", calc_tax+stateTax)
    print("The income before federal tax is: ", taxable_income)
    print("The income after federal tax is: ", taxable_income-calc_tax)
    print("The income after federal and state tax is: ", taxable_income-calc_tax-stateTax)
    print("The withholding tax is: ", w2_taxWithheld)

    if w2_taxWithheld > calc_tax+stateTax:
        print("You will get a refund of: ", w2_taxWithheld-calc_tax-stateTax)
    else:
        print("You owe: ", calc_tax+stateTax-w2_taxWithheld)

    program_run = input("Do you want to run the program again? (yes/no): ")
    if program_run == "no":
        program_run = False
    else:
        program_run = True

#webbrowser.open("http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era))

    