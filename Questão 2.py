#Escreva um programa que leia uma string e use uma pilha para inverter a ordem das palavras.


class Item: 
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Pilha:
    def __init__(self):
        self.top = None
        self.size = 0
        
    def push(self, value):
        novoItem = Item(value)
        novoItem.next = self.top
        self.top = novoItem
        self.size += 1
        
    def pop(self):
        if self.size == 0:
            raise Exception('A pilha está vazia')
        valor = self.top.value
        self.top = self.top.next
        self.size -= 1
        return valor
    
    def top(self):
        if self.size == 0:
            raise Exception('A pilha está vazia')
        return self.top.value
            
    def is_empty(self):
        return self.size == 0
    
    def get_size (self):
        return self.size 
    
def inverter(palavras):
    pilha = []
    for i in palavras.split(): #cria uma lista
        pilha.append(i)
    inversao = ''
    while pilha:
        inversao += pilha.pop() + ' '
    return inversao.strip()  #remove os espaços em branco

palavras = input('Digite uma pequena frase: ')
inversao = inverter(palavras)
print(inversao)
