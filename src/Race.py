from Node import Node

def get_positions_from_nodes(nodos):
    lista = []
    for nodo in nodos:
        lista.append(nodo.getPosition())
    return lista


class RaceP:

    # Argumento "file_path" é o caminho para o ficheiro que contém o circuito.
    def __init__(self, file_path):
        self.g = {}
        self.matrix = {}
        self.pos_inicial = None # tuplo da posição onde o jogador se encontra
        self.goals = []
        self.linhas = 0
        self.colunas = 0

        fp = open(file_path, "r")

        l = 0
        c = 0

        for line in fp:
            buf = []
            c = 0
            for ch in line:
                if ch != "\n":
                    if ch == "P":
                        self.pos_inicial = (l, c)
                    if ch == "F":
                        self.goals.append((l,c))
                    buf.append(ch)
                    c += 1
            self.matrix[l] = buf
            l += 1

        if self.pos_inicial is None:
            print("Não foi definida uma posição inicial!")
            return
        self.linhas = len(self.matrix)
        self.colunas = len(self.matrix[0])


    def expande(self, estado: Node):
        """
        Esta função calcula os próximos estados possíveis dado um estado atual.
        """
        accs = [(0,0), (1,0), (1,1), (0,1), (0,-1), (-1,0), (-1,-1), (1,-1), (-1,1)] # acelerações possíveis
        estados = []

        for ac in accs:
            new = estado.clone()
            new.sumVelocity(ac)
            new.sumPosition(new.velocity)
            if new != estado and (0 <= new.position[0] < self.linhas) and (0 <= new.position[1] < self.colunas):
                estados.append(new)

        return estados

    def addAresta(self, from_node: Node, to_node: Node, custo: int):
        if from_node not in self.g:
            self.g[from_node] = [(custo,to_node)]
        else:
            self.g[from_node].append((custo,to_node))

    def cria_grafo(self):
        estados = [Node(self.pos_inicial, (0, 0))]
        visitados = set()

        while estados:
            estado = estados.pop()
            visitados.add(estado)
            expansao = self.expande(estado)
            for e in expansao:
                if e not in visitados:
                    if self.possiblePath(estado.position,e.position): # verifica se é possível avancar, ou seja, não tem paredes pelo meio
                        self.addAresta(estado,Node(estado.position,(0,0)),25)
                    else:
                        self.addAresta(estado,e,1)
                    estados.append(e)


    def get_matrix(self):
        return self.matrix

    def get_start(self):
        return self.pos_inicial

    def get_goals(self):
        return self.goals

    # Printa uma matriz com "H" nas posicoes indicadas.
    def print_matrix(self, posicoes, file="result.txt"):
        new_matrix = self.matrix
        for p in posicoes:
            l = p[0]
            c = p[1]
            if self.colunas > l and self.linhas > c:
                new_matrix[l][c] = "H"

        fp = open(file, "w")
        for line_n in new_matrix:
            linha = "".join(new_matrix[line_n])
            fp.write(linha + "\n")
        fp.close()

    def obstaculo(self, coords: tuple) -> bool:
        """
        Indica se uma certa posição da matriz é um obstaculo ou não.
        """
        return self.matrix[coords[0]][coords[1]] == 'X'
    
    def possiblePath(self, pos_i: tuple, pos_f: tuple) :
        """
        Esta funcção verifica se é possível ir de uma posição para outra no mapa.
        Fonte: https://www.geeksforgeeks.org/check-possible-path-2d-matrix/
        """
        arr = []
        for i in range(len(self.matrix)):
            arr.append(self.matrix[i].copy())

        # directions
        Dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # queue, insert the initial position
        q = [pos_i]

        # until queue is empty
        while len(q) > 0 :
            p = q.pop(0)
            
            # mark as visited
            arr[p[0]][p[1]] = 'X'
            
            # destination is reached.
            if p == (pos_f[0],pos_f[1]) :
                return True
                
            # check all four directions
            for i in range(4) :
                # using the direction array
                a = p[0] + Dir[i][0]
                b = p[1] + Dir[i][1]
                
                # not blocked and valid
                if pos_i[0] <= a <= pos_f[0] and pos_i[1] <= b <= pos_f[1] and arr[a][b] != 'X':
                    q.append((a, b))
        return False


# Testing
rp = RaceP("race.txt")
rp.cria_grafo()


'''
matrix = rp.get_matrix()
n = Node((3,1), (0,2))  # posicao, velocidade
lista_nodos = rp.expande(n)
lista_posicoes = get_positions_from_nodes(lista_nodos)
print (lista_posicoes)
rp.print_matrix(lista_posicoes)
'''

t = 0