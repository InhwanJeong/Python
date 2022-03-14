from collections import defaultdict
import math

if __name__ == '__main__':
    roomNumber = int(input())

    numberPlateDict = defaultdict(int)

    while roomNumber:
        numberPlate = roomNumber % 10
        roomNumber = int(roomNumber / 10)

        numberPlateDict[numberPlate] += 1

    # 6과 9는 같이 사용 가능
    numberPlateDict[6] += numberPlateDict[9]
    numberPlateDict[6] = math.ceil(numberPlateDict[6]/2)

    numberPlateList = [numberPlateDict[i] for i in range(0, 9)]
    numberPlateList.sort()

    print(numberPlateList[-1])

