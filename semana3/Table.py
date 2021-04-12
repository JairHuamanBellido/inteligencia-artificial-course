from Node import Node
class Table:
    def __init__(self, width, height):
        self.width  = width
        self.height = height
        self.board = []
        self.build()

    def build(self):
        for x in range(self.height):
            row = []
            for y in range(self.width):
                row.append(Node(y,x))
            self.board.append(row)

    def SetPosition(self,node):
        self.board[node.y][node.x] = node