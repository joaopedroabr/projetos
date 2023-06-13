print('BINARIOS\n')
print("Converter decimal para binario\n")
print(f'Jeito Fácil:')

decimal = int(input('Digite um número em decimal para transformar em binário: '))

valorEmBinario = bin(decimal)
print(f"Decimal: {decimal}")
print(f"Binario: {valorEmBinario}")

print('\nJeito maneiro')
restoBin = ""
while True:
    if decimal == 0:
        break
    restoDecimal = decimal % 2
    cociente = decimal // 2
    restoBin += str(restoDecimal)
    decimal = cociente

emBinario = restoBin[::-1]

print(f"Decimal para binario: {emBinario}")

#-------------------------------
print('\nConvertendo binario para decimal')
bin = input('Digite o número em binário: ').strip()
numBin = bin[::-1]

numDecimal = 0
for expoente in range(0, len(bin)):
    resultBase2 = (2 ** expoente) * int(numBin[expoente])
    numDecimal += int(resultBase2)

print(f'O número em binário {bin} em decimal é {numDecimal}')

# OCTAL
print("\n\nOCTAL")
print("\nConvertendo decimal para octal\n")
print("Jeito facil")
decimal = int(input('Digite um número em decimal para transformar em octal: '))

valorEmOctal = oct(decimal)
print(f"Decimal: {decimal}")
print(f"Octal: {valorEmOctal}")

print('\nJeito maneiro')
restoOct = ''
condition = True
while condition:
    if decimal == 0:
        break
    restoDecimal = decimal % 8
    cociente = decimal // 8
    restoOct += str(restoDecimal)
    decimal = cociente

emOctal = restoOct[::-1]
print(f'Jeito Maneiro - Decimal para Octal: {emOctal}')



#-------------------------------
print("\nConvertendo octal para decimal")
oct = input('Digite um número em octal: ').strip()
numOct = oct[::-1]

numDecimal = 0
for expoente in range(0, len(oct)):
    resultBase8 = (8 ** expoente) * int(numOct[expoente])
    numDecimal += resultBase8

print(f'O número binário em {oct} em decimal é {numDecimal}.')


# HEXADECIMAL
print('\n\nHEXADECIMAL')
print("\nConvertendo decimal para hexadecimal\n")
print("Jeito facil")
decimal = int(input('Digite um número em decimal para transformar em Hexadecimal: '))

valorEmHexadecimal = hex(decimal)
print(f"Decimal: {decimal}")
print(f"Hexadecimal: {valorEmHexadecimal}")

print('\nJeito maneiro')
restoHex = ''
while condition:
    if decimal == 0:
        break
    restoDecimal = decimal % 16
    cociente = decimal // 16
    if restoDecimal < 10:
        restoHex += str(restoDecimal)
    elif restoDecimal == 10:
        restoHex += 'a'
    elif restoDecimal == 11:
        restoHex += 'b'
    elif restoDecimal == 12:
        restoHex += 'c'
    elif restoDecimal == 13:
        restoHex += 'd'
    elif restoDecimal == 14:
        restoHex += 'e'
    elif restoDecimal == 15:
        restoHex += 'f'

    decimal = cociente

emHexadecimal = restoHex[::-1]
print(f'Jeito Maneiro - Decimal para Hexadecimal: {emHexadecimal}')



#-------------------------------
print("\nConvertendo hexadecimal para decimal")
hex = input('Digite um número em hexadecimal: ').strip()
listHex = []

for valores in range(0, len(hex)):
    if hex[valores].lower() == 'a':
        listHex.append('10')
    elif hex[valores].lower() == 'b':
        listHex.append('11')
    elif hex[valores].lower() == 'c':
        listHex.append('12')
    elif hex[valores].lower() == 'd':
        listHex.append('13')
    elif hex[valores].lower() == 'e':
        listHex.append('14')
    elif hex[valores].lower() == 'f':
        listHex.append('15')
    else:
        listHex.append(hex[valores])

numHex = listHex[::-1]

numDecimal = 0
for expoente in range(0, len(hex)):
    resultBase16 = (16 ** expoente) * int(numHex[expoente])

    numDecimal += resultBase16

print(f'O número em hexadecimal {hex} em decimal é {numDecimal}.')