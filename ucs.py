from math import sqrt

# f = open("output1.txt","r").read().splitlines()
# lines = list(f)
# algo = str(lines[0])
# mapSize = lines[1].split()
# startingPoint = lines[2].split()
# startingPoint[0] = int(startingPoint[0])
# startingPoint[1] = int(startingPoint[1])
# maxRockHeight = int(lines[3])
# n = int(lines[4])
# settlingSites = []
# counter = 0
# for i in range(5,n+5):
#     settlingSites.append(lines[i].split())
#     counter = i
# settlingSites = [list( map(int,i) ) for i in settlingSites]
# searchMap = []
# h = int(mapSize[1])
# for i in range(counter+1,counter+1+h):
#     searchMap.append(lines[i].split())
# searchMap = [list( map(int,i) ) for i in searchMap]

# dirs = [
#     lambda x, y, z, p: (x, y - 1, z + 10, p + [(x, y)]),  # up
#     lambda x, y, z, p: (x, y + 1, z + 10, p + [(x, y)]),  # down
#     lambda x, y, z, p: (x - 1, y, z + 10, p + [(x, y)]),  # left
#     lambda x, y, z, p: (x + 1, y, z + 10, p + [(x, y)]),  # right
#     lambda x, y, z, p: (x - 1, y - 1, z + 14, p + [(x, y)]),  # up left
#     lambda x, y, z, p: (x + 1, y - 1, z + 14, p + [(x, y)]),  # up right
#     lambda x, y, z, p: (x - 1, y + 1, z + 14, p + [(x, y)]),  # down left
#     lambda x, y, z, p: (x + 1, y + 1, z + 14, p + [(x, y)])  # down right
# ]


# def thresholdValid(x1,y1,x2,y2,searchMap,threshold):
#     if abs(abs(searchMap[y][x])-abs(searchMap[y2][x2])) <= threshold:
#         return True
#     else:
#         return False
# def valid(x, y,grid):
#     return 0 <= x < len(grid) and 0 <= y < len(grid[0])

# def adjacent(grid, frontier,threshold):
#     for (x, y, z, p) in frontier:
#         x1 = x
#         y1 = y
#         for d in dirs:
#             x2, y2, nz, np = d(x,y,z,p)
#             if valid(x2,y2,grid) and thresholdValid(x1,y1,x2,y2,grid,threshold):
#                 print(x2,y2,nz,np)
#                 yield (x2, y2, nz, np)


# def flood(grid, frontier,threshold):
#     res = list(adjacent(grid, frontier,threshold))
#     return res

# def shortest(grid, start, end,threshold):
#     start, end = tuple(start), tuple(end)
#     frontier = [(start[0], start[1], 0, [])]
#     res = []
#     i=0
#     while frontier:
#         frontier=flood(grid, frontier,threshold)
#         for (x, y, z, p) in frontier:
#             if (x, y) == end:
#                 res.append((z, p + [(x, y)]))
#         i+=1
#     if not res:
#         return ()
#     return sorted(res)[0]

# x = startingPoint[0]
# y = startingPoint[1]
# goal = settlingSites[0]
# GoalX = goal[0]
# GoalY = goal[1]
# print(shortest(searchMap, (x, y), (GoalX, GoalY), maxRockHeight))



































f = open("output1.txt","r").read().splitlines()
lines = list(f)
algo = str(lines[0])
mapSize = lines[1].split()
startingPoint = lines[2].split()
startingPoint[0] = int(startingPoint[0])
startingPoint[1] = int(startingPoint[1])
maxRockHeight = int(lines[3])
n = int(lines[4])
settlingSites = []
counter = 0
for i in range(5,n+5):
    settlingSites.append(lines[i].split())
    counter = i
settlingSites = [list( map(int,i) ) for i in settlingSites]
searchMap = []
h = int(mapSize[1])
for i in range(counter+1,counter+1+h):
    searchMap.append(lines[i].split())
searchMap = [list( map(int,i) ) for i in searchMap]

def ValidPath(x,y,x2,y2,searchMap,threshold):
    if abs(abs(searchMap[y][x])-abs(searchMap[y2][x2])) <= threshold:
        return True
    else:
        return False

def ucs(mapSize, startingPoint, maxRockHeight , settlingSite, searchMap):
    if(len(searchMap)==0):
        return "FAIL"
    visited = [[0 for x in range(int(mapSize[0]))] for y in range(int(mapSize[1]))]
    explored = [[0 for x in range(int(mapSize[0]))] for y in range(int(mapSize[1]))] 
    queue = [(startingPoint[0], startingPoint[1], 0, [])]
    print(visited,explored,searchMap)
    x = startingPoint[0]
    y = startingPoint[1]
    visited[y][x] = 1
    GoalX = settlingSite[0]
    GoalY = settlingSite[1]
    while queue:
        #print(queue)
        current = queue[0]
        path = current[-1]
        x = current[0]
        y = current[1]
        #print(x,y)
        if visited[y][x]==1 and explored[y][x]==1:
            #print(queue)
            queue.pop(0)
            continue
        explored[y][x]=1
        queue.pop(0)
        if x==GoalX and y==GoalY:
            #print(path)
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < int(mapSize[0]) and 0 <= y2 < int(mapSize[1]) and ValidPath(x,y,x2,y2,searchMap,maxRockHeight):
                print(x2,y2)
                if explored[y2][x2]==0 or visited[y2][x2]==0:
                    visited[y2][x2]=1
                    #print(current[2])
                    queue.append((x2,y2,current[2]+10,path+[(x2,y2)]))
        for x2, y2 in ((x+1,y+1), (x-1,y-1), (x-1,y+1), (x+1,y-1)):
            if 0 <= x2 < int(mapSize[0]) and 0 <= y2 < int(mapSize[1]) and ValidPath(x,y,x2,y2,searchMap,maxRockHeight) and (visited[y2][x2]==0 or explored[y2][x2]==0):
                visited[y2][x2]=1
                queue.append((x2,y2,current[2]+14,path+[(x2,y2)]))
        #print(queue)
        sorted(queue,key= lambda x:x[2] )
        #print(queue)       
    return "FAIL"
        
#print(searchMap[2][0])
print(ucs(mapSize,startingPoint,maxRockHeight,settlingSites[0],searchMap))
