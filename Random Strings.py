#Probability that 90000 random DNA strings with 0.6 GC content of string length

DNA = 'CCCAGGCC'

at = 0
gc = 0
for i in DNA:
    if i == 'A' or i =='T':
        at += 1
    else:
        gc += 1


ATprob = ((1 - 0.489951) / 2)**at
#print(ATprob)
GCprob = ((0.489951) / 2)**gc
#print(GCprob)

print('%0.3f' % (1 - (1 - ATprob * GCprob)**81327))
