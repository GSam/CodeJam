import heapq

width = 80
height = 80

matrix = [None for x in range(height)]
f = open("p081_matrix.txt", "r")
for y in range(height):
    matrix[y] = [int(x) for x in f.readline().split(',')]
        

visited = [[-1 for y in range(width)] for x in range(height)]
queue = []
heapq.heappush(queue, (matrix[0][0],0,0,None))
while len(queue) > 0:
    cost,x,y,node = heapq.heappop(queue)
    if visited[y][x] == -1:
        visited[y][x] = cost
        if y == height-1 and x == width-1:
            print cost
            break
        if x < width - 1 and visited[y][x+1] == -1:
            heapq.heappush(queue, (cost+matrix[y][x+1],x+1,y,(x,y)))
        if y < height - 1 and visited[y+1][x] == -1:
            heapq.heappush(queue, (cost+matrix[y+1][x],x,y+1,(x,y)))
            
