import time
import random
import os

file = open("words.txt")
words = file.readlines()

while(1):
	print("Do you want to play?\n")
	s = input()
	if s == "1" or s == "yes" or s == "Yes":
		os.system("cls")
		rand = random.randint(0, len(words) - 1)

		w = words[rand]

		guess_word: [list] = []
		for i in range(len(w) - 1):
			guess_word.append("_")
		letters: [list] = []
		for i in range(26):
			letters.append(False)

		num_guess = 7
		while(num_guess != 0):
			print(" ".join(guess_word))
			print(f"You have {num_guess} guesses left")
			print("You can peek these letters:\n")
			for i in range(26):
				if letters[i] == False:
					print(chr(i + 97), end = " ")
			print("")

			l = input()
			while(len(l) != 1 or ord(l) < ord("a") or ord(l) > ord("z") or letters[ord(l) - 97] == True):
				print("Wrong input")
				l = input() 

			os.system("cls")

			flag = False
			for i in range(len(w)):
				if w[i] == l:
					flag = True
					guess_word[i] = l

			letters[ord(l) - 97] = True

			if flag == False:
				num_guess -= 1
			else:
				flag = False
				for i in range(len(guess_word)):
					if guess_word[i] == "_":
						flag = True
				if flag == False:
					break

		os.system("cls")
		if num_guess == 0:
			print("You lost!")
		else:
			print("You won!")
		print(f"The word was - {w}\n")

		time.sleep(3)
		os.system("cls")

	else:
		break


file.close()

