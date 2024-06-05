#四則運算
n = input()
d = {"A": 10, "J": 18, "S": 26, "B": 11, "K": 19, "T": 27, "C": 12, "L": 20, "U": 28, "D": 13, "M": 21, "V": 29, "E": 14,"N": 22, "W": 32, "F": 15, "O": 35, "X": 30, "G": 16, "P": 23, "Y": 31, "H": 17, "Q": 24, "Z": 33, "I": 34, "R": 25}

english = dict[n[0]]
total = english//10 + (english%10)*9+int(n[9])
for i in range(1, 9):
    total += int(n[i])*(9-i)
if total % 10:
    print('fake')
else:
    print('real')