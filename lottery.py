import random

jackpot = 5000000
jackpot_2 = 500000
jackpot_3 = 50000
ticket_price = 5

min_winning = 0
max_winning = 1000

number_of_tickets = 365

choice_for_lottery_ticket = 666

choice_for_lottery_ticket_list = []
print("Generating lottery ticket numbers...")
i = 0
while i < 365:
	choice = random.randint(min_winning, max_winning)
	if choice in choice_for_lottery_ticket_list:
		pass
	else:
		choice_for_lottery_ticket_list.append(choice)
		i += 1


'''
Calculate based on purchasing one ticket every day for tickets_purchased.
'''
win_count = 0
print("==========\nOne ticket every day for %s days." % number_of_tickets)
tickets_purchased = 1
while tickets_purchased <= number_of_tickets:
	#print("Tickets purchased: %s" % tickets_purchased)
	winning_number = random.randint(min_winning, max_winning)
	#print("Winning: %s" % winning_number)
	if choice_for_lottery_ticket == winning_number:
		#print("Winner!")
		win_count += 1

	tickets_purchased += 1
print("Won: %s" % win_count)

'''
Calculate based on purchasing number_of_tickets once.
'''
win_count = 0
print("==========\n%s tickets at once." % number_of_tickets)
tickets_purchased = 365
while tickets_purchased <= number_of_tickets:
	#print("Tickets purchased: %s" % tickets_purchased)
	winning_number = random.randint(min_winning, max_winning)
	#print("Winning: %s" % winning_number)
	if winning_number in choice_for_lottery_ticket_list:
		win_count += 1
	tickets_purchased += 1

print("Won: %s" % win_count)