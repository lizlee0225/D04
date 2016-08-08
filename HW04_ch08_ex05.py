# Structure this script entirely on your own.
# See Chapter 8: Strings Exercise 5 for the task.
# Please do provide function calls that test/demonstrate your
# function.


def rotate_word(s, n):
	y = 0
	new_s = ''
	while y < len(s):
		if s[y].islower():
			x = ord(s[y]) - ord('a')
			new_letter = chr((x+n) % 26 + ord('a'))
			new_s = new_s + new_letter
			y += 1
		elif s[y].isupper():
			x = ord(s[y]) - ord('A')
			new_letter = chr((x+n) % 26 + ord('A'))
			new_s = new_s + new_letter
			y += 1
	return new_s




def main():

	print(rotate_word('melon', -10))
	print(rotate_word('cheer', 7))
	print(rotate_word('PYTHON', 17))
	print(rotate_word('Hello', 30))

if __name__ == '__main__':
    main()
