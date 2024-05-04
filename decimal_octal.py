
from collections import deque

class Decimal_octal_binario:
    def deciOcta(self, x):
        valortrabalho = x
        Pilha_resto = deque()
        while valortrabalho != 0:
            Pilha_resto.append(valortrabalho % 8)
            valortrabalho = (valortrabalho // 8)
        numero_stri = ""
        for n in reversed(Pilha_resto):
            numero_stri = numero_stri + str(n)
        print(numero_stri)
        return numero_stri
    def deciObina(self, x):
        valortrabalho = x
        Pilha_resto = deque()
        while valortrabalho != 0:
            Pilha_resto.append(valortrabalho % 2)
            valortrabalho = (valortrabalho // 2)
        numero_stri = ""
        for n in reversed(Pilha_resto):
            numero_stri = numero_stri + str(n)
        print(numero_stri)
        return numero_stri
entrada = int(input("Digite o número que deseja converter: "))

donda = Decimal_octal_binario()
donda.deciOcta(entrada)

donda.deciObina(entrada)