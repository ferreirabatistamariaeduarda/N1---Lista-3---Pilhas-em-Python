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

def ordemCrescente(pilha):

    pilhaTemp = Pilha() #pilha temporária
    
    while not pilhaTemp.is_empty():
        num = pilhaTemp.remover()

        while not pilhaTemp.is_empty() and pilhaTemp.topo() > num:
            pilhaTemp.inserir(pilhaTemp.remover())

        #adiciona num a pilha temporária
        pilhaTemp.inserir(num)

    #move num para a pilha principal
    while not pilhaTemp.is_empty():
        pilhaTemp.inserir(pilhaTemp.remover())

numeros = input("Digite uma sequência de números: ")
pilha = Pilha()
for i in numeros:
    pilha.inserir(int(i))
    
ordemCrescente(pilha)
cresc = ""
while not pilha.is_empty():
    cresc += str(pilha.remover())
print("Ordem Crescente: ", cresc)
