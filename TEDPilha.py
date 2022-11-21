/* 1. Escrever uma função que receba como parâmetro uma pilha.
A função deve retornar o maior elemento da pilha. A passagem deve
ser por valor ou referência? */

import numpy as np


class pilhas:
    def __init__(self, capacidade):
        self.capacidade = capacidade

        self.topo = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def ver_topo(self):
        return self.topo

/* 2. Escreva uma função que receba como parâmetro duas pilhas e
verifique de elas são iguais. Duas pilhas são iguais se possuem os
mesmos elementos, na mesma ordem. */

def pilhas_iguais(pilha1:list,pilha2:list):
    if pilha1 == pilha2:
        return True
    else:
        return False

x = pilhas_iguais([1,2,3,4,5],[1,2,3,4,5])
z = pilhas_iguais([1,2,3,4,5],[5,4,3,2,1])
print(x)
print(z)

/* 3. Escreva uma função que preencha uma pilha passada como
parâmetro com os elementos de um vetor passado como parâmetro */

def preencher_pilha(nome_pilha:str, objetos_pilha:list):
    nome_pilha = objetos_pilha

    return nome_pilha

x = preencher_pilha("abc",[1,2,3])
print(x)

/* 4. Construa um programa utilizando uma pilha que resolva o seguinte
problema: Armazene as placas dos carros (apenas os números) que estão
estacionados numa rua sem saída estreita. Dado uma placa verifique
se o carro está estacionado na rua. Caso esteja, informe a sequência
de carros que deverá ser retirada para que o carro em questão consiga sair. */

import numpy as np


class Rua:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimo_carro = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def __rua_cheia(self):
        if self.ultimo_carro == self.capacidade - 1:
            return True

        else:
            return False

    def rua_vazia(self):
        if self.ultimo_carro == -1:
            return True

        else:
            return False

    def estacionar(self, placa):
        if self.__rua_cheia():
            print("A rua está cheia")

        else:
            self.ultimo_carro += 1
            self.valores[self.ultimo_carro] = placa

    def retirar(self):
        if self.rua_vazia():
            print("A pilha está vazia")
            return -1

        else:
            valor = self.valores[self.ultimo_carro]
            self.ultimo_carro -= 1
            return valor

    def ultimo_carro(self):
        if self.ultimo_carro != -1:
            return self.valores[self.ultimo_carro]
        else:
            return -1

    def numero_placa(self, placa):
        if self.rua_vazia():
            return False

        else:
            if placa in self.valores:
                for i in range(self.ultimo_carro + 1):
                    if placa == self.valores[i]:
                        global posicao_carro
                        posicao_carro = i
                        break

                retirar_carro = self.ultimo_carro - posicao_carro

                print(f"É preciso tirar o {retirar_carro} carro para o carro com indentificação {placa} sair!")

                return True
            else:
                return False


if __name__ == "__main__":
    c = Rua(5)
    c.estacionar(123)
    c.estacionar(321)
    c.estacionar(456)
    c.estacionar(654)
    c.estacionar(999)

    print(c.verificar_placa(654))

/* 5. Utilizando uma pilha resolver o exercício a seguir:
Dada uma sequência contendo N (N &gt;0) números reais, imprimi-la na
ordem inversa. */

def imprimir_ordem_inversa(pilha:list):
    pilha_inversa = []

    for i in pilha[::-1]:
        pilha_inversa.append(i)

    return pilha_inversa

x = imprimir_ordem_inversa([1,2,3,4,5])
print(x)

/* 6. Implemente uma função chamada TPilha, que receba um vetor de
inteiros com 15 elementos. Para cada um deles, como segue:
- se o número for par, insira-o na pilha;
- se o número lido for ímpar, retire um número da pilha;
- Ao final, esvazie a pilha imprimindo os elementos. /*

def TPilha(vetor):
    pilha = []

    if len(vetor) == 15:
        for i in range(len(vetor)):
            if vetor[i] % 2 == 0:
                pilha.append(vetor[i])
            else:
                if len(pilha) > 0:
                    pilha.pop()

        for i in range(len(pilha)):
            print(pilha[i])

        pilha.clear()


x = TPilha([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16])

/* 7. Escreva uma função chamada TPilha2 que recebe como parâmetro 2
pilhas (N e P) e um vetor de inteiros. Para cada um:
- se positivo, inserir na pilha P;
- se negativo, inserir na pilha N;
- se zero, retirar um elemento de cada pilha. */


def TPilha2(N:list,P:list,vetor:list):
    for i in range(len(vetor)):
        if vetor[i] == 0:
            if len(N) > 0:
                N.pop()
            if len(P) > 0:
                P.pop()

        elif vetor[i] > 0:
            P.append(vetor[i])

        else:
            N.append(vetor[i])

    print(N,P)

x = TPilha2([],[],[-1,1,-2,2,0])