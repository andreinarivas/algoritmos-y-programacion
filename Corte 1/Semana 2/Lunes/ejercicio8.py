score=float(input('Please enter your score: '))
unacceptable=0.0
intermediate=0.4
outstanding=0.6
money_earned=2400*score
if score==unacceptable:
    print("Your score is {} which is unacceptable. \nYou'll earn ${}".format(score,money_earned))
elif score==intermediate:
    print("Your score is {} which is intermediate. \nYou'll earn ${}".format(score,money_earned))
elif score>=outstanding:
    print("Your score is {} which is outstanding. \nYou'll earn ${}".format(score,money_earned))
else:
    print("ERROR. input invalid")