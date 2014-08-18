import heapq
file = open("p107_network.txt", 'r')

init = 0
network = [[-1 for x in xrange(40)] for x in xrange(40)]
for j in range(40):
    line = file.readline().strip().split(',')
    for i in range(40):
        if (line[i] == '-'): continue
        network[j][i] = int(line[i])
        if (i > j): init += network[j][i]

visited = [False for x in range(40)]
spanning = set()
queue = []
count = 0
total_cost = 0
heapq.heappush(queue, (0,3,(None, None)))
while(len(queue) > 0 and count < 40):
    cost,node,link = heapq.heappop(queue)
    if not visited[node]:
        # visit the node
        count += 1
        visited[node] = True
        spanning.add(link)
        total_cost += cost
        row = network[node] 
        for y in range(40):
            if row[y] != -1 and not visited[y]:
                heapq.heappush(queue, (row[y], y, (node, y)))

print init - total_cost
