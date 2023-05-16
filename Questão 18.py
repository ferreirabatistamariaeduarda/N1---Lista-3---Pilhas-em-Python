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

def infixa_para_posfixa(expressao):
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
            while not operadores.is_empty() and operadores.topo() != '(' and precedencia[caracter] <= precedencia[operadores.topo()]:
                posfixa.append(operadores.remover())
            operadores.inserir(caracter)
    while not operadores.is_empty():
        posfixa.append(operadores.remover())
    return ''.join(posfixa)

def calcular(expressao):
    pilha = Pilha()
    for i in expressao:
        if i.isdigit():
            pilha.inserir(int(i))
        elif i == '+':
            op2 = pilha.remover()
            op1 = pilha.remover()
            pilha.inserir(op1 + op2)
        elif i == '-':
            op2 = pilha.remover()
            op1 = pilha.remover()
            pilha.inserir(op1 - op2)
        elif i == '*':
            op2 = pilha.remover()
            op1 = pilha.remover()
            pilha.inserir(op1 * op2)
        elif i == '/':
            op2 = pilha.remover()
            op1 = pilha.remover()
            pilha.inserir(op1 / op2)
    return pilha.topo()

expressao = input('Digite uma expressão matemática: ')
posfixa = infixa_para_posfixa(expressao)
resultado = calcular(posfixa)

print('Expressão na notação polonesa reversa:', posfixa)
print('Resultado:', resultado)
