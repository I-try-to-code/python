import pandas
data= pandas.read_csv("nato_phonetic_alphabet.csv")
letters= data.Letter.tolist()
code= data.code.tolist()
dicto={letters[i]:code[i] for i in range(len(code))}


word= input("enter the word you want codes for: ").upper()
to_decode=[i for i in word]
for i in to_decode:
    print(dicto.get(i))