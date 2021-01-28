def rangeChecker(coord):
    for x in coord:
        if x < -10000.00 or x > 10000.00:
            raise Exception("Sorry, your coordinates are out of range.")


def calcDistance(start, end):
    sumOfSquares = sum([(start[i] - end[i]) ** 2 for i in range(3)])

    return sumOfSquares ** 0.5


def translate(stringCoord):
    points = stringCoord.split()
    coord = [float(x) for x in points]

    return coord


def findPath(start, finish, stations):
    if start == finish:
        return 0

    distances = []

    for station in stations:
        unseenStations = stations.copy()
        unseenStations.remove(station)
        distances.append(
            max(calcDistance(start, station), findPath(station, finish, unseenStations))
        )

    return min(distances)


destCoord = translate(input())
rangeChecker(destCoord)

numStations = int(input())
if numStations < 1 or numStations > 2000:
    raise Exception("Sorry, you cannot have this number of stations.")

stations = [destCoord]
for i in range(numStations):
    stationCoord = translate(input())
    rangeChecker(stationCoord)
    stations.append(stationCoord)

print("{:.2f}".format(findPath((0, 0, 0), destCoord, stations)))
