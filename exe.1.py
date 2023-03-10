'''
1) Observe o trecho de código abaixo:

int INDICE = 13, SOMA = 0, K = 0;
enquanto K < INDICE faça
{
K = K + 1;
SOMA = SOMA + K;
}
imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?
'''

indice, soma, k = 13, 0, 0

while k < indice:
    k = k + 1
    soma = soma + k
print(f'A variavel soma ao final do processo terá o valor: {soma}')














