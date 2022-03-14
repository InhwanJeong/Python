# time limit: 1sec
# memory limit: 512MB
import sys
import itertools

if __name__ == '__main__':
    '''
        1. 도시의 칸은 (r, c)와 같은 형태로 나타내고, r행 c열 또는 위에서부터 r번째 칸, 왼쪽에서부터 c번째 칸을 의미한다. r과 c는 1부터 시작한다.
        2. cityArray 0: empty 1: home 2: chicken
        3. 임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|로 구한다
        
        :print 도시의 치킨 거리의 최솟값
    '''
    arrayLength, maxStore = map(int, sys.stdin.readline().split())
    cityArray = [list(map(int, sys.stdin.readline().split())) for _ in range(arrayLength)]

    chickenLocation = [
        [r + 1, c + 1]
        for r, array in enumerate(cityArray)
        for c, value in enumerate(array)
        if value == 2
    ]
    homeLocation = [
        [r + 1, c + 1]
        for r, array in enumerate(cityArray)
        for c, value in enumerate(array)
        if value == 1
    ]

    chickenLocationDistanceList = []

    # 치킨집 기준 치킨 거리
    for r1, c1 in chickenLocation:
        chickenLocationDistance = [
            abs(r1-r2) + abs(c1-c2)
            for r2, c2 in homeLocation
        ]
        chickenLocationDistanceList.append(chickenLocationDistance)

    countHome = len(homeLocation)
    combinationsList = list(itertools.combinations(chickenLocationDistanceList, maxStore))

    combinationsListCompare = []

    for itemTuple in combinationsList:
        min_list = []
        for i in range(countHome):
            tmp = [itemTuple[j][i] for j in range(len(itemTuple))]
            min_list.append(min(tmp))
        combinationsListCompare.append(sum(min_list))
    print(min(combinationsListCompare))