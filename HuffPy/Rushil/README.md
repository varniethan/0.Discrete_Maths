# huffpy
**A Huffman encoder built in python**

This Huffman encoder was built using only python’s core modules. It does not use heaps/stacks such as those present in the `heapq` library and is therefore very inefficient in comparison. It also comes with a decoder that interfaces with a text file output by the encoder.

## Instructions
To run the encoder script:
- Paste the input into a textfile in the same directory as the script named `input.txt`.
- Run the script as a regular python script - opening a terminal in the directory of installation and entering `python encoder.py`.
This will show the methodology of conversion into the console and write the output letter dictionary and encoded binary string to a textfile called `encoded_output.txt`.

To run the decoder script:
- Run the script as a regular python script - opening a terminal in the directory of installation and entering `python decoder.py`.
This will take the encoded information in the encoded_output textfile and decode it, outputting the plaintext to the console.

## Verbose output
Both scripts have a `DIAG` variable that, when set to true, will give verbose diagnostic output.
Verbose output is enabled by default - if you wish to disable it, change the variable on line 2 of each script from
`DIAG = True`
to
`DIAG = False`

## Methodology
This script is an implementation of the Huffman encoding technique.
It works by:
- Taking input from a file

- Counting the number of occurences of each unique character in the input text
- Ordering them ascendantly

- Constructing a binary tree by:
  - Pairing the first two elements of the ascendantly ordered list into leaves of a node
  - Adding this new node into the list
  - Ordering the list again
  - Running the above steps continuously until the list reaches length 1 (the root).

- Encoding text by iterating through each character present, and for each one:
  - Searching the tree for that charater's node (linearly - O(n))
  - Finding the parent node to that character node (also linearly - O(n))
  - Labelling the traversal up one layer as either left or right
  - Traversing upwards in this fashion until the root is reached
  - Producing a string for the definition of each character

- Using the dictionary and the text, encoding it with the new binary tree derived definitions for each character.
  - There are spaces between each character to split them - this is an issue with variable length encoding compared to fixed length as splits between character bit signals are not constant.

- Outputting the encoded text and dictionary, and displaying (if diagnostics are enabled) the theoretical efficiency improvement over 8-bit ASCII text encoding.

In theory, the most frequently present characters will have the shortest bit definitions.

## TODO
- Implement a more efficient tree traversal/search algorithm. (DFS? BFS?)
- Change the current 'diagnostics' implementation:
  - Disable diagnostic output by default
  - Using the `argparse` module, use a flag on run to enable/disable diagnostics
- Re-implement the encoder using heaps/stacks and calculate big O, and delta between both implementations
