"""
Level 26

The image you see below contains the password to this level
Rules:
Every horizontal line stands for one letter
The pixel's offset from the left in each line is equal to its number of the letter in the alphabet (eg: offset 0: A, offset 25: Z)
The password is not case sensitive
The color of each pixel is random (but never white) and has no meaning
When you reload the page a new image (and therefore new password) is generated
You have 30 seconds to solve this level
"""

from PIL import Image
im = Image.open("level26.png")
px = im.load()

for row in range(im.size[1]):
	for col in range(26):
		#print(px[col,row])
		if px[col,row] != 0:
			print(chr(col+97),end='')
print()
