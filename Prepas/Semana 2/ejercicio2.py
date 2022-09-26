x = "Outside of that, Hu argues that the royalties can be more reliable than the entropy of Wall Street. No matter what happens to the stock market, people are always going to be listening to music."
y = "CBD, which comes from either a marijuana or hemp plant, is non-psychoactive, so it won’t get you high like THC (tetrayhydrocannabinol). It may, however, offer anti-inflammatory, antioxidant, anti-psychotic, anti-convulsant, and antidepressant properties. Because it can hemp is legal in all 50 states, hemp-derived CBD products are becoming more readily available online and in stores all over the country."
z = "According to a report published by Fast Company, apparel sales have plummeted by 50 percent. It’s a margin that will be difficult to recover from, especially for small businesses that don’t have the backing of major conglomerates. These independent companies rely on seasonal buys from retailers to stay afloat. But with the bevy of store closures and restrictions on online sales, these behemoth retailers are facing hard times of their own."
find_x='a'
find_x2='t'
find_y='o'
find_y2='m'
find_z='i'
find_z2="n"
text_list=list(x)
counter=0
positions=[]
for x in range(len(text_list)):
    letter=text_list[x]
    if letter==find_x:
        letter=text_list[x+1]
        positions.append(x)
        if letter==find_x2:
            counter+=1
            positions.append(x+1)
        else:
            positions.remove(x)
            continue
print('in text x, the syllable "{}": \n'.format(find_x+find_x2))
print("Repetitions: {}".format(counter))
print('Positions:')
for x in range(0,len(positions),2):
    if x>=(len(positions)-2):
        print('{}-{}\n'.format(positions[x],positions[x+1]))
    else:
        print('{}-{}'.format(positions[x],positions[x+1]), end=", ")
text_list=list(y)
counter=0
positions=[]
for x in range(len(text_list)):
    letter=text_list[x]
    if letter==find_y:
        letter=text_list[x+1]
        positions.append(x)
        if letter==find_y2:
            counter+=1
            positions.append(x+1)
        else:
            positions.remove(x)
            continue
print('in text y, the syllable "{}": \n'.format(find_y+find_y2))
print("Repetitions: {}".format(counter))
print('Positions:')
for x in range(0,len(positions),2):
    if x>=(len(positions)-2):
        print('{}-{}\n'.format(positions[x],positions[x+1]))
    else:
        print('{}-{}'.format(positions[x],positions[x+1]), end=", ")
text_list=list(z)
counter=0
positions=[]
for x in range(len(text_list)):
    letter=text_list[x]
    if letter==find_z:
        letter=text_list[x+1]
        positions.append(x)
        if letter==find_z2:
            counter+=1
            positions.append(x+1)
        else:
            positions.remove(x)
            continue
print('in text z, the syllable "{}": \n'.format(find_z+find_z2))
print("Repetitions: {}".format(counter))
print('Positions:')
for x in range(0,len(positions),2):
    if x>=(len(positions)-2):
        print('{}-{}\n'.format(positions[x],positions[x+1]))
    else:
        print('{}-{}'.format(positions[x],positions[x+1]), end=", ")