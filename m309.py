#運算
for _ in range(int(input())):
  h, m, s = map(int, input().split())
  s = h*32*16+m*16+s
  s *= 4
  h, s = s//3600, s%3600
  m, s = s//60, s%60
  print(f"{h}:{m}:{s}")