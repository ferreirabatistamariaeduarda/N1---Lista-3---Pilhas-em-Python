#Escreva um programa que use uma pilha para converter um número decimal para hexadecimal.

#Escreva um programa que use uma pilha para converter um número decimal para octal

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Pilha:
    def __init__(self):
        self._topo = None
        self.tamanho = 0
   
    def __len__(self):
        return self.tamanho
   
    def is_empty(self):
        return self.tamanho == 0
   
    def inserir(self, valor):
        no = No(valor)
        no.proximo = self._topo
        self._topo = no
        self.tamanho += 1
   
    def remover(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        valor = self._topo.valor
        self._topo = self._topo.proximo
        self.tamanho -= 1
        return valor
   
    def topo(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        return self._topo.valor

def hexaDecimal(hexadecimal):
    pilha = Pilha()

    for i in hexadecimal:
        if i.isdigit():
            pilha.inserir(int(i))
        else:
            valor = ord(i.upper()) - ord('A') + 10
            pilha.inserir(valor)

    decimal = 0
    expoente = 0
    while not pilha.is_empty():
        decimal += pilha.remover() * (16 ** expoente)
        expoente += 1

    return decimal


hexadecimal = input('Digite um número hexadecimal: ')
resultado = hexaDecimal(hexadecimal)
print('Número convertido para decimal:', resultado)