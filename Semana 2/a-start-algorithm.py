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
        self.g      = 0         # Coste del camino más barato desde n al objetivo
        self.path   = []
        self.name   = name

    def __lt__(self,other):
        return self.f < other.f
    
    def asignPath(self, nodeTarget, cost):
        path = Path(cost,nodeTarget)
        self.path.append(path)



def sortNodes(nodes):
    return 

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
            # Encontrar el mejor costo
            current_cost = bestNode.g + path.cost

            # Si se encuentra el hijo en cerrados
            if path.node in openNodes == True:
                # Si el camino actual es menor a valor G del vecino
                if current_cost <  path.node.g:
                    path.node.g =  current_cost
                    path.node.f = path.node.g + path.node.h
                    openNodes.append(path.node)
                continue
            # Si se encuentra el hijo en cerrados
            if path.node in closedNodes == True:
                # Si el camino actual es menor a valor G del vecino
                if current_cost <  path.node.g:
                    path.node.g =  current_cost
                    path.node.f = path.node.g + path.node.h
                    openNodes.append(path.node)
                continue
            else:
                path.node.g = current_cost     
                path.node.f = path.node.g + path.node.h
                openNodes.append(path.node)
    return closedNodes    




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

# EXCERSISES
# https://www.youtube.com/watch?v=PzEWHH2v3TE&t=33s

print("La ruta es: ")
for path in findPath(nodeS,nodeTarget):
    print(path.name)
    
