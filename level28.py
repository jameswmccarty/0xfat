"""
Level 28
by Jonas Acres

Here is a list of roads between cities.
You need to find the FASTEST way to get from city A to city Z.
Each road is one-way. For instance, A -> B means there's a road from city A to city B, and B -> A means there's a road from city B to city A.

Solution (like this: ACDTVZ)
"""

from collections import deque

roads = dict()

def parse(line):
	global roads
	l,r = line.split(' -> ')
	if l in roads:
		roads[l].add(r)
	elif l not in roads:
		roads[l] = {r}
	if r not in roads:
		roads[r] = set()

def bfs():
	q = deque()
	pos = 'A'
	path = 'A'
	q.append((pos,path))
	while len(q) > 0:
		pos,path = q.popleft()
		if pos == 'Z':
			return path
		else:
			for entry in roads[pos]:
				q.append((entry,path+entry))

with open('level28.txt','r') as infile:
	for line in infile.readlines():
		parse(line.strip())

print(bfs())
