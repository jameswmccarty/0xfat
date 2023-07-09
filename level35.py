"""
Level 35
by Oscar Arnflo

Count the circles.
Shapes can never intersect and are never broken by image's edges

You have 30 seconds.
"""

from PIL import Image
im = Image.open("circle_test.png")
px = im.load()

width,height = im.size
shapes = dict()
all_points = { (x,y) for y in range(height) for x in range(width) }

def flood_walk(pt):
	x,y = pt
	pt_color = px[x,y]
	shape_set = set(((x,y),))
	q = [(x,y)]
	while len(q) > 0:
		x,y = q.pop(0)
		for dx,dy in ((0,1),(0,-1),(1,0),(-1,0)):
			nx,ny = x+dx,y+dy
			if nx >=0 and ny >= 0 and nx < width and ny < height and px[nx,ny] == pt_color and (nx,ny) not in shape_set:
				shape_set.add((nx,ny))
				q.append((nx,ny))
	return shape_set

circles = 0
while len(all_points) > 0:
	new_shape = flood_walk(all_points.pop())
	all_points.difference_update(new_shape)
	min_x = min( pt[0] for pt in new_shape )
	max_x = max( pt[0] for pt in new_shape )
	min_y = min( pt[1] for pt in new_shape )
	max_y = max( pt[1] for pt in new_shape )
	if (min_x,min_y) not in new_shape: # not a square
		circles += 1
print(circles)
