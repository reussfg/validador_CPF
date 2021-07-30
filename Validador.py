CPF = input ('Insira seu CPF sem pontos e sem traços: ')
if len(CPF) < 11:
    print('Você digitou CPF errado')
list1 = []
list2 =[]
CPF_list = []
soma1 =[]
soma2 = []
for n in range (0, 11, +1):
    CPF_list.append((int(CPF[n])))
for v1 in range (10,1,-1):
    list1.append((v1))
for v2 in range (11, 1, -1):
    list2.append((v2))
for i in range (0, 9, +1):
    a = int(CPF_list[i])
    b = int(list1[i])
    soma1.append(a*b)
total1 = sum(soma1)
valido1 = 11 -(total1 % 11)
if valido1 > 9:
    primeiro_digito = 0
    if CPF_list[9] != primeiro_digito:
        print('CPF inválido')
        quit()
for i in range (0, 10, +1):
    a = int(CPF_list[i])
    b = int(list2[i])
    soma2.append(a*b)
total2 = sum(soma2)
valido2 = 11 - (total2 %11)
if valido2 > 9:
    segundo_digito = 0
    if CPF_list[10] != segundo_digito:
        print('CPF inválido')
        quit()
print('CPF Válido')





