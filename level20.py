import hashlib

with open('wordlist.txt','r') as infile:
	words = { x.strip() for x in infile.readlines() }

for a in words:
	for b in words:
		m = hashlib.md5()
		s = a+b
		m.update(s.encode("utf-8"))
		if m.hexdigest() == '0362a4277a021bd383af3d61bf915d7e':
			print(a+b)
