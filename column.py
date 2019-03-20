from itertools import permutations

from pycipher import ColTrans

encoded = "RSEBA DEUTL ITCUD VSEOS ETRNY AFTYR FETTU TRYAI ICYOB IORHO WUSDI PENYC"
encoded = encoded.replace(' ', '')
chars = 'ABCDEFGHIJKL'
print(len(encoded), encoded)
start = None
for keyword in permutations(chars):
    if keyword[:3] != start:
        start = keyword[:3]
        print(''.join(start))
    decoded = ColTrans(''.join(keyword)).decipher(encoded)
    if 'PLACE' in decoded:
        print(decoded)
