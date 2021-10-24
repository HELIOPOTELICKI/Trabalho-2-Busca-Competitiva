'''
Trabalho 2: Busca Competitiva
Grupo: Hélio Potelicki, Luis Felipe Zaguini, Pedro Henrique Roweder

'''


class Puzzle:
    def __init__(self):
        self.open = []
        self.closed = []

    # Calcula a heurística - f(n) = g(n) + h(n)
    def calculate_f(self, node, goal):
        start = node.getShuffledMatrix()
        return self.calculate_h(start, goal) + node.getLevel()

    def calculate_h(self, start, goal):
        count = 0

        for i in range(0, 3):
            for j in range(0, 3):
                if start[i][j] != goal[i][j] and start[i][j] != 0:
                    count += 1
        return count