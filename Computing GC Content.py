dna = ''
with open('Downloads/rosalind_gc(2).txt') as file:
    dna = file.readlines()

gc = 0
name = ''
string=None
bigname = None
for i, item in enumerate(dna):
	if item.startswith('>'):
		name = item[1:]
		string = ''
	else:
		seq = item.strip()
		string = string + seq
		string = string.strip()
		if i==len(dna)-1 or dna[i+1].startswith('>'):
			g = string.count('G')
			c = string.count('C')
			gcpercent = (g+c)/len(string) * 100
			if gcpercent > gc:
				gc = gcpercent
				bigname = name

print(bigname,gc)
