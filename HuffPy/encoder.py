#Get the input
plaintext = input("Enter the text to be encoded")

#Generate the dictionary - {'char':'feq....}
char_frequency = {}
for char in plaintext:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
print("Character Frequency Table")
print(char_frequency)

asc_char_frequency = []
for i in range(len(char_frequency)):
    cur_min_value = min(char_frequency, key=char_frequency.get)
    temp_list = [char_frequency[cur_min_value], cur_min_value]
    asc_char_frequency.append(temp_list)
    del char_frequency[cur_min_value]

print("Asending Character Frequency Table")
print(asc_char_frequency)

#Node Objects
class Node(object):
    freq = None
    ln = None
    rn = None
    def __init__(self, freq, ln, rn):
        self.freq = freq
        self.ln = ln
        self.rn = rn


#Generate Huffman tress as list of Objects
huffman_tree = []
print("Generating a Huffman Tree")
while len(asc_char_frequency) > 1:
    huffman_tree.append(Node(asc_char_frequency[0][0] + asc_char_frequency[1][0],asc_char_frequency[0][1],asc_char_frequency[1][1]))
    asc_char_frequency.append([asc_char_frequency[0][0] + asc_char_frequency[1][0], asc_char_frequency[0][1] + asc_char_frequency[1][1]])
    print(asc_char_frequency)
    del asc_char_frequency[:2]
    print(asc_char_frequency)
    asc_char_frequency.sort()
    print(asc_char_frequency)

    print()
    print("Huff Man Tree")
    for node in huffman_tree:
        print("Node:" + node.ln + node.rn + ", Frequency:" + str(node.freq))
        try:
            print("    left: " + "\'" + node.ln + "\'")
            print("    right: " + "\'" + node.rn + "\'")
        except:
            pass
    print()

# creating character code dictionary
for char in plaintext:
    if char in char_frequency:
        char_frequency[char] += 1
    else: char_frequency[char] = 1
root_node = asc_char_frequency[len(asc_char_frequency)-1][1]

# traverse graph from bottom up from each character and reverse for code
code_dict = {}
for char in char_frequency:
    path_to_char = ""
    current_node = char
    while not current_node != char:
        for node in huffman_tree:
            if node.ln == current_node:
                path_to_char += "0"
                current_node = node.ln + node.rn
            if node.rn == current_node:
                path_to_char += "1"
                current_node = node.ln + node.rn
    code_dict.update({char : path_to_char[::-1]})

print("code dictionary:")
print(code_dict)
print()

# encoding text and outputting
encoded_text = ""
spaced_out_encoded_text = ""
for char in plaintext:
    encoded_text += code_dict[char]
    spaced_out_encoded_text += code_dict[char] + ""

print("encoded text:")
print(encoded_text)
print("encoded text (spaced out):")
print(spaced_out_encoded_text)
print()
print("length of plaintext: " + str(len(plaintext)) + " characters")
print("length of plaintext in 8-bit ascii encoding: " + str(len(plaintext) * 8) + " bits")
print("length of plaintext in huffman encoding: " + str(len(encoded_text)) + " bits")
print()
print("efficiency improvement over 8-bit ascii: " + str((len(plaintext) * 8 - len(encoded_text)) * 100/(len(plaintext) * 8)) + "%")