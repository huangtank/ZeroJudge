d = {'HELLO':'ENGLISH',
     'HOLA':'SPANISH',
     'HALLO':'GERMAN',
     'BONJOUR':'FRENCH',
     'CIAO':'ITALIAN',
     'ZDRAVSTVUJTE':'RUSSIAN'}
i = 1
while True:
    n = input()
    if n == '#':
        break
    if n not in d:
        print(f'Case {i}: UNKNOWN')
    else:
        print(f'Case {i}: {d[n]}')
    i += 1
