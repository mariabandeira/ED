from grafos import Graph

def load_from(fileName):
    f = open(fileName, 'r')
    n = int(f.readline())

    g = Graph(n)

    l = 0
    for line in f:
        #print(line)
        #print("ola")
        line.strip()
        numeros = line.split("\t")
        c = 0
        for i in numeros:
            if(c == g.num_vertices):
                break
            #print(i)
            g.matrix[l][c] = int(i)
            if(g.matrix[l][c] > 0):
                g.list[l].append(c)

            c += 1
        l += 1
    return g


gr = load_from("/workspaces/ED/pcv4.txt")
gr.print()
dist, ant = gr.bfs(3)
distan = gr.distancia(0, 3)
dfs = gr.dfs()
print(dist)
print(ant)
print(distan)
print(dfs)
