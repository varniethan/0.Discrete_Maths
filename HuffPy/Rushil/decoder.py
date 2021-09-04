# huffman decoding solution by rushil a.
DIAG = True # toggles verbose output (True = enabled)

if DIAG == True:
    print("diagnostics enabled")
else:
    print("diagnostics disabled")

# reading output from text file
with open('encoded_output.txt', 'r') as f:
    content = f.read().splitlines()

# evaluating the text
code_dict = eval(content[0])
spaced_out_encoded_text = content[1].split(' ')
del spaced_out_encoded_text[len(spaced_out_encoded_text) - 1]
if DIAG == True:
    print("code dict read from file:")
    print(code_dict)
    print("encoded text read from file as list:")
    print(spaced_out_encoded_text)

# applying a dictionary key lookup for each character in the string to construct the decoded text
decoded_text = ""
for c in spaced_out_encoded_text:
    decoded_text += list(code_dict.keys())[list(code_dict.values()).index(c)]

print()
print("decoded text:")
print(decoded_text)
