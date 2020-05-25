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

    inedges = {i:[] for i in range(n)}
    print("loading "+graph+'/edgelist'+suffix)
    with open(graph+'/edgelist'+suffix, 'r') as fin:
        for line in fin:
            u, v = line.split()
            u, v = int(u), int(v)
            inedges[v].append(u)
            if isdirected==False:
                inedges[u].append(v)

    print("writing "+graph+'/indegreelist'+suffix)
    with open(graph+'/indegreelist'+suffix, 'w') as fout:
        for i in range(n):
            fout.write(str(i)+" "+str(len(inedges[i]))+"\n")
