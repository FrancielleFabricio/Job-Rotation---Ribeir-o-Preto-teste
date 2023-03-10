
''' 3) Descubra a lógica e complete o próximo elemento:
a = [1, 3, 5, 7, 9]
b = [2, 4, 8, 16, 32, 64]
c = [0, 1, 4, 9, 16, 25, 36]
d = [4, 16, 36, 64]
e = [1, 1, 2, 3, 5, 8]
f = [2,10, 12, 16, 17, 18, 19]

'''
import time

RespA = int(input('Descubra a lógica e complete o próximo elemento: 1, 3, 5, 7, 9 ... '))
while RespA != 11:
    RespA = int(input('Descubra a lógica e complete o próximo elemento: 1, 3, 5, 7, 9 ... '))
print(f'o numero {RespA} completa a sequencia, por tanto a sequencia fica :1, 3, 5, 7, 9 e 11')

for i in range(1, 3):
    time.sleep(1)
    print('.')
print('olá tenho mais um teste para você')
time.sleep(1)
RespB = int(input('Descubra a lógica e complete o próximo elemento: 2, 4, 8, 16, 32, 64,... '))
while RespB != 128:
    RespB = int(input('Descubra a lógica e complete o próximo elemento: 2, 4, 8, 16, 32, 64,...'))
print(f'O numero {RespB} completa a sequencia, por tanto a sequencia fica: 2, 4, 8, 16, 32, 64, 128')

for i in range(1, 3):
    time.sleep(1)
    print('.')
print('Voltei tenho mais um teste para você')
time.sleep(1)
RespC = int(input('Descubra a lógica e complete o próximo elemento: 0, 1, 4, 9, 16, 25, 36, ... '))
while RespC != 49:
    RespC = int(input('Descubra a lógica e complete o próximo elemento: 0, 1, 4, 9, 16, 25, 36, ... '))
print(f'O numero {RespC} completa a sequencia, por tanto a sequencia fica: 0, 1, 4, 9, 16, 25, 36, 49 ')

for i in range(1, 3):
    time.sleep(1)
    print('.')
print('olá de novo, estou com mais um teste para você')
time.sleep(1)
RespD = int(input('Descubra a lógica e complete o próximo elemento: 4, 16, 36, 64, ... '))
while RespD != 100:
    RespD = int(input('Descubra a lógica e complete o próximo elemento: 4, 16, 36, 64, ... '))
print(f'O numero {RespD} completa a sequencia, por tanto a sequencia fica: 4, 16, 36, 64, 100  ')


for i in range(1, 3):
    time.sleep(1)
    print('.')
print('olá de novo, estou com mais um teste para você')
time.sleep(1)
RespE = int(input('Descubra a lógica e complete o próximo elemento: 1, 1, 2, 3, 5, 8, ... '))
while RespE != 13:
    RespE = int(input('Descubra a lógica e complete o próximo elemento: 1, 1, 2, 3, 5, 8, ... '))
print(f'O numero {RespE} completa a sequencia, por tanto a sequencia fica: 1, 1, 2, 3, 5, 8, 13  ')

for i in range(1, 3):
    time.sleep(1)
    print('.')
print('UFAA!!! essá é a ultima.')
time.sleep(1)
RespE = int(input('Descubra a lógica e complete o próximo elemento: 2, 10, 12, 16, 17, 18, 19, ... '))
while RespE != 27:
    RespE = int(input('Descubra a lógica e complete o próximo elemento: 2, 10, 12, 16, 17, 18, 19, ... '))
print(f'O numero {RespE} completa a sequencia, por tanto a sequencia fica: 2,10, 12, 16, 17, 18, 19, 27 ')

time.sleep(1)
print(...)
print('-------------------------------------------------')
print('Parábens você completou o desafo')




