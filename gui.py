import tkinter as tk
from tkinter import ttk

# Method to perform encryption
def encrypt():
	# Get input message
	input_str = txtMessage.get().lower()

	# Get Cipher key
	shift = int(txtKey.get())

	# Convert input to characters, and then integers
	str_to_char = list(input_str)
	char_to_int = [ord(i) for i in str_to_char]

	# Shift characters, handle values outside boundaries
	for i in range(len(char_to_int)):
		char_to_int[i] += shift
		if char_to_int[i] > ord('z'):
			char_to_int[i] -= 26
		elif char_to_int[i] < ord('a'):
			char_to_int[i] += 26

	# Convert shifted integers to output string
	output_str = "".join([chr(i) for i in char_to_int])

	# Set output label
	lblOutput.configure(text=output_str)


# Initialise GUI
gui = tk.Tk()
gui.title("Caesar Cipher Encryption")
gui.geometry("250x200")

# Spacer object
lblFoo = tk.Label(gui)
lblFoo.pack()

# Cipher key input
lblKey = tk.Label(gui, text = "Cipher Key: ")
lblKey.pack()
txtKey = tk.Entry(gui)
txtKey.pack()

# Input message input
lblMessage = tk.Label(gui, text = "Input Message: ")
lblMessage.pack()
txtMessage = tk.Entry(gui)
txtMessage.pack()

# Submit button
btnSubmit = tk.Button(gui, text = "Encrypt", command=encrypt)
btnSubmit.pack()

# Spacer object
lblFoo = tk.Label(gui)
lblFoo.pack()

# Encrypted output
lblOutput = tk.Label(gui, text = "")
lblOutput.pack()



gui.mainloop()