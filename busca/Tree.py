import Fila
import Pilha

class No:
    def __init__(self, valor):
        self.info = valor
        self.filhos=[]

    def insere(self, valor1, valor2):
         if valor2 == self.info:
             self.filhos.append(No(valor1))
         else:
             for i in self.filhos:
                 i.insere(valor1,valor2)

    def show(self):
        pass

    def show1(self):
        f = Fila.FilaD()
        f.inserir(self)
        while f.estahVazia() != True:
            self = f.getPrim()
            print(self.info, end=' ')
            f.remover()
            for i in self.filhos: 
                f.inserir(i)

    def show2(self):
        p = Pilha.PilhaD()
        p.push(self)
        while p.estahVazia() != True:
            self = p.getTopo()
            print(self.info, end=' ')
            p.pop()
            for i in self.filhos[::-1]:
                p.push(i)

    def show3(self):
        p = Pilha.PilhaD()
        p.push(self)
        while p.estahVazia() != True:
            self = p.getTopo()
            print(self.info, end=' ')
            p.pop()
            for i in self.filhos:
                p.push(i)

class TreeIA:

    def __init__(self):
        self.raiz = None

    def insere(self, valor1,valor2):
        if self.raiz == None:
            self.raiz = No(valor1)
        else:
            self.raiz.insere(valor1,valor2)

    def show1(self):
        cont=0
        f = Fila.Fila()
        f.inserir(self)
        num= int(input("Digite um valor:"))
        
        while f.estahVazia() != True:
            self = f.getPrim()
            cont+=1               
            if(num == self.info):
                print("Nó:", cont)
                break
            print(self.info, end=" ")
            f.remover()
            for i in self.filhos: 
                f.inserir(i)

    def show2(self):
        if self.raiz!=None:
            self.raiz.show2()

    def show3(self):
        p = Pilha.Pilha()
        p.push(self)
        cont=0
        num= int(input("Digite um valor2:"))
        while p.estahVazia() != True:
            self = p.getTopo()
            cont+=1
            if(num == self.info):
                print("Nó:", cont)
                break
            print(self.info, end=" ")
            p.pop()
            for i in self.filhos:
                p.push(i)

    def show(self):
        if self.raiz!=None:
            self.raiz.show()
