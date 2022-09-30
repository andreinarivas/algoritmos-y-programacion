information={}
names=[]
last_names=[]
ages=[]
run="yes"
while run=="yes":
  given_name=input('Please enter your name: \n >>> ').capitalize()
  names.append(given_name)
  information['Names']=names
  given_last_name=input('Please enter your last name: \n >>> ').capitalize()
  last_names.append(given_last_name)
  information['Last Names']=last_names
  given_age=int(input('Please enter your age: \n >>> '))
  ages.append(given_age)
  information['Ages']=ages
  run=input("\n Would you like to add more information? \n Answer 'yes' or 'no' \n >>> ")
print(information)