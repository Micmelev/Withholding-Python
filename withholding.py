amount = float(input('Enter distribution amount:'))
withholding = float(input('Enter witholding % amount:')) / 100
withholding_amount = round(withholding * amount , 2)
amount_received = round(amount - withholding_amount,2)
print(f'Total Distribution amount: ${"{:,}".format(amount)}')
print(f'Witholding amount: ${"{:,}".format(withholding_amount)}')
print(f'Total You Will Receive: ${"{:,}".format(amount_received)}')
