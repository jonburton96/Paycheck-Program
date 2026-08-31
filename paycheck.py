#jonathan burton
#paycheck program

def main():

    #intialize
    hourlyPay  = float(0.0)
    hoursWorked = float(0.0)
    grossPay = float(0.0)
    totalGross = float (0.0)
    SS_RATE = float(.062)
    MEDICARE_RATE = float(.0145)
    annuityContrib = float(0.0)
    annuityEmployer = float(0.0)
    annuityBalance = float(0.0)
    
    socialTax = float(0.0)
    medicareTax = float(0.0)
    totalDeduction = float(0.0)
    toalNet = float(0.0)
    overtimeHours = float(0.0)
    overtimePay = float(0.0)
    overtimeRate= float(0.0)
    newAnnuity = float(0.0)

    #input
    hourlyPay = float(input("What's your pay rate?"))
    hoursWorked  = float(input("How many hours worked?"))
    annuityContrib = float(input("Annuity amount contribution?"))
    annuityBalance = float(input("Current annuity balance?"))


     #process
    if hoursWorked > 40:
        (hoursWorked- 40)*1.5

    if annuityContrib <= 50:
        annuityEmployer = annuityContrib
    else:
        annuityEmployer = 50
        
    overtimeHours = hoursWorked - 40
    overtimePay = overtimeHours*(1.5 *hourlyPay)
    overtimeRate = 22.5*1.5
    hoursWorked = hoursWorked - overtimeHours
    grossPay = hoursWorked * hourlyPay
    totalGross =  grossPay + overtimePay
    socialTax = totalGross *SS_RATE
    medicareTax = totalGross * MEDICARE_RATE
    totalDeduction= medicareTax + socialTax+annuityContrib
    totalNet = totalGross - totalDeduction
    newAnnuity = annuityEmployer+annuityContrib+annuityBalance
    annuityBalance = newAnnuity-annuityEmployer-annuityContrib

    #print
    print()
    print(f"Employee: {'Quincy'} {'Full Time'}")
    print()
    print(f"BUC-EE'S: WEEKLY PAY CHECK")
    print(f"-------- - --- ------ --- -----")
    print()
    print(f"Regular Time Calculations")
    print(f"{'Hourly Pay Rate:':>18}{hourlyPay:>13,.2f}")
    print(f"{'Hours Worked:':>15}{hoursWorked:>16,.2f}")
    print(f"{'Gross Regular Pay:':>20}{'$':>4}{grossPay:>7,.2f}")
    print()
    print (f"Overtime Calculations")
    print (f" {'Hourly OT Pay Rate:':>20} {overtimeRate:>9,.2f}")
    print (f" {'Hours OT Worked:':>17} {overtimeHours:>12,.2f}")
    print (f" {'Gross OT Pay:':>14}{'$':>9} {overtimePay:>4,.2f}")
    print()
    print (f"{'Total Gross Pay:'}{'$':>7} {totalGross:>7}")     
    print()
    print(f"Deduction Calculations")
    print(f"{'SSI Tax:':>10} {socialTax:>20,.2f}")
    print(f"{'Medicare Tax:':>15} {medicareTax:>15,.2f}")
    print(f"{'Annuity Savings:':>18} {annuityContrib:>12,.2f}")
    print(f"{'Total Deduction:':>18}{'$':>6}{totalDeduction:>7,.2f}")
    print()
    print(f"{'Total Net Pay:'}{'$':>10}{totalNet:>7,.2f}")
    print()
    print(f"Annuity Calculations")
    print(f"{'Previous Balance:':>19}{'$':>5} {annuityBalance:>5,.2f}")
    print(f"{'Emp. Contribution:':>20}{'$':>4} {annuityContrib:>6,.2f}")
    print(f"{'Company Match:':>16}{'$':>8}{annuityEmployer:>7,.2f}")
    print(f"{'New Balance:':>14}{'$':>10}{newAnnuity:>7,.2f}")
    
    
    
    
main()
