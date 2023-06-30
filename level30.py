"""
Level 30
by Joel I

Below is an image with green tiles of varying color, each with a character label.

The password to this level is a string of characters which orders their tiles from lightest to darkest.
"""

from PIL import Image
im = Image.open("lvl30_train.png")
im = im.convert('RGB')
px = im.load()

im2 = Image.open("level30.png")
im2 = im2.convert('RGB')
px2 = im2.load()

train_order = '>241RHGFNV9KE:6JD3BUPC5XTIL78<'

alpha_dict = dict()

for j in range(5):
	for i in range(6):
		base_x = i*40
		base_y = j*40
		letter_set = set()
		for y in range(40):
			for x in range(40):
				if px[base_x+x,base_y+y] == (255,255,255):
					letter_set.add((x,y))
		alpha_dict[train_order[j*6+i]] = letter_set

def find_match(base_x,base_y,px_data):
	this_set = set()
	this_level = 0
	for y in range(40):
		for x in range(40):
			if px_data[base_x+x,base_y+y] == (255,255,255):
				this_set.add((x,y))
			else:
				this_level = px_data[base_x+x,base_y+y][1]
	for k,v in alpha_dict.items():
		if v == this_set:
			return((this_level,k))
	return (None,None)

letters = []

for j in range(5):
	for i in range(6):
		base_x = i*40
		base_y = j*40
		letters.append(find_match(base_x,base_y,px2))
print(''.join( x[1] for x in sorted(letters,reverse=True)))
