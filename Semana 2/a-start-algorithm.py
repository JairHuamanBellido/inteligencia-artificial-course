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
        self.parent = None

    def __lt__(self,other):
        return self.f < other.f
    
    def asignPath(self, nodeTarget, cost):
        path = Path(cost,nodeTarget)
        pathReverse = Path(cost,self)
        
        self.path.append(path)
        nodeTarget.path.append(pathReverse)


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
                path.node.parent = bestNode
                openNodes.append(path.node)
    
    result = []
    endNode = nodeTarget

    while True:
        result.append(endNode)
        if endNode.parent == None:
            break
        endNode = endNode.parent
    
    result.reverse()
    return result    

def showResult(results):
    print("la ruta es")
    for path in results:
        print(path.name, "", sep =' | ',end=" ")
    print("\n")

def exercise3():
    Arad            = Node(366,'Arad')
    Bucharest       = Node(0,'Bucharest')
    Craiova         = Node(160,'Craiova')
    Dobreta         = Node(242,'Dobreta')
    Eforie          = Node(161,'Eforie')
    Fagaras         = Node(178, 'Fagaras')
    Giurgiu         = Node(77, 'Giurgiu')
    Hirsova         = Node(151, 'Hirsova')
    Iasi            = Node(226, 'Iasi')
    Lugoj           = Node(244,'Lugoj')
    Mehadia         = Node(241,'Mehadia')
    Neamt           = Node(234, 'Neamt')
    Oradea          = Node(380, 'Oradea')
    Pitesti         = Node(98, 'Pitesti')
    RimnicuVilcrea  = Node(193, 'Rimnicu Vilcea')
    Sibiu           = Node(253, 'Sibiu')
    Timisoara       = Node(329, 'Timisoara')
    Urziceni        = Node(80, 'Urziceni')
    Vaslui          = Node(199, 'Vaslui')
    Zerind          = Node(374, 'Zerind')

    Arad.asignPath(Zerind,75)
    Arad.asignPath(Sibiu,140)
    Arad.asignPath(Timisoara,118)
    
    Zerind.asignPath(Oradea,71)

    Oradea.asignPath(Sibiu,151)

    Timisoara.asignPath(Lugoj,111)

    Lugoj.asignPath(Mehadia,70)

    Mehadia.asignPath(Dobreta,75)

    Dobreta.asignPath(Craiova,120)

    Craiova.asignPath(RimnicuVilcrea,146)
    Craiova.asignPath(Pitesti,138)

    RimnicuVilcrea.asignPath(Pitesti,97)
    
    Sibiu.asignPath(Fagaras,99)
    Sibiu.asignPath(RimnicuVilcrea,80)

    Fagaras.asignPath(Bucharest, 211)

    Pitesti.asignPath(Bucharest,101)

    Bucharest.asignPath(Giurgiu,90)
    Bucharest.asignPath(Urziceni, 85)

    Urziceni.asignPath(Hirsova, 98)
    Urziceni.asignPath(Vaslui, 142)

    Hirsova.asignPath(Eforie, 86)

    Vaslui.asignPath(Iasi, 92)

    Iasi.asignPath(Neamt,87)

    showResult(findPath(Timisoara,Bucharest))


exercise3()


