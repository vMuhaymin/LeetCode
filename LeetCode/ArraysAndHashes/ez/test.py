class heap:

    nodes = []

    def __init__(self, list):
        for node in list:
            self.add(node)
    
    def getParentIndex(self, index):
        return (index-1)//2
    
    def getLchildIndex(self, index):
        return (2* index +1)

    def getRchildIndex(self, index):
        return (2* index +2)

    def getRchild(self, index):
        return self.nodes[(2* index +2)]

    def swap(self, firstI , sencondI):
        heapLen = len(self.nodes) 
        if firstI >= heapLen or sencondI >= heapLen:
            print("Error: Out of Index !!")
        self.nodes[firstI] , self.nodes[sencondI] =  self.nodes[sencondI], self.nodes[firstI]
        
    def heapify(self, child = None):

        if not child :
            child = len(self.nodes) - 1
        if child == 0:
            return self.nodes
        parent = self.getParentIndex(child)
        if self.nodes[parent] and self.nodes[parent] > self.nodes[child] :
            self.swap(parent, child)
            self.heapify(parent)
        return self.nodes

    def add(self, node):
        self.nodes.append(node)
        self.heapify()

    def getheap(self):
        return self.nodes
    
    def delete(self, node):
        self.nodes.remove(1)
        self.heapify()

    def insert(self, node):
        self.nodes.append(node)
        self.heapify()




unsorted_array = [100, 230, 44, 1, 74, 12013, 84]
unsorted_array2 = [100, 19, 36,17,3,25,1,2,7]
myHeap = heap(unsorted_array2)
myHeap.delete(1)
myHeap.insert(1)
print(myHeap.getheap())


            