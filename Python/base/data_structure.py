class List(list):
    super.__init__()

    
class Node(object):
    def __init__(self, item=-1, lchild=None, rchild=None):
        self.item = item
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    def __init__(self):
        self.root = Node()
        self.Queue = list()

    def add(self, item):
        node = Node(item)
        if self.root.item == -1:
            self.root = node
            self.Queue.append(self.root)
        else:
            treeNode = self.Queue[0]
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.Queue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.Queue.append(treeNode.rchild)
                self.Queue.pop(0)
