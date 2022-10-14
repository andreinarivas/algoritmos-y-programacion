import random


def generate_tickets(number_of_tickets):
  tickets=[]
  while len(tickets)<number_of_tickets:
    ticket_number=''
    while len(ticket_number)<8:
      digit=str(random.randint(0, 9))
      ticket_number+=digit
    tickets.append(ticket_number)

  return tickets



def main():
  tickets_available=generate_tickets(int(input('Please enter how many tickets you want: ')))
  print(tickets_available)
  print('The winning ticket is {}'.format(random.choice(tickets_available)))


main()