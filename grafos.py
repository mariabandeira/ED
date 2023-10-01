import queue

class Graph:
    def __init__(self, n):
        self.num_vertices = n
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]
        self.list = [[] for _ in range(n)]


    def print(self):
        print(self.matrix)
        print(self.list)


    def bfs(self, source):
        dist = [-1 for _ in range(self.num_vertices)]
        ant = [-1 for _ in range(self.num_vertices)]
        isVisited = [False for _ in range(self.num_vertices)]
        Q = queue.Queue()
        Q.put(source)
        isVisited[source] = True
        dist[source] = 0

        while Q.empty() != True:
            p = Q.get()
            #print("Vertice: " + str(p))

            for v in self.list[p]:
                if isVisited[v] == False:
                    dist[v] = dist[p] + 1
                    ant[v] = p
                    Q.put(v)
                    isVisited[v] = True

        return dist, ant

    def distancia(self, s, t): 
        dist = [-1 for _ in range(self.num_vertices)]
        ant = [-1 for _ in range(self.num_vertices)]
        isVisited = [False for _ in range(self.num_vertices)]
        Q = queue.Queue()
        Q.put(s)
        isVisited[s] = True
        dist[s] = 0

        while Q.empty() != True:
            p = Q.get()
            #print("Vertice: " + str(p))

            for v in self.list[p]:
                if isVisited[v] == False:
                    dist[v] = dist[p] + 1
                    ant[v] = p
                    Q.put(v)
                    isVisited[v] = True
        
        if t >= len(dist):
            return "O vértice procurado não pertence ao grafo."
        else:    
            if dist[t] == -1:
                return "O caminho não existe."
            else:  
                return dist[t]

    def dfs(self):
        pai = [-1 for _ in range(self.num_vertices)]
        isVisited = [False for _ in range(self.num_vertices)]
        Q = queue.Queue()

        for i in range(self.num_vertices):
            if(isVisited[i] == False):
                Q.put(i)
                isVisited[i] = True
                while Q.empty() != True:
                    p = Q.get()
                    #print("Vertice: " + str(p))

                    for u in self.list[p]:
                        if isVisited[u] == False:
                            Q.put(u)
                            isVisited[u] = True
                            pai[u] = p 

        return pai
