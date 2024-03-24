
import math

def isfloat(str_ing):
    ch_eck = "0123456789."
    r_e = True
    if str_ing[0] == '.':
        r_e = False
        return r_e
    c_ount = 0
    for i in str_ing:
        if i == '.':
            c_ount += 1
        for y in ch_eck:
            if i == y:
                break
            if y == '.':
                r_e = False
        if c_ount > 1:
            r_e = False
            break
    return r_e

# using print() function print out menu option
# and through input() function take information from the user
print("investment - to calculate the amount of interest you'll earn to your investment.")
print("bond       - to calculate the amount you'll have to pay on a home loan. \n")
in_vestment_raw = input("Enter either 'investment' or 'bond' from the menu above to proceed:")
in_vestment = in_vestment_raw.lower()

# using while loop check if entered value is correct
while  not in_vestment.isalpha or (in_vestment != "bond" and in_vestment != "investment"):
    in_vestmentraw = input("Enter 'inverstment' or 'bond':")
    in_vestment = in_vestmentraw.lower()

#reprint what is the user's choice
print(f"\nYou choice is {in_vestment}")

# using if statment check the choice and take the rest of the informatin from the user
# 'amount of money' and the 'rate' cast into float, the 'years' and 'months' into integer
# calculate the amount of intrest or bond
# the result print out at the end of each ifbranch, and round it into 2 decimal places
if in_vestment == "investment":
    P_raw = input("Enter amount of money you wish to deposite:")
    while not isfloat(P_raw) or float(P_raw) <= 0:
        P_raw = input("Enter valid amount of money:")
    P = float(P_raw)

    r_raw = input("Enter interest rate:")
    while not isfloat(r_raw) or float(r_raw)<0:
        r_raw = input("Enter valid interest rate:")
    r = float(r_raw)/100

    y_raw = input("Enter period in years:")
    while not y_raw.isdigit() or int(y_raw) < 0:
        y_raw = input("Enter valid period of investment:")
    t = int(y_raw)
    intr_raw = input("What kind of interest you choose ('simple' or 'compound'):")
    intr = intr_raw.lower()
    while  not intr.isalpha or (intr != "simple" and intr != "compound"):
        intr_raw = input("Enter 'simple' or 'compund':")
        intr = intr_raw.lower()

    if intr == "simple":
        A = P * (1 + r * t)
    elif intr == "compound":
        A = P * math.pow((1+r),t)
    print("Your intrest is ", format(A,".2f"))

elif in_vestment == "bond":
    P_b_raw = input("Enter the present value of the house:")
    while not isfloat(P_b_raw) or float(P_b_raw) < 0:
        P_b_raw = input("Enter valid house value:")
    P_b = float(P_b_raw)
    r_raw = input("Enter interest rate:")
    while not isfloat(r_raw) or float(r_raw)<=0:
        r_raw = input("Enter valid interest rate:")
    r = float(r_raw)/1200
    m_raw = input("Enter the number of months you plan to repay the bond(e.g.120):")
    while not m_raw.isdigit() or int(m_raw) <= 0:
        m_raw = input("Enter positive number of months:")
    m = int(m_raw)
    re_payment = (r * P_b)/(1 - (1 + r) ** (-m))
    print("You have to pay", format(re_payment,".2f"), "each month")
    