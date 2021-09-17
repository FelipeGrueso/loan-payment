import math

acción = input("""WWhat do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:""")


if acción == "n":
    loan = float(input("Enter the loan principal:"))
    mensualidad = float(input("Enter the monthly payment: "))
    interés = ((float(input("Enter the loan interest:")))/ 100) / 12
    y = str()
    m = str()
    n = math.ceil(math.log(mensualidad/(mensualidad - interés * loan), 1+interés))
    if n > 12:
        y = str("s")
    if n % 12 != 0:
        m = str("s")
            
    print(f"It will take {n // 12} year{y} and {n % 12} month{m} to repay this loan!")


if acción == "a":
    loan = float(input("Enter the loan principal:"))
    meses = float(input("Enter the number of periods: "))
    interés = (float(input("Enter the loan interest:"))/ 100) / 12
    mensualidad = math.ceil(loan * ((interés * pow(1 + interés, meses))/(pow(1+ interés, meses)-1)))
    print(f"Your monthly payment = {mensualidad}!")

   
                   
if acción == "p":
    mensualidad = float(input("Enter the annuity payment: "))
    meses = float(input("Enter the number of periods:"))
    interés  = (float(input("Enter the loan interest:")) / 100) / 12
    loan = round(mensualidad / ((interés * math.pow(1 + interés, meses)/(math.pow(1 + interés, meses)-1))))
    print(f"Your loan principal ={loan}!")



    
    
