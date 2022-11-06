from participants import Participants, Sing, Dance, Music, Free
def validate_option():
  option=input('Please enter the category of the participant: \n 1. Singing \n 2. Dance \n 3. Music \n 4. Free \n >>> ')
  while not option in ['1','2','3','4']:
    option=input('INVALID INPUT\n. Please enter a valid option \n 1. Singing \n 2. Dance \n 3. Music \n 4. Free \n >>> ')
  return int(option)

def validate_name():
  student_name=input('Please enter your name: \n >>> ')
  student=student_name.split()
  check_student=''
  for x in student:
    check_student+=x
  while not check_student.isalpha():
       student_name=input('INVALID INPUT \n Please enter your name: \n >>> ')
       check_student=''
       student=student_name.split()
       for x in student:
          check_student+=x
  return student_name

def validate_number(required):
  student_id=input('Please enter your {}: \n >>> '.format(required))
  while not student_id.isnumeric():
    student_id=input('INVALID INPUT \n Please enter your {}: \n >>> '.format(required))
  return int(student_id)

def add_instruments():
  instruments=[]
  add='Y'
  while add=='Y':
    new=input('Please enter the instrument you will play: \n >>> ')
    instruments.append(new)
    add=input('Do you want to add more instruments? \n Yes (Y) or No (N) \n >>>')
  return instruments

def create_participant(participants):
  option=validate_option()
  name=validate_name()
  kind=input('Please enter if the participant is a solo or group: \n >>> ')
  phone_number=validate_number('phone number')
  number=validate_number('contest number')
  if option==1:
    song_name=input('Please enter the songs name: \n >>> ')
    song_author=input('Please enter the song author: \n >>> ')
    participants['Singing'].append(Sing(name, kind, phone_number, number, song_name, song_author))
  if option==2:
    style=input('Please enter your dance style: \n >>> ')
    participants['Dance'].append(Dance(name, kind, phone_number, number, style))
  if option==3:
    instruments=add_instruments()
    participants['Music'].append(Music(name, kind, phone_number, number, instruments))
  if option==4:
    talent=input('Please describe what talent you will be displaying: \n >>> ')
    participants['Free'].append(Free(name, kind, phone_number, number, talent))

  

def main():
  participants= {
    'Singing': [],
    'Dance': [],
    'Music': [],
    'Free':[]
  }
  total_participants=0
  run=True
  while run:
    total_participants+=1
    create_participant(participants)
    run=input('Do you want to add another participant? \n Yes (Y) or No (N) \n >>> ')
    if run=='N':
      run=False
  for category, participants in participants.items():
    print('\n--------- {} CATEGORY ----------\n'.format(category))
    print('TOTAL PARTCIPANTS IN CATEGORY: {}'.format(len(participants)))
    for participant in participants:
      participant.print_info()
      print('\n')
  print('TOTAL PARTICIPANTS: {}'.format(total_participants))

  

main()