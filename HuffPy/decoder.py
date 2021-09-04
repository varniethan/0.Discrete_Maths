#Get the input
# encodedtext = input("Enter the text to be decoded")

with open('encoded_output.txt', 'r') as f:
    encodedtext = f.read().splitlines()

# evaluating the text
code_dict = eval(encodedtext[0])
spaced_out_encoded_text = encodedtext[1].split(' ')
del spaced_out_encoded_text[len(spaced_out_encoded_text) - 1]
print("Code dict read from file:")
print(code_dict)
print("encoded text read from file as list")
print(spaced_out_encoded_text)

# applying a dictionary key lookup for each character in the string to construct the decoded text
decoded_text = ""
for c in spaced_out_encoded_text:
    decoded_text += list(code_dict.keys())[list(code_dict.values()).index(c)]

print()
print("decoded text:")
print(decoded_text)
