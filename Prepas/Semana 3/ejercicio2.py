safe=False
pass_list=[]
number_in=0
mayus_in=0
lower_in=0
non_numeric_in=0
while safe==False:
  password=input('Please enter a password: \n >>> ')
  for x in password:
    if x.isdigit():
        number_in+=1
    if x.isupper():
        mayus_in+=1
    if x.islower():
        lower_in+=1
    if not x.isalnum():
      non_numeric+=1
  if len(password)<8:
    print('Your password is not safe. \n It must have at least 8 characters.')
    continue
  if number_in<1:
    print('Your password is not safe. \n It must have at least 1 number.')
    continue
  if mayus_in<1:
    print('Your password is not safe. \n It must have at least 1 upper case letter.')
    continue
  if lower_in<1:
    print('Your password is not safe. \n It must have at least 1 lower case letter.')
    continue
  if non_numeric_in<1:
    print('Your password is not safe. \n It must have at least 1 non numeric character.')
    continue
  else:
    safe=True
print('Your password is safe')
pass_list.append(password)
print(pass_list)


  