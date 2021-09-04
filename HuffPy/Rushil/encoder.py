# huffman encoding solution by rushil a.
DIAG = True # toggles verbose output (True = enabled)

if DIAG == True:
    print("diagnostics enabled")
else:
    print("diagnostics disabled")

# plaintext = input("enter text to be encoded: ")
with open('input.txt', 'r') as f:
    plaintext = f.read()

# generate unordered frequency table as dictionary: {'char': freq, 'char': freq, ...}
unord_freq_table = {}
for c in plaintext:
    if c in unord_freq_table:
        unord_freq_table[c] += 1
    else:
        unord_freq_table[c] = 1
if DIAG == True:
    print("unordered frequency table:")
    print(unord_freq_table)
    print()
# convert dictionary to ascendantly ordered list of lists: [[freq, 'char'], [freq, 'char'], ...]
asc_freq_table = []
for i in range(len(unord_freq_table)):
    cur_min_val = min(unord_freq_table, key=unord_freq_table.get)
    temp_sublist = [unord_freq_table[cur_min_val], cur_min_val]
    asc_freq_table.append(temp_sublist)
    del unord_freq_table[cur_min_val]
if DIAG == True:
    print("ascendantly ordered frequency table:")
    print(asc_freq_table)
    print()

# binary leaf node class
class Node(object):
    freq = None
    ln = None
    rn = None
    def __init__(self, freq, ln, rn):
        self.freq = freq
        self.ln = ln
        self.rn = rn

# generate huffman tree as list of node objects
huf_tree = []
if DIAG == True:
    print("generating huffman tree:")
while len(asc_freq_table) > 1:
    huf_tree.append(Node(asc_freq_table[0][0] + asc_freq_table[1][0], asc_freq_table[0][1], asc_freq_table[1][1]))
    asc_freq_table.append([asc_freq_table[0][0] + asc_freq_table[1][0], asc_freq_table[0][1] + asc_freq_table[1][1]])
    if DIAG == True:
        print(asc_freq_table)
    del asc_freq_table[:2]
    if DIAG == True:
        print(asc_freq_table)
    asc_freq_table.sort()
    if DIAG == True:
        print(asc_freq_table)
if DIAG == True:
    print()
    print("huffman tree:")
    for node in huf_tree:
        print("node: " + node.ln + node.rn + ", frequency: " + str(node.freq))
        try:
            print("    left: " + "\'" + node.ln + "\'")
            print("    right: " + "\'" + node.rn + "\'")
        except:
            pass
    print()

# creating character code dictionary
for c in plaintext:
    if c in unord_freq_table:
        unord_freq_table[c] += 1
    else:
        unord_freq_table[c] = 1
root_node = asc_freq_table[len(asc_freq_table) - 1][1] # find root node
# traverse graph from bottom up from each character and reverse for code
code_dict = {}
for char in unord_freq_table:
    path_to_char = ""
    cur_node = char
    while not cur_node == root_node:   
        for node in huf_tree:   
            if node.ln == cur_node:
                path_to_char += "0"
                cur_node = node.ln + node.rn
            if node.rn == cur_node:
                path_to_char += "1"
                cur_node = node.ln + node.rn
    code_dict.update({char : path_to_char[::-1]})
if DIAG == True:
    print("code dictionary:")
    print(code_dict)
    print()

# encoding text and outputting
encoded_text = ""
spaced_out_encoded_text = ""
for c in plaintext:
    encoded_text += code_dict[c]
    spaced_out_encoded_text += code_dict[c] + " "

if DIAG == True:     

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
else:
    print()
    # print("encoded text:")
    # print(encoded_text)
    print("encoded text to encoded_output.txt")

# writing output to text file
with open('encoded_output.txt', 'w') as f:
    print(code_dict, file=f)
    print(spaced_out_encoded_text, file=f)