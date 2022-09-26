marriage=[]
house=[]
vehicle=[]
children=[]
count_names=0
count_house=0
count_vehicle=0
count_children=0
name=input('Please enter your name: ')
full_list=[]
print("Let's begin by checking your choices")
print('Who could you marry?')
while count_names<4:
    name_insert=input('Enter a name:\n>>')
    marriage.append(name_insert)
    count_names+=1
print('Where could you live?')
while count_house<4:
    name_insert=input('Enter an option:\n>>')
    house.append(name_insert)
    count_house+=1
print('What could you drive?')
while count_vehicle<4:
    name_insert=input('Enter an option:\n>>')
    vehicle.append(name_insert)
    count_vehicle+=1
print('How many children could you have?')
while count_children<4:
    name_insert=input('Enter a name:\n>>')
    children.append(name_insert)
    count_children+=1
counter=int(input('Please choose a number: '))
index_to_delete=0
full_list= marriage + house + vehicle + children
length=len(full_list)
print('Now lets discover your life\n')

while len(marriage)!=1 or len(house)!=1 or len(vehicle)!=1 or len(children)!=1:
    index_to_delete+=counter
    length-=1
    if index_to_delete>length:
        index_to_delete=0
    to_delete=full_list[index_to_delete]
    if marriage in full_list or house in full_list or vehicle in full_list or children in full_list:
        if len(marriage)==1:
            full_list.remove(marriage[0])
        if to_delete in marriage:
            marriage.remove(to_delete)
            full_list.remove(to_delete)
        if len(house)==1:
            full_list.remove(house[0])
        if to_delete in house:
            house.remove(to_delete)
            full_list.remove(to_delete)
        if len(vehicle)==1:
            full_list.remove(vehicle[0])
        if to_delete in vehicle:
            vehicle.remove(to_delete)
            full_list.remove(to_delete)
        if len(children)==1:
            full_list.remove(children[0])
        if to_delete in children:
            children.remove(to_delete)
            full_list.remove(to_delete)

print(marriage,house,vehicle,children)
print("\nCONGRATS! {}, your future is:\n You're gonna marry {}\n You'll live in {}\n You'll drive a {}\n You'll have {} children".format(name,marriage[0],house[0],vehicle[0],children[0]))