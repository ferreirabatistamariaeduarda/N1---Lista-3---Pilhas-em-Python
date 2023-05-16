#Escreva um programa que leia uma expressão matemática na forma de string e 
#utilize uma pilha para verificar se os parênteses estão balanceados.

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
    
def parenteses(expr): 
    pilha = Pilha()
    for i in expr:
        if i == '(':
            pilha.push(i)
        if i == ')':
            if pilha.is_empty():
                return False
            else:
                pilha.pop()
    return pilha.is_empty()

expr = input('Escreva uma expressão matemática: ')
if parenteses(expr):
    print('Parênteses balanceados')
else:
    print('Parênteses não balanceados')