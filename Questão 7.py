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

def converter_dec_bin(n):
    p = Pilha()
    q = n
    while n > 0:
        r = n % 8
        n = n // 8
        p.inserir(r)
       
    return p
       
n = int(input("NUMERO: "))

r = converter_dec_bin(n)

while not r.is_empty():
    print(r.remover())