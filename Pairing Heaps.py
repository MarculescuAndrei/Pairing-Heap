class Node:
    
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.sibling = None

class pairingHeap:
    
    def __init__(self, rootValue):
        
        self.root = Node(rootValue)

    def merge(self, root):
        
        if root.value < self.root.value:
            self.root.sibling = root.leftChild
            root.leftChild = self.root
            self.root = root
        else:
            root.sibling = self.root.leftChild
            self.root.leftChild = root
        return self.root

    def insert(self, value):
        newNode = Node(value)
        self.merge(newNode)

    def showRoot(self):
        return self.root.value

    def delete(self):

        Ok = False
        Z = self.root.value
        X = self.root.leftChild
        siblingsList = []
        while not Ok:
            Y = X.sibling
            X.sibling = None
            siblingsList.append(X)
            X = Y
            if X == None:
                Ok = True

        # 1st Pass
        siblingsList2 = []
        for j in range(0, len(siblingsList), 2):
            P1 = siblingsList[j]
            try:
                P2 = siblingsList[j+1]
            except:
                siblingsList2.append(P1)
                P2 = None
            if P2 is None:
                break
            if P1.value < P2.value:
                P2.sibling = P1.leftChild
                P1.leftChild = P2
                siblingsList2.append(P1)
            else:
                P1.sibling = P2.leftChild
                P2.leftChild = P1
                siblingsList2.append(P2)

        # 2nd Pass
        for i in range(1, len(siblingsList2)):
            Condition = 0
            if Condition == 0:
                P1 = siblingsList2[-i]
                Condition = 1
            P2 = siblingsList2[-(i+1)]
            if P1.value < P2.value:
                P2.sibling = P1.leftChild
                P1.leftChild = P2
                P1 = P1
            else:
                P1.sibling = P2.leftChild
                P2.leftChild = P1
                P1 = P2
        self.root = P1
        return Z




    def display(self):
        
        P = self.root
        print('Root Node:', end='')
        print(P.value)
        print('\r')
        def Show(node, leftchild, sibling):
            if leftchild is not None:
                print("Node " + str(node.value), 'Left Child: ', end='')
                print(leftchild.value)
                Show(leftchild, leftchild.leftChild, leftchild.sibling)

            if sibling is not None:
                print("Node " + str(node.value), 'Sibling: ', end='')
                print(sibling.value)
                Show(sibling, sibling.leftChild, sibling.sibling)

        Show(P, P.leftChild, P.sibling)


N = int(input("Number of operations: "))
print("Types of Operations :")
print("1 - Insert ; 2 - Show the Pairing Heap; 3 - Print the Root; 4 - Deletes the Root")
print("\n")

X = int(input("The 1st Root is: "))
Obj = pairingHeap(X)

for i in range(N-1):
    Op = int(input("Operation: "))
    if Op == 1:
        X = int(input("Item to insert: "))
        Obj.insert(X)
    elif Op == 2:
        print('____________________________')
        Obj.display()
        print('____________________________')
    elif Op == 3:
        print("The root is " + str(Obj.showRoot()))
    elif Op == 4:
        Obj.delete()



