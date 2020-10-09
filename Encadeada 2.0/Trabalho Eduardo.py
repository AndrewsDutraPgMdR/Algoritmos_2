class Produto():
    
    def __init__(self):
        self.produto = None 
        self.validade = None
        self.apontador = '-->'

    def setItem(self, produto):
        self.produto = produto
    
    def setValidade(self, validade):
        self.validade = validade

    def getItem(self):
        return self.produto
    
    def getValidade(self):
        return self.validade

    def getProduto(self):
        return (self.produto, self.validade, self.apontador)
    
class ListaEnc():

    def __init__(self):
        self.lista = [None]

    def insere(self, produto, posicao):
        if (posicao >= 1):
            if self.lista[0] == None:
                self.lista = [None] * 2
                self.lista[0] = produto
            else:
                listaAuxiliar = self.lista
                cont = 0
                for x in listaAuxiliar:
                    cont = cont + 1
                tamanho_novo = cont + 1
                if posicao > tamanho_novo:
                    print('Posição inválida')
                else:
                    self.lista = [None] * (tamanho_novo)
                    produto_adicionado = False
                    for x in range(0, tamanho_novo):
                        if (x + 1) == posicao:
                            self.lista[x] = produto
                            produto_adicionado = True
                        else:
                            if produto_adicionado == True:
                                self.lista[x] = listaAuxiliar[x - 1]
                            else:
                                self.lista[x] = listaAuxiliar[x]
        else:
            print('Posição inválida')
                  
                                
    def remove(self, posicao):
        listaAuxiliar = self.lista
        tamanho = 0
        for x in self.lista:
            tamanho = tamanho + 1
        tamanho_novo = tamanho - 1
        if posicao > tamanho_novo or posicao < 1:
            print('Posição inválida')
        elif (posicao == 1) and (tamanho == 2):
            self.lista = [None]
        else:
            self.lista = [None] * tamanho_novo
            posicao = posicao - 1
            for x in range(0, posicao):
                self.lista[x] = listaAuxiliar[x]
            for x in range(posicao, tamanho_novo):
                self.lista[x] = listaAuxiliar[x + 1]
        
           

    def imprime(self):
        return self.lista
    
    #def posicao(self):

    #def valor(self):

executar = True
lista = ListaEnc()
produto = Produto()

while executar:
    opcao = int(input('Adicionar = 1, remover = 2, imprimir = 3, sair = 4: '))

    if opcao == 1:        
        item = input('Qual o produto ?')
        vencimento = input('Qual o vencimento ?')
        produto.setItem(item)
        produto.setValidade(vencimento)
        posicao = int(input('Qual a posição deseja inserir na lista? '))
        lista.insere(produto.getProduto(), posicao)

    if opcao == 2:
        posicao = int(input('De qual posição você quer remover? '))
        lista.remove(posicao)
    
    if opcao == 3:
        print(lista.imprime())

    if opcao == 4:
        executar = False
    
    

