import random

while 0==0:

	try:



		rnum=random.randint (0,10)
		print ("Guess a random number between 0 and 10")
		answer=input()
		a=int (answer)

		if a==rnum:
			print("Correct!You are still worthy of the hammer!")
		else:
			print ("You're washed up son. :(")

		

	except ValueError:
		print ("Please enter a number!")