'''
Trabalho 2: Busca Competitiva
Grupo: Hélio Potelicki, Luis Felipe Zaguini, Pedro Henrique Roweder

'''


class Node:
    def __init__(self, shuffledMatrix, level=0, fvalue=0):
        self.shuffledMatrix = shuffledMatrix
        self.level = level
        self.fvalue = fvalue
        self.goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def getShuffledMatrix(self):
        return self.shuffledMatrix

    def getLevel(self):
        return self.level

    def getGoal(self):
        return self.goal

    # Move o '0' nas quatro direções possíveis, gerando nós filhos
    def generate_child(self):
        x, y = self.find(self.shuffledMatrix, 0)
        directions = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        children = []

        for d in directions:
            child = self.shuffle(self.shuffledMatrix, x, y, d[0], d[1])

            if child is not None:
                child_node = Node(child, self.level + 1, 0)
                children.append(child_node)
        return children

    # Move o '0' para a direção passada no argumento, se possível
    def shuffle(self, puz, x1, y1, x2, y2):
        if x2 >= 0 and x2 < len(self.shuffledMatrix) and y2 >= 0 and y2 < len(
                self.shuffledMatrix):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None

    # Cria uma cópia da matriz, a partir do nó passado
    def copy(self, root):
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    # Retorna a posição (x,y) de onde está o '0' na matriz
    def find(self, puz, x):
        for i in range(0, len(self.shuffledMatrix)):
            for j in range(0, len(self.shuffledMatrix)):
                if puz[i][j] == x:
                    return i, j