# Beginner / Trivial Pursuit on steroids

> **Author:** `viipz` 
> <br/>
> **Description** Can you provide the correct answer fast enough?
>
> `nc io.ept.gg 30023`

When connecting to the server you are served different questions like solving math equations or converting base64 to ascii. There are 100 questions, the order of the questions is random each time, and you have 5 seconds to answer each question.

By connecting to `io.ept.gg 30023` multiple times we can figure out that the type of questions we get are:

- Decode morse code to ascii
- Decode base64 to ascii
- Decode hex to ascii
- Solve a math equation
- Decode decimal to ascii

We are provided with an example Python script which uses [pwntools](https://docs.pwntools.com/en/stable/) to connect to and communicate with the web server, and shows a general layout of how the script can be written. The only things missing from the script is the functions for solving and answering the given questions.

```py
#If you do not have pwntools installed, run the following command: python3 -m pip install --upgrade pwntools
from pwn import *

#Needs to be implemented
def decodeMorse(morse):
	return morse

#Connect with netcat
io = connect("io.ept.gg", 30023)

#Recieve data
data = io.recvuntil("Are you ready?").decode()
print(data)

#Send data
io.sendline("Yes")

#Recieve empty line then the line containing the question
io.recvline()
question = io.recvline().decode().strip()

#Check if it is a morse question and if so, extract the morse code
if "morse" in question:
	morse = question.split(": ")[1]

	decoded = decodeMorse(morse)
	print(decoded)
	io.sendline(decoded)

io.interactive()
```

We start with figuring out how to decoding morse as a function for this is already defined. Luckily someone has already made a function for this [here](https://www.geeksforgeeks.org/morse-code-translator-python/):

```python
# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
 
# Function to decrypt the string
# from morse to english
def decrypt(message):
 
    # extra space added at the end to access the
    # last morse code
    message += ' '
 
    decipher = ''
    citext = ''
    for letter in message:
 
        # checks for space
        if (letter != ' '):
 
            # counter to keep track of space
            i = 0
 
            # storing morse code of a single character
            citext += letter
 
        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1
 
            # if i = 2 that indicates a new word
            if i == 2 :
 
                 # adding space to separate words
                decipher += ' '
            else:
 
                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(citext)]
                citext = ''
 
    return decipher
```

This function can be inserted directly into our script. Next we find out how to convert base64 to ascii. This can be done quickly by using the [base64](https://docs.python.org/3/library/base64.html#module-base64) library:

```py
import base64

def decodeBase64(base64_message):
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    ascii_message = message_bytes.decode('ascii')

    return ascii_message
```

Decoding hex can be done using Python's built-in [bytes](https://docs.python.org/3/library/functions.html#func-bytes) class:

```py
def decodeHex(hex_message):
    ascii_message = bytes.fromhex(hex_message)
    ascii_message = ascii_message.decode('ascii')
    return ascii_message
```

The math equations can be solved using the `sympify` function from the [SymPy](https://www.sympy.org/en/index.html) library:

```py
from sympy import sympify

def solveEquation(equation):
    solved = sympify(equation)
    solved = int(solved)
    return solved

```

We have to convert the answer to an `int` to prevent `sympify` from giving us a fraction as an answer and to truncate all decimals, as this is a requirement in the question.

Lastly we have to convert decimals numbers to ascii. No external libraries are needed for this, we can just convert the decimal integer to a character directly using the [chr()](https://docs.python.org/3/library/functions.html#chr) method:

```py
decoded_num = numbers_str.split(' ')
dec_msg = ""
for num in decoded_num:
	dec_msg += chr(int(num))

return dec_msg
```

We split the individual numbers with the [split()](https://docs.python.org/3/library/stdtypes.html#bytearray.split) method with spaces as the separator with `.split(' ')`. Then we loop through the numbers with a `for`-loop and convert each number and insert them into the previously defined `dec_msg` string.

Now we have a function for solving each question. The example script has provided a way to check what the given question is asking to choose what function to use. It checks for a keyword specific for that question type, then it uses the `split()` method to extract the part after the `:` which is the part we have to decode/solve:

```py
if "morse" in question:
    morse = question.split(": ")[1]

    decoded = decodeMorse(morse)
    print(decoded)
    io.sendline(decoded)
```

This `if`-statement layout can be used for all question types. Lastly we have to create a loop to read and solve all 100 questions automatically. This can be done with a simple `for`-loop over a `range(100)`. When answering a question correctly we get one line of output confirming that the question was answered correctly, and after we get a line with the next question. For each loop we can read one line `io.recvline()`, then we know the next line is the question. This line can be read into the `question` variable. We print both the response and the question to see what the script is outputting and to print the flag at the end.

```py
...

for i in range(100):

	if "hexadecimal" in question:
        hex = question.split(": ")[1]

        decoded = decodeHex(hex)
        print(decoded)
        io.sendline(decoded)
...

	response = io.recvline()
	print(response)
	question = io.recvline().decode().strip()
	print(question)
```
If we run the script now we get the flag at the end:

```
EPT{W0w_Y0u_4r3_4_5up3r_f457_typ3r}
```
