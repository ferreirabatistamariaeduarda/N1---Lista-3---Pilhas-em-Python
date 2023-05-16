#Escreva um programa que leia uma string contendo apenas números e 
#use uma pilha para verificar se a string é um número de palíndromo.


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
    
def palindromo(string):
    pilha = Pilha()
    tamanho = len(string)
    
    if string != '0123456789':
        print('digite apenas números')
        return False
    if tamanho == 0:
        return False
    for i in range(0, tamanho // 2):
        if string[i] != string[tamanho - i - 1]: 
            return False   
    return pilha.is_empty

string = input('Digite algo: ')

if palindromo(string):
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
         
    
   
    
    
