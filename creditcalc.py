import math
import string
import argparse

payment_output = string.Template('Your monthly payment = $payment!')
principal_output = string.Template('Your loan principal = $add_principal!')


def type_n(pri, pay, inter):
    not_base = pay / (pay - inter * pri)
    n = math.ceil(math.log(not_base, 1 + inter))
    years = int(n / 12)
    if years == 0:
        message = "It will take "
    elif years == 1:
        message = "It will take 1 year "
    else:
        message = f"It will take {years} years "
    months = math.ceil(n % 12)
    if months == 0:
        message += "to repay this loan!"
    elif months == 1 and years != 0:
        message += f"and {months} month to repay this loan!"
    elif months == 1 and years == 0:
        message += f"{months} month to repay this loan!"
    elif months > 1 and years >= 1:
        message += f"and {months} months to repay this loan!"
    elif months > 1 and years == 0:
        message += f"{months} months to repay this loan!"
    return n, message


def type_a(pri, per, inter):
    annuity = math.ceil(pri * ((inter * math.pow(1 + inter, per)) / ((math.pow(1 + inter, per)) - 1)))
    return annuity


def calc_interest(loan_interest):
    return loan_interest / (12 * 100)


def type_p(pay, per, inter):
    p = int(pay / ((inter * math.pow(1 + inter, per)) / ((math.pow(1 + inter, per)) - 1)))
    return p


def diff_calc(parsed_list):
    principal = parsed_list[0]
    periods = parsed_list[1]
    interest = calc_interest(parsed_list[2])
    _sum = 0
    for j in range(periods):
        m = j + 1
        d = principal / periods + interest * (principal - ((principal * (m - 1)) / periods))
        print(f"Month {m}: payment is {math.ceil(d)}")
        j += 1
        _sum += math.ceil(d)
    print(f"\nOverpayment = {_sum - principal}")


def check_type(i):
    if i.isdigit():
        i = int(i)
    else:
        i = float(i)
    return i


def annuity_calc(parsed_list):
    payment = parsed_list[0]
    principal = parsed_list[1]
    periods = parsed_list[2]
    interest = calc_interest(parsed_list[3])
    if principal is None:
        principal = type_p(payment, periods, interest)
        print(principal_output.substitute(add_principal=str(principal)))
        print(f"Overpayment = {payment * periods - principal}")
    elif payment is None:
        payment = type_a(principal, periods, interest)
        print(payment_output.substitute(payment=payment))
        print(f"Overpayment = {payment * periods - principal}")
    elif periods is None:
        periods, message = type_n(principal, payment, interest)
        print(message)
        print(f"Overpayment = {payment * periods - principal}")


parser = argparse.ArgumentParser(description="This program calculates annuity payment or \
differential payments of the loan data you provide such as loan principal, interest, monthly payment.")

parser.add_argument("-i1", "--type",
                    help="You need to choose one payment method.")  # if not specified - error message
parser.add_argument("-i2", "--payment", type=int,
                    help="Enter the monthly payment amount.")  # if it was specified for diff - error message
parser.add_argument("-i3", "--principal", type=int,
                    help="Enter the loan principal.")  # is needed for both calculations, but we can calculate it,
# if we know interest, annuity payment and the number of months (periods)
parser.add_argument("-i4", "--periods", type=int,
                    help="Enter the number of periods (months) is needed to repay the loan.")
parser.add_argument("-i5", "--interest",  # can be floating-point value
                    help="Enter the loan interest. It must always be provided")

args = parser.parse_args()

if args.interest is not None:
    args.interest = check_type(args.interest)

user_input = [args.type, args.payment, args.principal, args.periods, args.interest]
if (args.type is None) or (args.interest is None) or (args.type == "diff" and args.payment is not None):
    print("Incorrect parameters.") or (len(user_input) < 4)
elif (args.payment is not None and args.payment < 0) or (args.principal is not None and args.principal < 0) \
        or (args.periods is not None and args.periods < 0) or args.interest < 0:
    print("Incorrect parameters.")
else:
    if args.type == "diff":
        user_input = [args.principal, args.periods, args.interest]
        diff_calc(user_input)
    else:
        user_input = [args.payment, args.principal, args.periods, args.interest]
        annuity_calc(user_input)
