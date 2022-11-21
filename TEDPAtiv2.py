/* 1. Construa uma Pilha utilizando a linguagem Python. Dada uma sequência contendo N (N>0) 
números inteiros, imprimi-la na ordem inversa. */

import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.valores = np.empty(self.capacidade, dtype= int)

    def __pilha_cheia(self):
        if self.topo == self.capacidade -1:
            return True

        else:
            return False

    def pilha_vazia(self):
        if self.topo == -1:
            return True

        else:
            return False

    def empilhar(self, valor):
        if self.__pilha_cheia():
            print("A pilha está cheia")

        else:
            self.topo += 1
            self.valores[self.topo] = valor

    def desempilhar(self):
        if self.pilha_vazia():
            print("A pilha está vazia")
            return -1

        else:
            valor = self.valores[self.topo]
            self.topo -=1
            return valor

    def ver_topo(self):
        if self.topo != -1:
            return self.valores[self.topo]
        else:
            return -1

    def imprimir_inverso(self):
        pilha_inversa = []
        for i in self.valores[::-1]:
            pilha_inversa.append(i)

        return pilha_inversa

if __name__ == "__main__":
    pilha = Pilha(10)
    pilha.empilhar(1)
    pilha.empilhar(2)
    pilha.empilhar(3)
    pilha.empilhar(4)
    pilha.empilhar(5)
    pilha.empilhar(6)
    pilha.empilhar(7)
    pilha.empilhar(8)
    pilha.empilhar(9)
    pilha.empilhar(10)

    print(pilha.imprimir_inverso())

/* 2. Desenvolva um programa em Python utilizando uma Pilha de acordo com a situação
problema: Armazene as placas dos carros de luxos (apenas os números) que estão
estacionados em um rua sem saída. Dado uma placa verifique se o carro está estacionado
na rua. Caso esteja, informe a sequência de carros que deverá ser retirada para que o
carro em questão consiga sair. */

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
            print('A rua está cheia')

        else:
            self.ultimo_carro += 1
            self.valores[self.ultimo_carro] = placa

    def retirar(self):
        if self.rua_vazia():
            print('A pilha está vazia')
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

                print(f'É preciso tirar o {retirar_carro} carro para o carro com indentificação {placa} sair!')

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

/* 3. Construa um programa em Python de acordo com situação problema descrita: Um grupo
de soldados está cercado e não há esperança de vitória, porém existe somente um cavalo
disponível para escapar e buscar por reforços. Para determinar qual soldado deve escapar
para encontrar ajuda, eles formam um círculo (Fila Circular) e sorteiam um número de um
chapéu. Começando por um soldado sorteado aleatoriamente, uma contagem é realizada
até o número sorteado. Quando a contagem terminar, o soldado em que a contagem
parou é removido do círculo, um novo número é sorteado e a contagem recomeça no
soldado seguinte ao que foi eliminado. A cada rodada, portanto, o círculo diminui em um,
até que somente um soldado reste e seja escolhido para a tarefa. */

import numpy as np

class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade=capacidade
        self.inicio=0
        self.final=-1
        self.numero_elemento=0
        self.valores=np.empty(self.capacidade, dtype=int)

    def __fila_vazia(self):
        return self.numero_elemento==0

    def __fila_cheia(self):
        return self.numero_elemento==self.capacidade

    def enfileirar(self, valor):
        if self.__fila_cheia():
            print('A fila está cheia!!!')
            return
        if self.final==self.capacidade -1:
            self.final=-1
        self.final+=1
        self.valores[self.final]=valor
        self.numero_elemento+=1

    def desenfileirar(self):
        if self.__fila_vazia():
            print('A fila está vazia!!!')
            return

        temp=self.valores[self.inicio]
        self.inicio+=1
        if self.inicio==self.capacidade-1:
            self.inicio=0
        
        self.numero_elemento-=1
        return temp

    def primeiro(self):
        if self.__fila_vazia():
            return -1
        else:
            return self.valores[self.inicio]

    fila = FilaCircular(5)
    fila.primeiro()
    fila.enfileirar(2)
    fila.primeiro()
    fila.enfileirar(10)
    fila.enfileirar(9)
    fila.enfileirar(5)

/* 4. Construa uma Fila de Prioridade utilizando a linguagem Python em que sejam
implementadas as funções para inserção de um novo elemento (inteiro) na fila e a
remoção do elemento de mais alta prioridade */ 

import numpy as np

class FilaPrioridade:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_elementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)
        self.prioridades = np.empty(self.capacidade, dtype=int)

    def __fila_vazia(self):
        if self.numero_elementos == 0:
            return True
        else:
            return False

    def __fila_cheia(self):
        if self.numero_elementos == self.capacidade:
            return True
        else:
            return False

    def enfileirar(self, valor, prioridade):
        if self.__fila_cheia():
            print('A fila está cheia!')
            return

        if self.final == self.capacidade - 1:
            self.final = -1
  
        self.final += 1
        self.prioridades[self.final] = prioridade
        self.valores[self.final] = valor
        self.numero_elementos += 1

    def desenfileirar(self):
        if self.__fila_vazia():
            print('A fila está vazia!')
            return

        temp = self.valores[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade -1:
            self.inicio = 0
        else:
            self.numero_elementos -= 1
            return temp

    def primeiro(self):
        if self.__fila_vazia():
            return -1
        else:
            return self.valores[self.inicio]

    def mostrar_fila(self):
        for i in range(self.numero_elementos):
            print(f"{i+1}º -> {self.valores[i]}")

if __name__ == "__main__":
    p = FilaPrioridade(10)
    p.enfileirar(1,0)
    p.enfileirar(2,0)
    p.enfileirar(3,1)
    p.enfileirar(4,0)
    p.enfileirar(5,0)
    p.enfileirar(6,0)
    p.enfileirar(7,0)
    p.enfileirar(8,0)
    p.enfileirar(9,0)
    p.enfileirar(10,0)

    p.mostrar_fila()

/* 5. Escreva um programa em Python que simule o controle de uma pista de decolagem de
aviões em um aeroporto. Neste programa, o usuário deve ser capaz de realizar as
seguintes tarefas:
a. Listar o número de aviões aguardando na fila de decolagem;
b. Autorizar a decolagem do primeiro avião da fila;
c. Adicionar um avião à fila de espera;
d. Listar todos os aviões na fila de espera;
e. Listar as características do primeiro avião da fila. */

import numpy as np

class Aeroporto:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numero_avioes = 0
        self.avioes = np.empty(self.capacidade, dtype=int)
        self.identificacao_letra = np.chararray(self.capacidade, unicode=True)
        self.identificacao_numero = np.chararray(self.capacidade, unicode=True)

    def __pista_vazia(self):
        if self.numero_avioes == 0:
            return True
        else:
            return False

    def __pista_cheia(self):
        if self.numero_avioes == self.capacidade:
            return True
        else:
            return False

    def lista_espera(self, aviao, identificacao_letra:str, identificacao_num:str):
        if self.__pista_cheia():
            print('Todos aviões estão na pista')
            return

        if self.final == self.capacidade - 1:
            self.final = -1

        self.final += 1
        self.avioes[self.final] = aviao
        self.identificacao_letra[self.final] = identificacao_letra
        self.identificacao_numero[self.final] = identificacao_numero
        self.numero_avioes += 1

    def autorizacao_decolagem(self):
        if self.__pista_vazia():
            print('Todos os aviões decolaram')
            return

        temp = self.avioes[self.inicio]
        self.inicio += 1
        if self.inicio == self.capacidade -1:
            self.inicio = 0
        else:
            self.numero_avioes -= 1
            return temp

    def carc_primeiro_aviao(self):
        if self.__pista_vazia():
            print('Sem aviões na fila')
        else:
            primeiro_aviao = self.avioes[self.inicio]
            letra_primeiro_aviao = self.identificacao_letra[self.inicio]
            numero_primeiro_aviao = self.identificacao_numero[self.inicio]

            print(f'Próximo avião a decolar:'{primeiro_aviao}
IDT LETRA: {letra_primeiro_aviao}
IDT NUM: {numero_primeiro_aviao})

    def numero_avioes(self):
        if self.__pista_vazia():
            print('Sem aviões na fila para decolar')
        else:
            print(f'A quantidade de aviões na fila para decolar é de: ' {self.numero_avioes}!!)

    def listar_avioes(self):
        for i in range(len(self.avioes)):
            print(f'A fila de espera: Avião '{self.avioes[i]}\

if __name__ == '__main__':
    a = Aeroporto(10)
    a.lista_espera(1,"A","1")
    a.lista_espera(2,"B","2")
    a.lista_espera(3,"C","3")
    a.lista_espera(4,"D","4")
    a.lista_espera(5,"E","5")
    a.lista_espera(6,"F","6")
    a.lista_espera(7,"G","7")
    a.lista_espera(8,"H","8")
    a.lista_espera(9,"I","9")
    a.lista_espera(10,"J","10")

    a.numero_avioes()
    a.carac_primeiro_aviao()
    a.listar_avioes()
    a.autorizacao_decolagem()
    a.numero_avioes()

/* 6. Construa uma Lista Sequencial utilizando a linguagem Python com as seguintes operações:
a. Verificar se um número pertence lista;
b. Inserir um novo elemento na lista;
c. Remover um elemento da lista;
d. Imprimir os valores da lista; */

import numpy as np

class ListaSequencial:
    def __init__(self, capacidade):
        self.capacidade = capacidade 
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprimir(self):
        if self.ultima_posicao == -1:
            print('A lista está vazia!!')
        else:
            for i  in range(self.ultima_posicao +1):
                print(f"{i} -> {self.valores[i]}")

    def insere(self, valor):
        if self.ultima_posicao == self.capacidade -1:
            print('Capacidade máxima atingida!')
        else:
            self.ultima_posicao +=1
            self.valores[self.ultima_posicao] = valor

    def pesquisa_posicao(self,valor):
        for i  in range(self.ultima_posicao +1):
            if valor == self.valores[i]:
                return i
            
        return -1

    def excluir(self, valor):
        posicao = self.pesquisa_pos(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]      
            self.ultima_posicao -= 1

    def pesquisa_numero(self,valor):
        for i  in range(self.ultima_posicao +1):
            if valor == self.valores[i]:
                return print(f'O número {valor} pertence a lista')
            
        return (f'O número {valor} não pertence a lista')
            
    
if __name__ == "__main__":

    lista = ListaSequencial(3)
    lista.insere(3)
    lista.insere(8)
    lista.insere(7)
    lista.imprimir()
    print(lista.pesquisa_numero(3))
    lista.excluir(3)
    lista.imprimir()
    print(lista.pesquisa_numero(3))
