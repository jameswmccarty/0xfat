"""
The following password has been encrypted by the telephone alphabet pattern. The solution for this level is the digit sum of the number code

Example:
A => 22
B => 222
C => 2222
1 => 1
2 => 2
5 => 5
I => 4444
W => 99
Z => 99999

"HEY" => 444 333 9999 => 4+4+4+3+3+3+9+9+9+9 = 57

"""

puzz = '371356a76f7a8292632055877126fba5'

def digit_sum(letter):
	alpha = { 'abc' : 2,
			  'def' : 3,
			  'ghi' : 4,
			  'jkl' : 5,
			  'mno' : 6,
			  'pqrs' : 7,
			  'tuv' : 8,
			  'wxyz' : 9 }
	if letter in '0123456789':
		return int(letter)
	else:
		for k,v in alpha.items():
			if letter.lower() in k:
				return (k.index(letter.lower())+2)*v

print(sum([digit_sum(x) for x in puzz]))
