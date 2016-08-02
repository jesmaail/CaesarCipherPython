print("")
print("--- Caesar Cipher Encryption ---")

# Get Cipher key as integer
print("")
while True:
	try:
		shift = int(input("Please enter cipher key: "))
	except ValueError:
		print("You must enter an integer!")
		continue
	else:
		break


# Get Message as lowercase string
print("")
input_str = input("Please enter your message: ").lower()

# Convert string to list of characters
str_to_char = list(input_str)

# Convert list of characters to list of integers
char_to_int = [ord(i) for i in str_to_char]


# Shift characters, handle values outside boundaries
for i in range(len(char_to_int)):
	char_to_int[i] += shift
	if char_to_int[i] > ord('z'):
		char_to_int[i] -= 26
	elif char_to_int[i] < ord('a'):
		char_to_int[i] += 26

# Convert list of shifted integers to output string
output_str = "".join([chr(i) for i in char_to_int])

print("Encrypted message: ", output_str)
