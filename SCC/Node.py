
class Node(object):
    def __init__(self, data):
        self.data = data
        self.neighbors = []
        self.discovered = False

    def __int__(self):
        return self.data
        
    def __str__(self):
        return str(self.data)

    def __gt__(self, other):
        return self.data > other

    def __lt__(self, other):
        return self.data < other
