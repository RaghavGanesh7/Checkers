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
def astarCost(x,y,x2,y2,searchMap):
    cost=0
    height=0
    nextheight=0
    if searchMap[y2][x2]>=0:
        cost+=searchMap[y2][x2]
    height = min(0,searchMap[y][x])
    nextheight = min(0,searchMap[y2][x2])
    return cost + abs(height-nextheight)
    

def astar(mapSize, startingPoint, maxRockHeight , settlingSite, searchMap):
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
                    cost = astarCost(x,y,x2,y2,searchMap)
                    queue.append((x2,y2,cost,path+[(x2,y2)]))
        for x2, y2 in ((x+1,y+1), (x-1,y-1), (x-1,y+1), (x+1,y-1)):
            if 0 <= x2 < int(mapSize[0]) and 0 <= y2 < int(mapSize[1]) and ValidPath(x,y,x2,y2,searchMap,maxRockHeight) and (visited[y2][x2]==0 or explored[y2][x2]==0):
                visited[y2][x2]=1
                queue.append((x2,y2,current[2]+14,path+[(x2,y2)]))
        #print(queue)
        sorted(queue,key= lambda x:x[2] )
        #print(queue)           


print(astar(mapSize,startingPoint,maxRockHeight,settlingSites[0],searchMap))