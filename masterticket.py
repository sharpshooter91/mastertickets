

SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining  = 100

def calculate_price (x):
    return int(x) * TICKET_PRICE + SERVICE_CHARGE


while tickets_remaining > 0:
    try:
        print('There are', tickets_remaining, 'tickets left.')
        name = input('What is your name?  ')
        number_of_tickets = input('Hello {}, how many tickets do you want?   '.format(name))
        price = calculate_price(number_of_tickets)
        print('Total price for you is {} dolars'.format(price))
        should_proceed = input('Do you want to proceed with a purchase Y/N?     ')

        if should_proceed.lower() == 'y' and int(tickets_remaining) >= int(number_of_tickets):
            tickets_remaining = int(tickets_remaining) - int(number_of_tickets)
            print('SOLD!')
        elif int(tickets_remaining) < int(number_of_tickets):
            print('There is only {} tickets remaining'.format(tickets_remaining))
        else:
            print('Thank you, if you change your mind please come back. Have a nice day!')

    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

else:
        print('There are not enuf tickets left.')
