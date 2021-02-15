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

def astar(mapSize, startingPoint, maxRockHeight , settlingSite, searchMap):


print(astar(mapSize,startingPoint,maxRockHeight,settlingSites[0],searchMap))