"""
Level 32
by Joel I

Below is a nonsense paragraph of latin words from >>this dictionary<<(8.6 KB)

A few letters from random words in the paragraph are spelled with one letter shifted one place forward. Eg A -> B, B -> C, Z -> A

The password to this level is a string created by the letters which would fix the typos

You have 10 seconds to solve this level

"""

with open('latindictionary.txt','r') as infile:
	words = { word.strip() for word in infile }

# return off-by-one letter match
def typo_match(a):
	if a in words:
		return ''
	alpha = 'abcdefghijklmnopqrstuvwxyz'
	for b in { x for x in words if len(x) == len(a) }:
		diff = ''
		all_offset_match = True
		for idx,char in enumerate(b):
			if a[idx] != char:
				diff += char
				if alpha[(alpha.index(char)+1)%len(alpha)] != a[idx]:
					all_offset_match = False
		if all_offset_match and len(diff) > 0:
			return diff
	return ''

puzzle = input("Copy/Paste puzzle text: ")
puzzle = puzzle.lower().replace('.','')
print(''.join(typo_match(x) for x in puzzle.split(' ')))
