graph = {
'A' : {'B': 6, 'F': 5},
'B' : {'C': 5, 'G': 6, 'A':6},
'C' : {'D': 7, 'H': 5, 'B':5},
'D' : {'E': 7, 'C':7, 'I': 8},
'E' : {'I': 6, 'N': 15, 'D': 7},
'I' : {'H': 12, 'E': 6, 'M': 10, 'D':8},
'G' : {'H': 9, 'B': 6, 'F': 8, 'K':8},
'H' : {'G': 9, 'I': 12, 'C': 5},
'F' : {'J': 7, 'A': 5, 'G': 8},
'J' : {'K': 5, 'F': 7, 'O': 7},
'K' : {'J': 5, 'L': 7, 'G': 8},
'L' : {'M': 7, 'P': 7, 'K': 7},
'M' : {'N': 9, 'L':7, 'I': 10},
'N' : {'R': 7, 'E': 15, 'M': 9},
'R' : {'Q': 9, 'N':7, 'W':10},
'Q' : {'P': 8, 'R': 9},
'P' : {'O': 13, 'L': 7, 'Q': 8, 'U': 11},
'O' : {'S': 9, 'P': 13, 'J': 7},
'S' : {'T': 9, 'O': 9},
'T' : {'U': 8, 'S': 9},
'U' : {'V': 8, 'P': 11, 'T': 8},
'V' : {'W': 5, 'U': 8},
'W' : {'R': 10, 'R': 10},
}
def dijkstra(graph,start,gas):
     shortdis = {}
     pre = {}
     unseeNodes = graph
     infinity = 99999
     path = []
     for node in unseeNodes:
         shortdis[node] = infinity
     shortdis[start] = 0
    
     while unseeNodes:
        minNode = None
        for node in unseeNodes:
            if minNode is None:
                minNode = node
            elif shortdis[node] < shortdis[minNode]:
                minNode = node
        for childNode, weight in graph[minNode].items():
            if weight + shortdis[minNode] < shortdis[childNode]:
                shortdis[childNode] = weight + shortdis
                pre[childNode] = minNode
        unseeNodes.pop(minNode)
    
     currentNode = gas
     while currentNode != start:
        try:
            path.insert(0,start)
            currentNode = pre[currentNode]
        except KeyError:
            print('Path Is not Possible')
     if shortdis[gas] != infinity:
        print('shortest distance i' + str(shortdis[gas]))
        print('the path is' + str(path))
     dijkstra(graph , 'G', 'K')
     print(shortdis)