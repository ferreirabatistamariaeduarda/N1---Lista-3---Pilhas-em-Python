#Escreva um programa que use uma pilha para verificar se uma expressão aritmética é válida. 
#A expressão é válida se para cada parêntese aberto houver um parêntese fechado correspondente e, 
#para cada operação matemática, houver dois operandos.

class No:
    def _init_(self, valor):
        self.valor = valor
        self.proximo = None
        
class Pilha:
    def _init_(self):
        self._topo = None
        self.tamanho = 0
    
    def _len_(self):
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
            raise IndexError('A pilha está vazia')
        valor = self._topo.valor
        self._topo = self._topo.proximo
        self.tamanho -= 1
        return valor
    
    def topo(self):
        if self.is_empty():
            raise IndexError('A pilha está vazia')
        return self._topo.valor
    
def verificar_expressão(expressao):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operadores = Pilha()
    posfixa = []
    numeros = '0123456789'
    for caracter in expressao:
        if caracter in numeros:
            posfixa.append(caracter)
        elif caracter == '(':
            operadores.inserir(caracter)
        elif caracter == ')':
            while operadores.topo() != '(':
                posfixa.append(operadores.remover())
            operadores.remover()
        elif caracter in precedencia:
            while not operadores.is_empty()  \
                and operadores.topo() != '(' \
                and precedencia[caracter] <= precedencia[operadores.topo()]:
                posfixa.append(operadores.remover())
            operadores.inserir(caracter)
    while not operadores.is_empty():
        posfixa.append(operadores.remover())
    return ''.join(posfixa)

def calcular(expressao):
    p = Pilha()
    for caractere in expressao:
        if caractere.isdigit():
            p.inserir(caractere)
        else:
            num2 = p.remover()
            num1 = p.remover()
            if caractere == '+':
                resultado = int(num1) + int(num2)
                p.inserir(str(resultado))
            elif caractere == '-':
                resultado = int(num1) - int(num2)
                p.inserir(str(resultado))
            elif caractere == '*':
                resultado = int(num1) * int(num2)
                p.inserir(str(resultado))
            elif caractere == '/':
                resultado = int(num1) / int(num2)
                p.inserir(str(resultado))
    return p.remover()

exp = input('Digite uma expressão matemática: ')
pos = verificar_expressão(exp)
v = calcular(pos)
print(v)