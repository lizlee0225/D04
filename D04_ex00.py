#!/usr/bin/env python
# D04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
import random

def random_game():
	x = random.randint(0,25)
	n = ''
	count = 0
	while count < 5:
		try: 
			n = int(input('Choose a number between 1-25: '))
			print(n)
		except:
			print('Needs to be an integer')
			count += 1
			continue
		if n == x:
			print ('You got the number!')
			break
		elif n > x:
			print('Your number is too high.')
			count += 1
			continue
		elif n < x:
			print('Your number is too low.')
			count += 1
			continue


################################################################################
def main():

    random_game()

if __name__ == '__main__':
    main()