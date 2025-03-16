# M. Overman, 3/6/2025
# lab 9, question 1

import random

class coin():
	def __init__(self):
		self.amount = 20
		self.sideup = "Heads"
	def toss(self):
		if random.randint(0, 1) == 0:
			self.sideup = "Heads"
		else:
			self.sideup = "Tails"
	def get_amount(self):
		return self.amount
	def get_sideup(self):
		return self.sideup
	def set_amount(self, inc):
		self.amount += inc

def main():
	p1 = coin()
	p2 = coin() 
	cont_play = input("Do you want to play? (Y = yes) ")
	while cont_play == "Y" or cont_play == "y":
		p1.toss()
		p2.toss()
		if p1.get_sideup() == p2.get_sideup():
			p1.set_amount(1)
			p2.set_amount(-1)
		else:
			p2.set_amount(1)
			p1.set_amount(-1)
		
		print(f"Player 1 landed on {p1.get_sideup()} and Player 2 landed on {p2.get_sideup()}.")
		print(f"Player 1 now has {p1.get_amount()} coins, and Player 2 now has {p2.get_amount()} coins.")

		cont_play = input("Do you want to continue? (Y = yes) ")
	
	print(f"Player 1 final score: {p1.get_amount()}\nPlayer 2 final score: {p2.get_amount()}")

if __name__ == '__main__':
    main()