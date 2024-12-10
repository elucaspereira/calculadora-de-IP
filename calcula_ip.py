import math


print('-'*50)
print('calculadora de ip')

def calcula_mascara(ip_valido):
    ip_total = ip_valido + 2
    
    bits = math.ceil(math.log2(ip_total))
    
    mascara = 32 - bits
    
    return mascara

ip_necessario = input('Digite a quantidade de ip necessario: ')
ip_valido = int(ip_necessario)
mascara = calcula_mascara(ip_valido)
print(f'A máscara de sub-rede será: /{mascara}')

