    def __init__(self, nr):
        global index
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
        with open(header_fisier, 'r') as f:
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
        with open(fisier_output, 'w') as f:
            f.write(fisier_gdl)   