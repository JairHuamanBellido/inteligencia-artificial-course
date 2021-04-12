from Constants import DIAGONAL,LINEAL

class AStartAlgorithm:
    
    def __init__(self,table):
        self.table = table.board
        self.tableWidth  = table.width
        self.tableHeight = table.height

    def ManhattanDistance(self,origin,target):
        
        targetX = target.x
        targetY = target.y

        originX = origin.x
        originY = origin.y
        
        result = abs(targetX-originX) + abs(targetY-originY)

        return result * 10
        
    def getNeighbors(self,node):

        neighbors = []

        if node.x - 1 >= 0:
            if self.table[node.y][node.x - 1].type != '|' :
                self.table[node.y][node.x - 1].direction = "Lineal"
                neighbors.append(self.table[node.y][node.x - 1])

        if node.x + 1 < self.tableWidth :
            if  self.table[node.y][node.x + 1].type != '|':
                self.table[node.y][node.x+1].direction = "Lineal"
                neighbors.append(self.table[node.y][node.x+1])

        if node.y - 1 >= 0 :
            if  self.table[node.y - 1][node.x].type != '|':
                self.table[node.y - 1][node.x].direction = "Lineal"
                neighbors.append(self.table[node.y - 1][node.x])

        if node.y + 1 < self.tableHeight:
            if  self.table[node.y + 1][node.x].type != '|':
                self.table[node.y + 1][node.x].direction = "Lineal"
                neighbors.append(self.table[node.y + 1][node.x])

        if node.x - 1 >= 0 and node.y - 1 >= 0:
            if (self.table[node.y - 1][node.x - 1].type != '|' and 
                (self.table[node.y -1][node.x].type != '|' or  self.table[node.y][node.x - 1].type != '|')):    
                self.table[node.y - 1][node.x - 1].direction = "Diagonal"
                neighbors.append(self.table[node.y - 1][node.x - 1])

        if node.x - 1 >= 0 and node.y + 1 < self.tableHeight:
            if (self.table[node.y + 1][node.x - 1].type != '|' and
                (self.table[node.y][node.x - 1].type != '|' or self.table[node.y + 1][node.x].type != '|')):        
                self.table[node.y + 1][node.x - 1].direction = "Diagonal"
                neighbors.append(self.table[node.y + 1][node.x - 1])

        if node.x + 1 < self.tableWidth and node.y - 1 >= 0:
            if (self.table[node.y - 1][node.x + 1].type != '|' and
                (self.table[node.y - 1][node.x].type !='|' or self.table[node.y][node.x+1].type != '|') ):        
                self.table[node.y - 1][node.x + 1].direction = "Diagonal"
                neighbors.append(self.table[node.y - 1][node.x + 1])

        if node.x + 1 < self.tableWidth and node.y + 1 < self.tableHeight:
            if ( self.table[node.y + 1][node.x + 1].type != '|' and
                (self.table[node.y + 1][node.x].type != '|' or self.table[node.y][node.x + 1].type != '|')):
                self.table[node.y + 1][node.x + 1].direction = "Diagonal"
                neighbors.append(self.table[node.y + 1][node.x + 1])

        return neighbors

    def findPath(self,nodeOrigin,nodeTarget):
        
        # Definir los abiertos (Por defecto contendrá el primer nodo)
        openNodes = [nodeOrigin]

        # Definir los cerrados
        closedNodes = []

        # Repetir hasta abiertos es vacio o encontrado
        while  len(openNodes) > 0:


            # Buscar el mejor con la F mínima (Ordenar) [1,2,3,4]
            openNodes.sort()

            
            # Extraer el menor Indice[0] -> MEJOR NODO
            bestNode =  openNodes.pop(0)


            # Mover el nodo a los cerrados
            closedNodes.append(bestNode)

            # Si el mejor nodo es igual a NodeTarget
            if bestNode == nodeTarget:
                break

            neighbors = self.getNeighbors(bestNode)
            for neighbor in neighbors:

                cost = 0
                if neighbor.direction == 'Diagonal':
                    cost =  DIAGONAL
                else:
                    cost = LINEAL
                # Costo actual
                current_cost = bestNode.g + cost

                # Actualizar distancia Manhattan
                neighbor.h =  self.ManhattanDistance(neighbor,nodeTarget)

                # Si se encuentra el hijo en cerrados
                if neighbor in openNodes:
                    # Si el camino actual es menor a valor G del vecino
                    if current_cost <  neighbor.g:
                        neighbor.g =  current_cost
                        neighbor.f = neighbor.g + neighbor.h
                        neighbor.parent = bestNode
                    continue

                # Si se encuentra el hijo en cerrados
                if neighbor in closedNodes:

                    # Si el camino actual es menor a valor G del vecino
                    if current_cost <  neighbor.g:
                        neighbor.g =  current_cost
                        neighbor.f = neighbor.g +  neighbor.h
                        neighbor.parent = bestNode

                        closedNodes.remove(neighbor)
                        openNodes.append(neighbor)
                    continue

                else:
                    neighbor.g  = current_cost
                    neighbor.f = neighbor.g +  neighbor.h
                    neighbor.parent = bestNode
                    openNodes.append(neighbor)
        result = []
        endNode = nodeTarget

        while True:
            result.append(endNode)
            if endNode.parent == None:
                break
            endNode = endNode.parent
        
        result.reverse()
        for x in result:
            if self.table[x.y][x.x].type == '0':
                self.table[x.y][x.x].type = '='
        return result    
