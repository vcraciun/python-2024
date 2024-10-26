index = 1
relatii = []
noduri = []
class Node:
    def __init__(self, data, Left=None, Right=None): 
        global index
        self.data = data
        self.left = Left
        self.right = Right
       
        self.idx = f"n{index:>02}"
        index += 1
    def descopera_noduri(self):     
        global noduri
        global relatii
        if self.left:
            relatii += [(self.idx, self.left.idx, 48)]
            self.left.descopera_noduri()
        noduri += [self]     
        if self.right:
            relatii += [(self.idx, self.right.idx, 33)]
            self.right.descopera_noduri()

    def ListeazaArbore(self):
        fisier_gdl = ""
        with open("header.txt", 'r') as f:
            header = f.read()        
        fisier_gdl += header
        self.descopera_noduri()
        for nod in noduri:
            text_nod = f"node: {{\ntitle: \"{nod.idx}\"\nlabel: \"{nod.data}\"}}\n"            
            fisier_gdl += text_nod
        for nod in relatii:
            text_nod = f"edge: {{sourcename: \"{nod[0]}\" targetname: \"{nod[1]}\" color: {nod[2]}}}\n"
            fisier_gdl += text_nod
        fisier_gdl += "}\n"
        with open("ceva.gdl", 'w') as f:
            f.write(fisier_gdl)  
def eval(node):
    if isinstance(node.data,(int,float)):
        return node.data
    elif node.data=='+':
        return eval(node.left)+eval(node.right)
    elif node.data=='-':
        return eval(node.left)-eval(node.right)
    elif node.data=='*':
        return eval(node.left)*eval(node.right)
    elif node.data=='/':
        return eval(node.left)//eval(node.right)
    
def print_ast(node,level=0):
    indent=' '*(level*2)
    if node:
        print(f"{indent}{node.data}")
        if node.left:
            print(f"{indent}Left:")
            print_ast(node.left,level+1)
        if node.right:
            print(f"{indent}Right:")
            print_ast(node.right,level+1)
#AST - expresie: 13*2-11+5+21/7
root=Node('+',
        Node('-',
             Node('*',
                  Node(13),
                  Node(2)),
             Node(11)
             ),
          Node('+',
               Node(5),
               Node('/',Node(21),Node(7))
               )
          )

print(eval(root))
print_ast(root)
root.ListeazaArbore()
        