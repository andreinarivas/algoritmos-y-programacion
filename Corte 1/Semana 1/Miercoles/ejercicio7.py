first_deposit=int(input('Please enter the amount first deposited: '))
interest_rate=int(input("Please enter the account's interest rate: "))/100
first_year=round(first_deposit*(1+interest_rate), ndigits=2)
second_year=round(first_year*(1+interest_rate), ndigits=2)
third_year=round(second_year*(1+interest_rate), ndigits=2)
print(f"Your account at the end of the first year will have {first_year} dollars")
print(f"Your account at the end of the second year will have {second_year} dollars")
print(f"Your account at the end of the third year will have {third_year} dollars")