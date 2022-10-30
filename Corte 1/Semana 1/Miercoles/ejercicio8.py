num_bread=int(input('Please enter the number of breads not sold: '))
bread_price=float(input('Please enter the normal price of a bread loaf: '))
discount=float(input('Please enter discount percentage for non-fresh bread: '))/100
discount_cost=bread_price*(1-discount)
normal_cost=num_bread*bread_price
total_cost=round(num_bread*discount_cost,ndigits=2)
print(f"The total normal cost for the fresh bread would be {normal_cost}")
print(f"The total cost for the unsold bread will be {total_cost}")