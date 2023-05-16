#Escreva um programa que use uma pilha para converter um número binário para octal.

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

def binarioOctal(binario):
    pilha = Pilha()

    for i in binario:
        pilha.inserir(int(i))

    octal = ""
    while len(pilha) % 3 != 0:  #zeros se necessário
        pilha.inserir(0)

    while not pilha.is_empty():
        valor = 0
        for _ in range(3):
            valor = valor * 2 + pilha.remover()
        octal += str(valor)

    return octal


binario = input('Digite um número binário: ')
resultado = binarioOctal(binario)
print('Número convertido para octal:', resultado)
#a cada digito de 3 num binários é convertido em 1 num em octal