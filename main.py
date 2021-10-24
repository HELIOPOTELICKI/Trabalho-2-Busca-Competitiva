'''
Trabalho 2: Busca Competitiva
Grupo: Hélio Potelicki, Luis Felipe Zaguini, Pedro Henrique Roweder

'''

from node import Node
from puzzle import Puzzle


def main(puz, node):
    # Obtem a matriz objetivo
    goal = node.getGoal()

    node.setFValue(puz.calculate_f(node, goal))
    puz.appendNodeOpen(node)

    print('\n\nJogo embaralhado:')
    printMatrix(start)
    print('\nJogo objetivo:')
    printMatrix(node.getGoal())
    print('\nCaminho percorrido:')

    while True:
        cur = puz.getOpenFirst()
        print('')

        printMatrix(cur.getShuffledMatrix())

        if (puz.calculate_h(cur.getShuffledMatrix(), goal) == 0):
            break

        for i in cur.generate_child():
            i.setFValue(puz.calculate_f(i, goal))
            puz.appendNodeOpen(i)

        puz.appendNodeClosed(cur)
        puz.deletFirstNode()
        puz.getOpenList().sort(key=lambda x: x.getFValue(), reverse=False)


# Apresenta a matriz no terminal
def printMatrix(matrix):
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print("")


if __name__ == '__main__':
    # Matriz embaralhada
    start = [[2, 3, 6], [1, 4, 0], [7, 5, 8]]

    # Instancia as classes
    puz = Puzzle()
    node = Node(start)
    main(puz, node)
    print('\nFIM')