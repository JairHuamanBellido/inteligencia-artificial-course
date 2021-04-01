# F(n) = G(n) + H(n)
# Author: Jair Orlando Huaman Bellido
class Path:
    def __init__(self, cost, node):
        self.cost   = cost
        self.node   = node

class Node: 
    def __init__(self, h, name):
        self.h      = h
        self.f      = 0
        self.g      = 0         
        self.path   = []
        self.name   = name

    def __lt__(self,other):
        return self.f < other.f
    
    def asignPath(self, nodeTarget, cost):
        path = Path(cost,nodeTarget)
        self.path.append(path)


def findPath(nodeOrigin,nodeTarget):
    
    # Definir los abiertos (Por defecto contendrá el primer nodo)
    openNodes = [nodeOrigin]

    # Definir los cerrados
    closedNodes = []
    
    nodeOrigin.f  = nodeOrigin.h

    # Repetir hasta abiertos es vacio o encontrado
    while len(openNodes) > 0:

        # Buscar el mejor con la F mínima (Ordenar) [1,2,3,4]
        openNodes.sort()

        # Extraer el menor Indice[0] -> MEJOR NODO
        bestNode =  openNodes.pop(0)

        # Mover el nodo a los cerrados
        closedNodes.append(bestNode)

        # Si el mejor nodo es igual a NodeTarget
        if bestNode == nodeTarget:
            break

        paths = bestNode.path

        for path in paths:

            # Costo actual
            current_cost = bestNode.g + path.cost

            # Si se encuentra el hijo en cerrados
            if path.node in openNodes:

                # Si el camino actual es menor a valor G del vecino
                if current_cost <  path.node.g:
                    path.node.g =  current_cost
                    path.node.f = path.node.g + path.node.h
                continue

            # Si se encuentra el hijo en cerrados
            if path.node in closedNodes:

                # Si el camino actual es menor a valor G del vecino
                if current_cost <  path.node.g:
                    path.node.g =  current_cost
                    path.node.f = path.node.g + path.node.h
                    closedNodes.remove(path.node)
                    openNodes.append(path.node)
                continue

            else:
                path.node.g = current_cost     
                path.node.f = path.node.g + path.node.h
                openNodes.append(path.node)
    return closedNodes    

def showResult(results):
    print("la ruta es")
    for path in results:
        print(path.name, "", sep =' | ',end=" ")
    print("\n")

def exercise1():
    # VIDEO
    # https://www.youtube.com/watch?v=PzEWHH2v3TE&t=33s
    
    nodeS = Node(5,'Nodo S')
    nodeA = Node(3,'Node A')
    nodeB = Node(4,'Node B')
    nodeC = Node(2,'Node C')
    nodeD = Node(6,'Node D')
    nodeTarget = Node(0,'Node Target')

    # Nodo Origen
    nodeS.asignPath(nodeA,1)
    nodeS.asignPath(nodeTarget,10)

    # Nodo A
    nodeA.asignPath(nodeB,2)
    nodeA.asignPath(nodeC,1)

    # Nodo B
    nodeB.asignPath(nodeD,5)

    # Nodo C
    nodeC.asignPath(nodeD,3)
    nodeC.asignPath(nodeTarget,4)

    # Nodo D
    nodeD.asignPath(nodeTarget,2)
    showResult(findPath(nodeS,nodeTarget))
  

def exercise2():
    # VIDEO
    # https://www.youtube.com/watch?v=Eiu1Cb-veCc
    nodeS = Node(7, 'Node S')
    nodeA = Node(6, 'Node A')
    nodeB = Node(2, 'Node B')
    nodeC = Node(1, 'Node C')
    nodeD = Node(0, 'Nodo D')

    # Nodo origen
    nodeS.asignPath(nodeA, 1)
    nodeS.asignPath(nodeB, 4)

    # Nodo A
    nodeA.asignPath(nodeB, 2)
    nodeA.asignPath(nodeC, 5)
    nodeA.asignPath(nodeD, 12)

    # Nodo B
    nodeB.asignPath(nodeC, 2)

    # Node C
    nodeC.asignPath(nodeD, 3)
    showResult(findPath(nodeS,nodeD))

exercise1()
exercise2()


