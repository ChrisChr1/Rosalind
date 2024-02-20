dna= ''
with open('Downloads/rosalind_hamm(1).txt') as f:
    dna = f.read().split()

word = dna[0]
word2 = dna[1]

count = 0
for item in range(len(word)):
	if word[item] != word2[item]:
		count +=1
	
print(count)
