def print_menu():
  print('\nWELCOME TO THE SYSTEM \n Please choose an option\n')
  option=input('1. Aspiring student \n2. Administration \n 3. Quit \n >>> ')
  while not option.isnumeric() or not option in ['1','2','3']:
    option=input('INVALID INPUT \n \n Please enter a valid option\n1. See inventory \n2. Purchase \n 3. Quit\n >>> ')
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


def define_trimester(student_average):
  if student_average<12:
    print('NOT ADMITTED')
    trimester='NOT ADMITTED'
  if student_average>=12 and student_average<18:
    trimester=1
  if student_average>=18 and student_average<=20:
    trimester=2
  return trimester

def print_report(new_student):
  print('\n ------ REGISTRATION SUMMARY ------')
  for info,data in new_student.items():
    print('{}: {}'.format(info.upper(),data))

def main():
  students={}
  student_number=0
  option=print_menu()
  if option==1:
    student_number+=1
    new_student={}
    new_student['student name']=validate_name()
    new_student['student id']=validate_number(required='ID')
    student_average=validate_number(required='average')
    new_student['student average']=student_average
    new_student['trimester']=define_trimester(student_average)
    students[student_number]=new_student
    print_report(new_student)
    


  
  pass


main()