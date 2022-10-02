# Loan_calculator

JetBrains Academy mathematical project for calculating annuity payment or differential payments of the loan data you provide through the command line such as loan principal, interest, monthly payment.

# description / input options:

$ python3 creditcalc.py -h 

For successful execution of the program, you must specify at least 4 input parameters.

# Example user input: calculating differentiated payments

$ python3 creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10

Month 1: payment is 108334
Month 2: payment is 107500
Month 3: payment is 106667
Month 4: payment is 105834
Month 5: payment is 105000
Month 6: payment is 104167
Month 7: payment is 103334
Month 8: payment is 102500
Month 9: payment is 101667
Month 10: payment is 100834

Overpayment = 45837

# Example user input: calculating the annuity payment

$ python3 creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=10

Your annuity payment = 21248!
Overpayment = 274880

# Example user input: calculating how long it will take to repay a loan

$ python3 creditcalc.py --type=annuity --principal=500000 --payment=23000 --interest=7.8

It will take 2 years to repay this loan!
Overpayment = 52000
