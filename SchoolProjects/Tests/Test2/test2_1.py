years = float(input("Enter the number of years to simulate: "))
annual_interest_rate = float(input("Enter the annual interest rate: "))
monthly_deposit = float(input("Enter the monthly amount deposited to the account: "))

# years = 5
# monthly_deposit = 250
# annual_interest_rate = 0.06

account_balance = 0.0
monthly_interest_rate = annual_interest_rate / 12.0

months = int(12*years)
for monthCounter in range(months):
    interestToBeAdded = 0.0
    interestToBeAdded = account_balance*monthly_interest_rate

    account_balance += monthly_deposit
    account_balance += interestToBeAdded

    print("{month} {interestAdded} {AccountBalance}".format(month = monthCounter, interestAdded = interestToBeAdded, AccountBalance = account_balance))