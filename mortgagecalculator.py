L = float(input("Enter the loan amount, in dollars: "))
R = float(input("Enter the annual interest, in percent: "))
M = int(input("Enter the loan duration, in months: "))

r = R/100/12
P = L*r*pow(1+r,M)/((pow(1+r,M))-1)
B = L
CIP = 0
CPP = 0

for i in range(1,M+1):
    monthly_principal = P -B*r
    monthly_paid_interest = B*r
    B = B - monthly_principal
    print(i, monthly_principal, monthly_paid_interest, B)
    CIP = monthly_paid_interest + CIP
    CPP = monthly_principal + CPP
    
print (L, R, M, r*100, P, CPP, CIP+CPP)