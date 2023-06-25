"""

The text below are semicolon seperated and scrambled words from >>THIS DICTIONARY<< (134 KB).
Can you unscramble them in 30 Seconds or less?

#Text: masmei;ixamme;ineram;vpamrie
#Solution: sammie;maxime;marine;vampire

"""

puzz = 'idtsninifsefetr;knamgi;otnllisieiuisb;orniigdr;mahrsc;rujnnigito;alenhst;gsniev;orbilygn;klscci'

with open('dictionary.txt','r') as infile:
	words = { x.strip() for x in infile.readlines() }

def norm(word):
	return ''.join(sorted([ x for x in word]))

scrambled = dict()
for word in words:
	scrambled[norm(word)] = word

out = ''
for entry in puzz.split(';'):
	out += scrambled[norm(entry)]
	out += ';'
print(out[0:-1])

