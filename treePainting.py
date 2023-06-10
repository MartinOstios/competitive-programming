
class Tree:
    def __init__(self) -> None:
        self.children = []
        self.ncam = []
        self.nlibre = []



    def fill_initial_list(self):
        (n, m, k) = [int(x) for x in input().split(" ")]
        self.children = [None] * (n)
        self.ncam = [None] * (n)
        for i in range(m):
            data = input()
            data_children = data.split(" ")[1:]
            self.children[int(data.split(" ")[0])] = [int(x) for x in data_children]
        
        for i, node in enumerate(self.children):
            if node is None:
                self.ncam[i] = (0, 1)

        for i in range(n - 1, -1, -1):
            if self.ncam[i] is None:
                nodo = 0
                camino = 0
                mejorNodo = 0
                #print("---------------")
                children_nodes = self.children[i]
                #print(self.ncam[i])
                #print(children_nodes)
                for node in children_nodes:
                    if self.ncam[node] is not None:
                        camino += self.ncam[node][0]
                        mejorNodo = self.ncam[node][1]
                        if mejorNodo > nodo:
                            nodo = mejorNodo
                if nodo == k:
                    camino += 1
                    nodo = 0
                else:
                    nodo += 1
                self.ncam[i] = (camino, nodo)

        return self.ncam[0][0]
    


if __name__ == "__main__":
    tree = Tree()
    print(tree.fill_initial_list())
    