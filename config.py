
bgColor = (17, 17, 17)
screenSize = (1024, 768)
fps = 60

mapSize = (5, 5)
tileSize = (128, 64)
tileCount = mapSize[0] * mapSize[1]
origin = (mapSize[0] - 1) * tileSize[0] // 2, 0
mapSizePixels = mapSize[0] * tileSize[0], mapSize[1] * tileSize[1]
surfaceSize = mapSizePixels[0], mapSizePixels[1] + 10
maxAreasPerRow = 9

scrollSpeed = 800
scrollMargin = 100

uiBgColor = (17, 17, 17)
uiPadding = 20
uiGap = 20

costAnimDuration = 2
costAnimYLength = 80
costOffsetY = 30

rawTile = 0
ploughedTile = rawTile + 1
plantedTile = ploughedTile + 1
readyTile = plantedTile + 2
fireTile = readyTile + 1
stoneTile = fireTile + 1

coins = 15
ploughCost = 1
plantCost = 2
waterCost = 3
pickCost = 2
workerCost = 5
expandCost = 10
harvestGain = 20
growDuration = 5
workerSpeed = 0.65
workDuration = .6
salary = 1
salaryFrequency = 5

firstWorkerPos = (0, mapSize[1] // 2 - 1)
