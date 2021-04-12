class Node: 
    def __init__(self,x,y,type = "0"):
        self.h          = 0
        self.f          = 0
        self.g          = 0         
        self.parent     = None
        self.x          = x
        self.y          = y
        self.type       = type
        self.visited    = False
        self.direction  = ""

    def __lt__(self,other):
        return self.f < other.f