from Node import Node
from Table import Table
from AStartAlgorithm import AStartAlgorithm


## Instancia del tablero
table = Table(10,10)


## Instancia del algoritmo A* Estrella
AStart = AStartAlgorithm(table)

## Inicialización del origen
origin = Node(9,9,'D')

# Inicialización del destino
destination =  Node(5,3,'X')

origin.visited = True

table.SetPosition(origin)
table.SetPosition(destination)

block1 = Node(2,    3,  '|')
block2 = Node(2,    4,  '|')
block3 = Node(3,    4,  '|')
block4 = Node(4,    4,  '|')
block5 = Node(5,    4,  '|')
block6 = Node(6,    4,  '|')
block7 = Node(7,    3,  '|')
block8 = Node(6,    2,  '|')

table.SetPosition(block1)
table.SetPosition(block2)
table.SetPosition(block3)
table.SetPosition(block4)
table.SetPosition(block5)
table.SetPosition(block6)
table.SetPosition(block7)
table.SetPosition(block8)

AStart.findPath(origin,destination)

for x in table.board:
    row = []
    for y in x:
        row.append(y.type)
    print(row)


# '0' -> Caminos
# '|' -> Obstáculos
# 'X' -> Nodos de origen y destinos
# '=' -> Camino escogido para el destino