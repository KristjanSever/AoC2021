import copy
class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    def edges(self):
      return self.getEdges()
    def getVertices(self):
        return list(self.gdict.keys())
    def addVertex(self, vrtx):
        if vrtx not in self.gdict:
            self.gdict[vrtx] = []
    def addEdge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        self.gdict[vrtx1].append(vrtx2)
        self.gdict[vrtx2].append(vrtx1)
    def getEdges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename
    def getEdgesOfVertice(self,vertice):
        edges = []
        for nxtvrtx in self.gdict[vertice]:
            if {nxtvrtx, vertice} not in edges:
                edges.append({vertice, nxtvrtx})
        return edges

    def getOtherSide(self,vertice):
        vertices = []
        
        for nxtvrtx in self.gdict[vertice]:
            if {nxtvrtx, vertice} not in vertices:
                vertices.append(nxtvrtx)
        return vertices


def numOfPaths(g, curVert, used, path):
    path.append(curVert)
    print(curVert)
    print('path',path)
    print('used',used)
    if curVert in used:
        print('cant do this,retrace...')
        return 0
    if curVert == curVert.lower() and curVert != 'end':
        used[curVert] = True
    if curVert == 'end':
        return 1
    else:
        paths = 0
        print('possible:',g.getOtherSide(curVert))
        for edgeVertice in g.getOtherSide(curVert):
            newPath = copy.deepcopy(path)
            newUsed = copy.deepcopy(used)
            paths += numOfPaths(g, edgeVertice, newUsed, newPath)
        return paths

f = open('input.txt','r')
g = graph()
for line in f:
    edge = line.rstrip().split('-')
    g.addVertex(edge[0])
    g.addVertex(edge[1])
    g.addEdge(edge)

print(numOfPaths(g,'start', {},[]))
