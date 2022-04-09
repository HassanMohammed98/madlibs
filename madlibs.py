def main():
	# write your code here
	print("Mad libs where libs get mad.\nStart below:\n")
	# test = True
	while True:
		time = int(input("Enter a number from 1 to 12: "))
		# if time > 0 and time < 13
		if time in range(1,13) : 
			# test = False
			break
		else:
			print("Enter a valid number between 1 and 12") 
	items = input("Enter a noun (plural): ")
	name = input("Enter a name: ")
	scream = input("Enter any sentence: ")
	action = input("Enter a verb: ")

	print('''
	The story goes\n\n
It was {} o'clock when I heard a knock at the door.
I opened the door and there was a box full of {} with a note saying "From Mr. {}."
Just as I closed the door I heard a scream "{}."
I froze in place and all I could do was {}.
	'''.format(time, items, name.title(), scream.upper(),action))



if __name__ == '__main__':
	main()