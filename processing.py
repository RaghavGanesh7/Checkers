from collections import deque
from queue import PriorityQueue

def ValidPath(x,y,x2,y2,searchMap,threshold):
    if abs(abs(searchMap[y][x])-abs(searchMap[y2][x2])) <= threshold:
        return True
    else:
        return False
def bfs(mapSize, startingPoint, maxRockHeight , settlingSite, searchMap):
    if(len(searchMap)==0):
        return "FAIL"
    queue = deque([[startingPoint]])
    x = startingPoint[0]
    y = startingPoint[1]
    seen = set([(x,y)])
    GoalX = settlingSite[0]
    GoalY = settlingSite[1]
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if y==GoalY and x==GoalX:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1), (x-1,y-1),(x+1,y+1),(x+1,y-1),(x-1,y+1)):
            if 0 <= x2 < int(mapSize[0]) and 0 <= y2 < int(mapSize[1]) and ValidPath(x,y,x2,y2,searchMap,maxRockHeight)and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
                #print(queue)
    return "FAIL"




f =  open("output.txt",'r').read().splitlines()
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


print(algo, mapSize, startingPoint, maxRockHeight, n , settlingSites, searchMap)
#print(bfs(mapSize,startingPoint,maxRockHeight,settlingSites[0],searchMap))
#print(ucs(mapSize,startingPoint,maxRockHeight,settlingSites[0],searchMap))
pQueue = PriorityQueue()
pQueue.put((3,[[startingPoint]]))
pQueue.put((2,[[startingPoint]]))
pQueue.put((2,[[1,2]]))
print(pQueue.get())
