import sys

counting = {'F':2, 'L':6, 'I':3, 'M':1, 'V':4, 'S':6, 'P':4, 'T':4, 'A':4, 'Y':2, '*':3, 'H':2, 'Q':2, 'N':2, 'K':2, 'D':2,'E':2, 'C':2, 'W':1, 'R':6,'G':4}
protein = sys.argv[1]
protein = protein + '*'

total = 1
for i in protein:
	if i in counting:
		get = counting.get(i)
		total = get*total
print(total%1000000)


