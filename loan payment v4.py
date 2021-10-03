import math
import argparse

parser = argparse.ArgumentParser(description="This program calculates your loan and payments.")
    
parser.add_argument("--type")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()

conjunto = [args.type, args.payment, args.principal, args.periods, args.interest]# hago este conjunto porque los objetos parser o args no son iterables


if args.type == "diff" and args.payment != None:
    print("Incorrect parameters")

elif args.interest == None:
    print("Incorrect parameters")

elif conjunto.count(None) > 1:
    print("Incorrect parameters")
      
elif args.type == "diff" or args.type == "annuity":
    
    if args.type == "diff":
        acumuladora = 0
        interés = (float(args.interest)/100)/12
        p = float(args.principal)
        n = int(args.periods)
        
        for i in range(1, int(args.periods) +1):
            D = (p / n) + interés * (p - (p * (i - 1))/n )
            print(f"Month {i}: payment is {math.ceil(D)}")
            acumuladora += math.ceil(D)
            
        print(f"\nOverpayment = {int(acumuladora - p)}")

    elif args.type == "annuity" and args.principal != None and args.payment == None:
        loan = float(args.principal)
        meses = int(args.periods)
        interés = (float(args.interest)/100)/12
        mensualidad = math.ceil(loan * ((interés * pow(1 + interés, meses))/(pow(1+ interés, meses)-1)))
        print(f"Your monthly payment = {mensualidad}!")
        print(f"Overpayment = {math.ceil(mensualidad * meses - loan)}")


    elif args.type == "annuity" and args.principal == None and args.payment != None:
        mensualidad = float(args.payment)
        meses = int(args.periods)
        interés = (float(args.interest)/100)/12
        loan = math.ceil(mensualidad / ((interés * math.pow(1 + interés, meses)/(math.pow(1 + interés, meses)-1))))
        print(f"Your loan principal = {loan}!")
        print(f"Overpayment = {(math.ceil(mensualidad * meses) - loan)}")
        

    elif args.type == "annuity" and args.principal != None and args.payment != None:
        loan = float(args.principal)
        mensualidad = float(args.payment)
        interés = ((float(args.interest))/ 100) / 12
        y = str()
        m = str()
        n = math.ceil(math.log(mensualidad/(mensualidad - interés * loan), 1+interés))
        if n > 12:
            y = str("s")
        if n % 12 != 0:
            m = str("s")
                
        print(f"It will take {n // 12} year{y} and {n % 12} month{m} to repay this loan!")
        print(f"Overpayment = {(int(math.ceil(mensualidad * n)) - loan)}")
                
else:
    print("Incorrect parameters")
