from pycipher import Vigenere
from checkWords import infer_spaces

def score(text):
    textWords = infer_spaces(text)
    # print(textWords)
    textWords = [word in words for word in textWords]
    return sum(textWords) / len(textWords)

encoded = 'EAEMO IMSRT NGFAT ASCGC EGMIC ZUMML PNKTE ZXSNS WOCOR HTKLV UZTRK USDFY XSTOA TFRTE CRFQP TKEHC HFFKD EOAUE HBHTI NEIYP OIXUJ CYZTX AACWV IIFVT NKSRB JYIWF SOPGW THUQJ EHUFS IACJM XERAG AALIN MYSOZ JEGMS GIXZF IKPWX LJESO MGMEH HHVEU ARKEI PMYNL FECXA PITHR PDDTY FISUY WSWPT NKSIX WYRTW OMAWP LUMEN WAHNE QNNVZ JYTKE HCHFF KDSAY KTHEC DMYLT OQNH'
encoded = encoded.replace(' ', '')

with open('newWords.txt') as f:
    words = f.read().split('\n')

text = ''

index = 0

lines = []

maxScore = -1
for word in words:
    word = word.upper()
    code = Vigenere(word)
    try:
        plain = code.decipher(encoded).lower()
    except Exception as e:
        print(word)
    s = score(plain)
    if s > 0.35:
        plain = ' '.join(infer_spaces(plain))
        lines.append(f"{word} {plain}")
    if s > maxScore:
        maxScore = s
    if index % 20 == 0:
        print(index // 20, '/', len(words) // 20, len(lines), f"{index / len(words):.3f}%", end='\r')
    index += 1

with open('vResults.txt', 'w') as f:
    f.write('\n'.join(lines))

print(maxScore)