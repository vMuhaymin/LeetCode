class Heap:
    nodes = []

    def __init__(self, list):
        for node in list:
            self.add(node)
    
    def getParentIndex(self, index):
        return ((index-1)//2)

    def add(self, node):
        self.nodes.append(node)
        self.heapify()
    
    def swap(self, firstIndex, secondIndex):
        self.nodes[firstIndex] , self.nodes[secondIndex] = self.nodes[secondIndex], self.nodes[firstIndex]

    def heapify(self, child = None):
        if child == 0:
            return self.nodes
        if not child:
            child = len(self.nodes) - 1
        parent = self.getParentIndex(child)
        if self.nodes[child] < self.nodes[parent] :
            self.swap(child, parent)
            self.heapify(parent)
        return self.nodes
    
    #Require to add few healper method (Reverse heapify for deletion)
    def delete(self, index: None):

        if not index:
            rootNode , leafNode = self.nodes[0], self.nodes[len(self.nodes)-1] 
            self.nodes[0] = leafNode
            self.nodes.pop()
            self.heapify()
            return rootNode

        node , leafNode = self.nodes[index], self.nodes[len(self.nodes)-1] 
        self.nodes[index] = leafNode
        self.nodes.pop()
        self.heapify()
        return node
    
    def getTree(self):
        return self.nodes

unsorted_array = [100, 230, 44, 1, 74, 12013, 84]
myHeap = Heap(unsorted_array)
myHeap.add(200)

print(myHeap.getTree())

    
    
         
