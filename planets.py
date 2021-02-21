def range_checker(coord):
    for x in coord:
        if x < -10000.00 or x > 10000.00:
            raise Exception("Sorry, your coordinates are out of range.")


def calc_distance(start, end):
    sumOfSquares = sum([(start[i] - end[i]) ** 2 for i in range(3)])

    return sumOfSquares ** 0.5


def translate(stringCoord):
    points = stringCoord.split()
    coord = [float(x) for x in points]

    return coord


def find_path(start, finish, stations):
    if start == finish:
        return 0

    distances = []

    for station in stations:
        unseenStations = stations.copy()
        unseenStations.remove(station)
        distances.append(
            max(calc_distance(start, station), find_path(station, finish, unseenStations)))

    return min(distances)


destCoord = translate(input())
range_checker(destCoord)

numStations = int(input())
if numStations < 1 or numStations > 2000:
    raise Exception("Sorry, you cannot have this number of stations.")

stations = [destCoord]
for i in range(numStations):
    stationCoord = translate(input())
    range_checker(stationCoord)
    stations.append(stationCoord)

print("{:.2f}".format(find_path((0, 0, 0), destCoord, stations)))
