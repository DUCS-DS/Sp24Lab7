from codetree_solution import PrefixCodeTree

tree = PrefixCodeTree()
tree.add_code(' ','011')
tree.add_code('a','00')
tree.add_code('b','1001')
tree.add_code('c','1000')
tree.add_code('d','1010')
tree.add_code('e','11000')
tree.add_code('g','11001')
tree.add_code('h','11010')
tree.add_code('i','1011')
tree.add_code('m','11011')
tree.add_code('o','11100')
tree.add_code('r','010')
tree.add_code('s','11101')
tree.add_code('t','11110')
tree.add_code('w','11111')

coded_msg = "11110110101100001111011001100110111000011111111110001010100111011111010111111000101000"

print("the bitstring has length:", len(coded_msg))
print("the decoded message is:", tree.decode(coded_msg))
