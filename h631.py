# 質因數
n = int(input())
while not(n%2):
    n //= 2
while not(n%3):
    n //= 3
while not(n%5):
    n //= 5
print("ugly" if n == 1 else "beautiful")