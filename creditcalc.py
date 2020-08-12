#imports
import math
import argparse

#variables
#credit_principal = 0
#interest = 0
#mon_1 = 0
#pay_1 = 0
remainder = 0
years = 0
type_command = ""
n_a_p = ""
count = 0
count2 = 0
count3 = 0
diff_out = 0
diff_extra = 0

#take command input
parser = argparse.ArgumentParser()
parser.add_argument("--type", help="will calculate the month differential", type=str, choices=["diff", "annuity"])
parser.add_argument("--payment", help="the desired monthly payment", type=float, default=0)
parser.add_argument("--periods", help="how many months it will be paid over", type=int, default=0)
parser.add_argument("--interest", help="the interest you produce on remaining payments per month in /%", type=float, default=0)
parser.add_argument("--principal", help="total loan payment before interest", type=int, default=0)
args = parser.parse_args()
mon_1 = args.periods
pay_1 = args.payment
interest = args.interest
credit_principal = args.principal

#testing
"""
print(mon_1)
print(pay_1)
print(interest)
print(credit_principal)
"""

#check for proper command input
if args.type != "diff":
    if args.type != "annuity":
        print("Incorrect parameters")
        mon_1 = 1
        pay_1 = 1
        credit_principal = 1
if credit_principal == 0:
    count += 1
if mon_1 == 0:
    count += 1
if pay_1 == 0:
    count += 1
if interest == 0:
    count += 2
if count >= 2:
    mon_1 = 1
    pay_1 = 1
    credit_principal = 1
    print("Incorrect parameters")

#idk why but this makes it work
pay_1 = (float(pay_1))


#define differential
def diff_1(p, m, n, i):
    global diff_out
    var10 = i * (p - ((p * (m - 1)) / n))
    var11 = (p / n)
    diff_out = var11 + var10


#output calculation for annuity
if args.type == "annuity":
    if mon_1 == 0:
        var3 = (float(interest)/100) / 12
        var2 = (pay_1 / (pay_1 - (var3 * credit_principal)))
        var1 = math.log(var2, (1 + var3))
        mon_1 = math.ceil(var1)
        overpay = math.ceil((pay_1 * mon_1) - credit_principal)
        while mon_1 >= 12:
            mon_1 -= 12
            years += 1
        if mon_1 == 0:
            print("You need %i years to repay this credit!" % years)
        elif years == 0:
            if mon_1 == 1:
                print("You need %i month to repay this credit!" % mon_1)
            elif mon_1 >> 1:
                print("You need %i months to repay this credit!" % mon_1)
        else:
            if mon_1 == 1:
                print("You need ", years, " years and", mon_1, " month to repay this credit!")
            elif mon_1 >> 1:
                print("You need ", years, " years and ", mon_1, " months to repay this credit!")
        print("Overpayment = {}".format(overpay))
    elif pay_1 == 0:
        var3 = (float(interest)/100) / 12
        var4 = pow(var3 + 1, mon_1)
        var2 = (var3 * var4) / (var4 - 1)
        var1 = credit_principal * var2
        pay_1 = math.ceil(var1)
        overpay = math.ceil((pay_1 * mon_1) - credit_principal)
        print("Your annuity payment = %i" % pay_1)
        print("Overpayment = {}".format(overpay))

    elif credit_principal == 0:
        var3 = (float(interest)/100) / 12
        var4 = pow(var3 + 1, mon_1)
        var2 = (var3 * var4) / (var4 - 1)
        credit_principal = pay_1 / var2
        overpay = math.ceil((pay_1 * mon_1) - credit_principal)
        print("Your credit principal = %i" % credit_principal)
        print("Overpayment = {}".format(overpay))

#output calculation for diff
if args.type == "diff":
    if mon_1 == 0:
        var3 = (float(interest)/100) / 12
        var2 = (pay_1 / (pay_1 - (var3 * credit_principal)))
        var1 = math.log(var2, (1 + var3))
        mon_1 = math.ceil(var1)
        #overpay = math.ceil((pay_1 * mon_1) - credit_principal)
        count2 = mon_1
        count3 = 1
        while count2 != 0:
            diff_1(credit_principal, count3, mon_1, var3)
            diff_extra += diff_out
            diff_out = math.ceil(diff_out)
            print("Month {}: paid out {}".format(count3, diff_out))
            count3 += 1
            count2 -= 1
        overpay = (pay_1 * mon_1) - diff_extra
        overpay = math.ceil(overpay)
        print("")
        print("Overpayment = {}".format(overpay))
    elif pay_1 == 0:
        var3 = (float(interest)/100) / 12
        var4 = pow(var3 + 1, mon_1)
        var2 = (var3 * var4) / (var4 - 1)
        var1 = credit_principal * var2
        pay_1 = var1
        #overpay = math.ceil((pay_1 * mon_1) - credit_principal)
        count2 = mon_1
        count3 = 1
        while count2 != 0:
            diff_1(credit_principal, count3, mon_1, var3)
            diff_out = math.ceil(diff_out)
            diff_extra += diff_out
            print("Month {}: paid out {}".format(count3, diff_out))
            count3 += 1
            count2 -= 1
        overpay = diff_extra - credit_principal
        overpay = math.ceil(overpay)
        print("")
        print("Overpayment = {}".format(overpay))
    elif credit_principal == 0:
        var3 = (float(interest)/100) / 12
        var4 = pow(var3 + 1, mon_1)
        var2 = (var3 * var4) / (var4 - 1)
        credit_principal = pay_1 / var2
        #overpay = math.ceil((pay_1 * mon_1) - credit_principal)
        count2 = mon_1
        count3 = 1
        while count2 != 0:
            diff_1(credit_principal, count3, mon_1, var3)
            diff_extra += diff_out
            diff_out = math.ceil(diff_out)
            print("Month {}: paid out {}".format(count3, diff_out))
            count3 += 1
            count2 -= 1
        overpay = (pay_1 * mon_1) - diff_extra
        overpay = math.ceil(overpay)
        print("")
        print("Overpayment = {}".format(overpay))
