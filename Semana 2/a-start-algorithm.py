# F(n) = G(n) + H(n)

class Path:
    def __init__(self, cost, node):
        self.g      = cost
        self.node   = node

class Node: 
    def __init__(self, h, name):
        self.h      = h
        self.f      = 0
        self.g      = 0         # Coste del camino más barato desde n al objetivo
        self.path   = []
        self.name   = name

    def __lt__(self,other):
        return self.h < other.h
    
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
            print("Se ha encontrado")
            break

        paths = bestNode.path

        for path in paths:

            if path.node in openNodes == True:
                if path.g <  
                continue
            if path.node in closedNodes == True:
                continue
            else:
                openNodes.append(path.node)     
                path.node.f = path.g + path.node.h




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


# findPath(nodeS,nodeTarget)
