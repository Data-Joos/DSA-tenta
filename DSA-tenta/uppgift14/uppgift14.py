class node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None

class binary_search_tree:
    def __init__(self):
        self.root = None
    
    def insert(self,value): #Funktion för att inserta värden
        if self.root == None:
            self.root=node(value)#Kollar ifall vi inte har en root, isf ska värdet sättas in som en root
        else:
            self._insert(value,self.root) # "_" innebär att kalla en funktion inuti sig själv i sin egna klass.

    def _insert(self,value,cur_node):
        if value<cur_node.value: #Är värdet mindre än värdet till nuvarande node?
            if cur_node.left_child == None: #...Om ja och ifall nuvarande node inte har någon child...
                cur_node.left_child=node(value) #...Sätt då left child till det nya värdet
            else:
                self._insert(value.cur_node.left_child)#...Om ja och ifall nuvarande node har en left child så kalla funktionen (recurseviely) igen
                #och sätt nuvarande left child node som argument till cur node.
        #Om värdet istället är STÖRRE än värdet till nuvarande node...
        elif value>cur_node.value: #elif ist för else eftersom ifall det är = och vi får ett träd med flera lika värden.
            #Börja med att checka om det inte finns en right node precis som ovan
            if cur_node.right_child==None:
                cur_node.right_child=node(value)
            #Annars, kalla funktionen recurseviely igen
            else:
                self._insert(value,cur_node.right_child) 
        else: #Om värdet är lika med current node värde
            print("Value already in tree!")