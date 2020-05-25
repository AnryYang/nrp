import sys


if __name__=='__main__':
    graph = sys.argv[1]
    directed = int(sys.argv[2])
    full = int(sys.argv[3])
    if directed>0:
        isdirected=True
    else:
        isdirected=False

    if full>0:
        suffix = '.txt'
    else:
        suffix = '.train.txt'

    with open(graph+'/attr.txt', 'r') as fin:
        line = fin.readline()
        n = int(line.split('=')[1])

    edges = {i:[] for i in range(n)}
    print("loading "+graph+'/edgelist'+suffix)
    with open(graph+'/edgelist'+suffix, 'r') as fin:
        for line in fin:
            u, v = line.split()
            u, v = int(u), int(v)
            edges[u].append(v)
            if isdirected==False:
                edges[v].append(u)
    print("writing "+graph+'/outdegreelist'+suffix)
    with open(graph+'/outdegreelist'+suffix, 'w') as fout:
        for i in range(n):
            for j in edges[i]:
                deginv = 1.0/len(edges[i])
                fout.write(str(i)+" "+str(j)+" "+str(deginv)+"\n")
