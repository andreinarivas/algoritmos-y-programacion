print("This program will allow you to know how much capital you'll make from an inversion")
deposit=int(input('Please enter how much you would invest: '))
interest=int(input('Please enter the annuel interest rate: '))
time=int(input('Please enter the amount of years the investment would go on for: '))
capital=deposit*((interest+1)**time)
print(f'You would make {capital} dollars')