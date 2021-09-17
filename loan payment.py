loan = int(input("Enter the loan principal:"))
acción = input("""WWhat do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment""")

if acción == "m":
    mensualidad = int(input("Enter the monthly payment:"))
    s =str()
    if loan//mensualidad >1:
        s = str("s")
    print(f"It will take {round(loan / mensualidad)} month{s} to repay the loan")
               
if acción == "p":
    meses = int(input("Enter the number of months:"))
    if loan % meses == 0:
        
        print(f"Your monthly payment = {loan//meses}")
    else:
        redondeo = loan // meses + 1
        print(f"Your monthly payment = {redondeo} and the last payment = {loan - (meses - 1)* redondeo}.")  
